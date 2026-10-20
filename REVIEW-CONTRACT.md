# Review contract v1
Input: job ID, exact artifact ID/version, objective, source evidence, confirmed rubric, named owner, round (0 initial; 1–2 revisions) and inspection access. A review is invalid if the reviewer receives the worker's private reasoning or is asked to rubber-stamp a verdict.

Output JSON:
- `artifact`: nonempty exact ID/version.
- `round`: integer 0, 1 or 2.
- `verdict`: PASS, PASS_WITH_FLAGS, FAIL or BLOCKED.
- `checks`: nonempty list of `{criterion, status, evidence}`. Status is PASS, FAIL or UNVERIFIED. Each agreed rubric criterion must appear; the caller checks coverage against the brief.
- `findings`: list of `{severity, location, evidence, correction}`. Severity is blocker or improvement.
- `next_action`: handover, revise or escalate.

PASS: all required checks passed; no findings. PASS_WITH_FLAGS: checks passed and only specific optional improvements remain. FAIL: an observed material defect; at least one failed check and blocker finding. BLOCKED: required inspection/evidence unavailable; at least one UNVERIFIED check and blocker finding. An unverified required check prevents any passing verdict. If there are both observed failures and unverified checks, use BLOCKED and report both.

FAIL with round 0 or 1 → revise, unless the issue needs an owner decision, in which case escalate. FAIL at round 2 → escalate. BLOCKED → escalate. Passing verdict → handover. Handover follows the user's agreed human-approval policy; it does not authorise publication or sending.

PASS means this version met the tested criteria. It is not a guarantee of truth or perfection.
