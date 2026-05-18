# LEO Institutional Approval Review Demo README v1.0

## Status

PUBLIC MVP DEMONSTRATION — REVIEW READY

---

# LEO Institutional Approval Review

The **Institutional Approval Review** demo is the first public MVP slice of the LEO project.

It demonstrates a local, human-controlled evidence-review workflow for institutional approval chains.

The demo shows how LEO can help reviewers inspect approval-process signals, understand evidence, record human review actions, and export a review package without creating autonomous institutional decisions.

---

# What This Demo Shows

This demo demonstrates the following workflow:

```text
INPUT
→ INPUT QUALITY CHECK
→ ANALYSIS
→ EVIDENCE REPORT
→ HUMAN REVIEW
→ EXPORT PACKAGE
```

The workflow is designed to remain:

- local-first;
- reproducible;
- human-controlled;
- evidence-oriented;
- non-production;
- non-autonomous.

---

# What LEO Does In This Demo

LEO:

- reads structured institutional approval input data;
- checks input quality;
- generates review findings;
- creates evidence objects;
- links findings to evidence;
- provides reviewer questions;
- suggests review-oriented next actions;
- validates evidence report structure;
- supports local human review through a dashboard;
- exports a human review package.

---

# What LEO Does NOT Do

LEO does NOT:

- approve institutional actions;
- reject institutional requests;
- block payments;
- punish staff;
- issue legal conclusions;
- issue donor compliance conclusions;
- replace management boards;
- mutate production records;
- write to canonical registries;
- access signing keys;
- execute external institutional actions.

Human reviewers remain responsible for interpretation, escalation, and institutional decisions.

---

# Zero-Autonomy Boundary

This demo preserves the following boundary:

```text
EVIDENCE_GENERATION
!=
AUTONOMOUS_DECISION
```

and:

```text
HUMAN_REVIEW
!=
AUTONOMOUS_ENFORCEMENT
```

The dashboard is a reviewer interface, not an institutional control system.

---

# Directory Contents

Expected directory structure:

```text
institutional_approval_review/
│
├── input/
├── output/
├── tests/
│
├── institutional_approval_input_quality_report.py
├── institutional_approval_review_pipeline.py
├── institutional_approval_evidence_report_validator.py
├── institutional_approval_human_review_package.py
├── leo_institutional_approval_dashboard.html
│
├── README.md
├── QUICK_START.md
├── WORKFLOW_OVERVIEW.md
└── SAFETY_BOUNDARY.md
```

---

# Core Files

## `institutional_approval_input_quality_report.py`

Checks whether the local input dataset is structurally usable for review.

Expected output:

```text
output/institutional_approval_input_quality_report.json
```

---

## `institutional_approval_review_pipeline.py`

Runs the local review pipeline and generates evidence-backed review findings.

Expected output:

```text
output/institutional_approval_evidence_report.json
```

---

## `institutional_approval_evidence_report_validator.py`

Validates the evidence report structure and boundary assumptions.

---

## `institutional_approval_human_review_package.py`

Creates or validates a local human review package structure.

Expected output:

```text
output/institutional_approval_human_review_package.json
```

---

## `leo_institutional_approval_dashboard.html`

Local browser dashboard for reviewer workflow.

The dashboard allows a user to:

- load the evidence report;
- inspect priority findings;
- review selected findings;
- save local human review actions;
- export a review package;
- reload review package state.

---

# Quick Start

From this directory:

```bash
python institutional_approval_input_quality_report.py
python institutional_approval_review_pipeline.py
python institutional_approval_evidence_report_validator.py
```

Then open:

```text
leo_institutional_approval_dashboard.html
```

in a browser.

Load:

```text
output/institutional_approval_evidence_report.json
```

Then review a finding and export:

```text
institutional_approval_human_review_package.json
```

---

# Example Reviewer Workflow

1. Open the dashboard.
2. Load the evidence report.
3. Select a Critical or High finding.
4. Read the reviewer question.
5. Choose a human review action.
6. Add a reviewer note.
7. Save the review record.
8. Download the review package.
9. Reload the package to confirm review state persistence.

---

# Review Actions

Supported reviewer actions:

```text
ESCALATE_FOR_REVIEW
ACCEPT_AS_JUSTIFIED
MARK_FALSE_POSITIVE
REQUEST_MORE_EVIDENCE
DEFER_REVIEW
```

These are human review classifications only.

They do not trigger autonomous institutional action.

---

# Example Review Package

A human review package may include:

- reviewed finding ID;
- review action;
- reviewer note;
- reviewer ID;
- evidence IDs;
- follow-up status;
- zero-autonomy acknowledgement;
- source report summary.

The review package is a local evidence-review artifact, not a legal decision.

---

# Current Validated Baseline

Current validated baseline:

```text
Dashboard v0.2 manually validated
Review package round-trip validated
Combined runtime baseline: 2451 passed in 56.87s
```

---

# Public Safety Notes

This demo is:

- research-oriented;
- local-first;
- non-production;
- reviewer-controlled;
- evidence-centric.

This demo is not:

- production governance software;
- autonomous enforcement software;
- legal decision software;
- automated corruption verdict software.

---

# Recommended Use

This demo may be useful for:

- governance tooling research;
- institutional workflow review;
- evidence lineage experiments;
- reviewer workflow prototyping;
- auditability research;
- public-interest technology exploration.

---

# Not Recommended Use

This demo should not be used as:

- a production institutional decision system;
- a legal compliance engine;
- an automated approval engine;
- an enforcement system;
- a replacement for responsible human governance.

---

# Test Commands

From the demo directory:

```bash
python -m pytest tests/test_institutional_approval_input_quality_report.py
python -m pytest tests/test_institutional_approval_review_pipeline.py
python -m pytest tests/test_institutional_approval_evidence_report_validator.py
python -m pytest tests/test_institutional_approval_human_review_package.py
```

From the runtime root, the combined test command used during validation was:

```bash
python -m pytest tests demos/institutional_approval_review/tests
```

---

# Design Philosophy

LEO does not replace the reviewer.

LEO helps structure the review.

The system creates evidence and questions.

Humans remain accountable.

---

# Boundary Declaration

This demo preserves the following invariant:

```text
PUBLIC_DEMO
!=
PRODUCTION_GOVERNMENT_SYSTEM
!=
AUTONOMOUS_INSTITUTIONAL_AUTHORITY
!=
AUTONOMOUS_ENFORCEMENT_ENGINE
```

LEO remains:

- human-controlled;
- reviewer-oriented;
- evidence-centric;
- research-aligned;
- non-autonomous;
- non-production.
