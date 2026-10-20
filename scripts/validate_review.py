#!/usr/bin/env python3
"""Validate report shape and verdict consistency; does not judge artifact quality."""
import json,sys

def validate(r):
    if not isinstance(r,dict): raise ValueError('Report must be an object')
    for k in ('artifact','round','verdict','checks','findings','next_action'):
        if k not in r: raise ValueError('Missing '+k)
    if not isinstance(r['artifact'],str) or not r['artifact'].strip(): raise ValueError('Missing artifact version')
    if type(r['round']) is not int or r['round'] not in (0,1,2): raise ValueError('Round must be 0, 1 or 2')
    if r['verdict'] not in ('PASS','PASS_WITH_FLAGS','FAIL','BLOCKED'): raise ValueError('Invalid verdict')
    if not isinstance(r['checks'],list) or not r['checks']: raise ValueError('Checks required')
    if not isinstance(r['findings'],list): raise ValueError('Findings must be a list')
    for c in r['checks']:
        if not isinstance(c,dict) or c.get('status') not in ('PASS','FAIL','UNVERIFIED'): raise ValueError('Invalid check')
        if any(not isinstance(c.get(k),str) or not c[k].strip() for k in ('criterion','evidence')): raise ValueError('Check evidence required')
    for f in r['findings']:
        if not isinstance(f,dict) or f.get('severity') not in ('blocker','improvement'): raise ValueError('Invalid finding')
        if any(not isinstance(f.get(k),str) or not f[k].strip() for k in ('location','evidence','correction')): raise ValueError('Finding details required')
    states={c['status'] for c in r['checks']}
    blockers=any(f['severity']=='blocker' for f in r['findings'])
    v=r['verdict']
    if v in ('PASS','PASS_WITH_FLAGS'):
        if states!={'PASS'} or blockers: raise ValueError('A passing verdict cannot contain failed or unverified checks or blockers')
        if (v=='PASS') != (len(r['findings'])==0): raise ValueError('Use flags only for specific improvements')
        expected={'handover'}
    elif v=='FAIL':
        if 'FAIL' not in states or 'UNVERIFIED' in states or not blockers: raise ValueError('FAIL requires an observed defect; missing checks require BLOCKED')
        expected={'escalate'} if r['round']==2 else {'revise','escalate'}
    else:
        if 'UNVERIFIED' not in states or not blockers: raise ValueError('BLOCKED requires an unverified check and blocker')
        expected={'escalate'}
    if r['next_action'] not in expected: raise ValueError('Invalid next action for verdict/round')
    return True

if __name__=='__main__':
    try:
        if len(sys.argv)!=2: raise ValueError('Usage: python3 scripts/validate_review.py report.json')
        with open(sys.argv[1]) as f: validate(json.load(f))
        print('Valid review contract. Verify artifact identity, rubric coverage and substantive findings separately.')
    except (ValueError,OSError,TypeError,KeyError) as exc:
        print('INVALID: '+str(exc),file=sys.stderr);sys.exit(1)
