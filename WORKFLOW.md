# Connect the worker and checker
Use the runtime's existing delegation/orchestration mechanism. Confirm file and source access first. No particular API, model or subscription is assumed.

1. Save the original brief, sources and approved rubric in the user's private workspace. Give the job a stable ID.
2. Worker creates artifact v1. Record status Reviewing, version and owner.
3. Start the separate checker with the review packet. Exclude the worker's reasoning. Record whether the context was genuinely separate.
4. Validate the report structure with the supplied script, then verify its artifact ID and criterion coverage against the original brief. Invalid reports require a corrected review; they are never passes. Allow one malformed-report retry, then escalate. Review retries count against the agreed budget.
5. PASS/PASS_WITH_FLAGS: retain the exact reviewed artifact, report and optional findings; hand over according to the agreed approval rules.
6. FAIL: send the specific findings to the worker. Preserve the original brief and sources. Worker creates v2, then v3 if needed. Re-review every required criterion on each new version, not only the repaired ones.
7. BLOCKED, exhausted revision budget, or a required human decision: stop and record the missing evidence/action and owner. Never weaken a criterion or claim an unread artifact passed.
8. Save the record: job ID, input, artifact/version, review reports, round, status, next action and owner. Keep this where authorised teammates can access it.

## Acceptance run
Use the text fixture for the first round: the initial draft must FAIL, its source-faithful correction must PASS the text criteria. Then test an actual rendered deck with a planted clipping defect to validate the visual route. Finally test an unfixable missing source and confirm escalation. The text example alone is not an end-to-end deck validation.

Until these tests run in the chosen runtime, describe the connected loop as unverified. Scheduling and cross-app interception require separate implementation.
