---
name: set-standards
description: Convert a user's quality requirements and examples into an observable review rubric and test a separate quality reviewer. Use when setting up the Standard Setter for a defined output.
---
# Make quality observable
Ask for the artifact, audience, repeated corrections, good and bad examples, source material, available inspection tools and human decisions.

Turn “make it good” into conditions with evidence. For example: a slide's factual claim matches the cited passage; all required sections are present; the rendered slide fits on the page; the CTA points to the approved destination. Agree style preferences separately from hard defects. Offer a proposed rubric and ask the owner to confirm it.

Create QUALITY-BRIEF.md using `templates/quality-brief.md`. Define what to inspect, how to inspect it, what counts as a defect, the owner, maximum two revision rounds and any required expert review. The checker cannot silently change the brief or the pass threshold.

Prepare an independent review packet using `REVIEW-CONTRACT.md`. Ask a distinct reviewer context to inspect the exact artifact and original evidence. Use a fresh chat if separate-agent delegation is unavailable; mark the handoff manual. Do not label the worker's second pass an independent review.

Test with a clean example and planted defects: unsupported factual claim, missing required element, wrong audience or destination, and an inaccessible required source. For visual work include a clipping/readability defect in a rendered artifact. Record actual detection, misses, false positives and untested checks. A supplied text example cannot validate visual inspection.

Connect the revision loop according to WORKFLOW.md. Verify that a FAIL reaches the worker, the worker changes the artifact, the reviewer receives the new version, and the final work record shows the correct verdict. Stop on missing access or exhausted retries. A second authorised person should be able to find the result and unresolved issues without the original conversation.
