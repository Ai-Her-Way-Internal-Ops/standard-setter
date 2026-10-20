# The Standard Setter
## Your standards. A second set of AI eyes. Fewer corrections landing on you.
A guided reviewer kit from AI Her Way. Define what good work looks like, give a separate agent the job of checking it, and return specific corrections to the worker before the result reaches you.

**Start here:** open this folder in an AI workspace and paste [START-HERE.md](START-HERE.md). You will leave with a quality brief, a reviewer, a bounded revision workflow and a tested example.

The kit adapts AI Her Way's independent-review method. Our motivating use case is speaker decks: check source claims, narrative, readability, audience fit and the close before the human reviews the deck. The [worked example](examples/deck-review.md) is synthetic and contains no client material.

## The loop
Brief → Worker → Separate reviewer → Specific corrections → Worker revises → Reviewer checks the new version → Human review or agreed handoff.

Maximum: initial review plus two revision reviews. An unresolved defect then goes to the owner. A missing source, permission or tool can go straight to the owner. A passing score never overrides a hard failure.

## What is included
- A guided setup prompt that turns preferences into observable criteria.
- A portable reviewer definition in `.claude/agents/standard-setter.md`.
- A rubric template and review contract.
- A synthetic deck test with defective and corrected versions.
- A deterministic validator for review reports, with sample reports.

Run `python3 scripts/validate_review.py examples/fail-report.json` to check a report's structure. The validator checks the contract; the AI reviewer and human still judge the work itself.

## Connect it honestly
An agent-capable runtime can route work to a separate reviewer and return feedback automatically if its orchestration supports it. Read [WORKFLOW.md](WORKFLOW.md), test the full loop, and record the observed result. This repository supplies instructions and contracts; it does not intercept every AI tool on your computer.

With ordinary chat, use two separate conversations and move the review packet and verdict between them manually. That gives you a usable first review; the connected automatic loop is a subsequent setup task. Your subscription/API costs apply.

A fresh reviewer can still share the worker's blind spots. Test with planted defects and keep qualified human review for consequential decisions. Visual claims require the rendered artifact to be inspected. If it cannot see the slides, it must mark the visual review incomplete.

## Continue
Explore [The AI Handover Bootcamp](https://go.aiherway.com.au/bootcamp-2026) to build a first business agent with skills, a separate checker and a shared handover record.
