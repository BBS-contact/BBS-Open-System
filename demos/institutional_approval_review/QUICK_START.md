# LEO Institutional Approval Review Quick Start v1.0

## Status

PUBLIC MVP QUICK START DOCUMENT — WORK-IN-PROGRESS

---

# Purpose

This document provides the executable Quick Start workflow for the public MVP slice:

```text
institutional_approval_review
```

The goal is to allow an external user to:

1. clone the repository;
2. run the demo locally;
3. generate evidence reports;
4. open the dashboard;
5. review findings;
6. export a review package;
7. reload review state.

This onboarding flow is intentionally:

- local-first;
- reproducible;
- transparent;
- human-controlled;
- non-production.

---

# What This Demo Demonstrates

This demo demonstrates the workflow:

```text
INPUT
→ INPUT QUALITY VALIDATION
→ ANALYSIS
→ EVIDENCE REPORT
→ HUMAN REVIEW
→ EXPORT PACKAGE
→ RELOAD REVIEW STATE
```

The workflow is intended for reviewer support and evidence inspection.

The workflow does NOT create autonomous institutional decisions.

---

# Environment Requirements

The public MVP currently assumes:

- Python 3.11+ installed;
- Git installed;
- local filesystem access;
- terminal access;
- browser access.

Cloud infrastructure is NOT required.

---

# Recommended Environment

Recommended operating systems:

- Windows
- Linux
- macOS

Recommended environment:

```text
Local developer workstation
```

The public MVP is intentionally local-first.

---

# Step 1 — Clone Repository

Example:

```bash
git clone https://github.com/BBS-contact/BBS-Open-System.git
```

Enter the repository:

```bash
cd BBS-Open-System
```

---

# Step 2 — Navigate To Demo Directory

Navigate to:

```bash
cd demos/institutional_approval_review
```

Expected structure:

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

# Step 3 — Run Input Quality Validation

Run:

```bash
python institutional_approval_input_quality_report.py
```

Expected output:

```text
output/institutional_approval_input_quality_report.json
```

Purpose:

- validate input structure;
- identify missing fields;
- identify malformed workflow states;
- verify dataset readiness.

---

# Step 4 — Run Review Pipeline

Run:

```bash
python institutional_approval_review_pipeline.py
```

Expected output:

```text
output/institutional_approval_evidence_report.json
```

The pipeline generates:

- findings;
- evidence objects;
- severity levels;
- reviewer questions;
- review-oriented recommendations.

The pipeline does NOT create institutional decisions.

---

# Step 5 — Validate Evidence Report

Run:

```bash
python institutional_approval_evidence_report_validator.py
```

Expected result:

```text
Validation successful
```

Purpose:

- verify report integrity;
- verify evidence linkage;
- verify workflow structure;
- verify safety assumptions.

---

# Step 6 — Open Dashboard

Open in a browser:

```text
leo_institutional_approval_dashboard.html
```

The dashboard is a:

- reviewer interface;
- workflow visualization layer;
- evidence navigation tool;
- local review environment.

The dashboard is NOT:

- an autonomous control system;
- an institutional authority engine;
- an enforcement interface.

---

# Step 7 — Load Evidence Report

Inside the dashboard:

1. Load:

```text
output/institutional_approval_evidence_report.json
```

2. Review findings;
3. Inspect severity levels;
4. Select a finding;
5. Inspect evidence;
6. Review reviewer questions.

---

# Step 8 — Record Human Review

Example review actions:

```text
ESCALATE_FOR_REVIEW
ACCEPT_AS_JUSTIFIED
MARK_FALSE_POSITIVE
REQUEST_MORE_EVIDENCE
DEFER_REVIEW
```

Recommended workflow:

1. Select finding;
2. Choose review action;
3. Add reviewer ID;
4. Add reviewer note;
5. Save review record.

Review actions are classifications only.

They do not trigger autonomous institutional action.

---

# Step 9 — Export Review Package

Use the dashboard export functionality.

Expected output:

```text
output/institutional_approval_human_review_package.json
```

The package preserves:

- review actions;
- reviewer notes;
- reviewed findings;
- evidence linkage;
- follow-up state;
- review metadata.

The export package is a local workflow artifact.

---

# Step 10 — Reload Review Package

Reload the exported package into the dashboard.

Expected result:

- review state restored;
- reviewed findings visible;
- reviewer notes restored;
- workflow continuity preserved.

This confirms round-trip workflow persistence.

---

# Example Full Workflow

Complete public MVP workflow:

```text
INPUT
→ INPUT QUALITY VALIDATION
→ ANALYSIS
→ EVIDENCE REPORT
→ DASHBOARD REVIEW
→ HUMAN REVIEW
→ EXPORT PACKAGE
→ RELOAD REVIEW STATE
```

This workflow is the practical public MVP identity of LEO.

---

# Expected Public MVP Outputs

Expected generated outputs:

```text
output/institutional_approval_input_quality_report.json
output/institutional_approval_evidence_report.json
output/institutional_approval_human_review_package.json
```

These outputs are intended to remain local and reproducible.

---

# Running Tests

Run isolated tests:

```bash
python -m pytest tests/test_institutional_approval_input_quality_report.py
python -m pytest tests/test_institutional_approval_review_pipeline.py
python -m pytest tests/test_institutional_approval_evidence_report_validator.py
python -m pytest tests/test_institutional_approval_human_review_package.py
```

Combined runtime validation used during development:

```bash
python -m pytest tests demos/institutional_approval_review/tests
```

Validated baseline:

```text
2451 passed in 56.87s
```

---

# Current Validated MVP State

Current validated state:

```text
Dashboard v0.2 manually validated
Review package round-trip validated
Combined runtime baseline validated
```

---

# Troubleshooting

## Dashboard Does Not Load

Possible causes:

- invalid JSON structure;
- missing output files;
- browser local file restrictions;
- incomplete pipeline execution.

Recommended actions:

1. re-run validator;
2. verify output files exist;
3. refresh browser fully;
4. re-run pipeline.

---

## Evidence Report Missing

Verify:

```bash
python institutional_approval_review_pipeline.py
```

completed successfully.

Expected file:

```text
output/institutional_approval_evidence_report.json
```

---

## Review Package Missing

Verify:
- a review action was saved;
- export button was used;
- browser download was successful.

Expected file:

```text
output/institutional_approval_human_review_package.json
```

---

# Safety Notes

This demo is:

- research-oriented;
- reviewer-controlled;
- evidence-centric;
- local-first;
- non-production.

This demo is NOT:

- production governance software;
- autonomous enforcement software;
- legal authority software;
- institutional replacement infrastructure.

---

# Human Accountability Principle

LEO generates:

- evidence;
- findings;
- reviewer questions;
- workflow state.

Humans remain responsible for:

- interpretation;
- escalation;
- institutional decisions;
- governance accountability.

---

# Zero-Autonomy Boundary

This Quick Start preserves the following invariants:

```text
EVIDENCE_GENERATION
!=
AUTONOMOUS_AUTHORITY
```

```text
HUMAN_REVIEW
!=
AUTONOMOUS_ENFORCEMENT
```

```text
PUBLIC_MVP
!=
PRODUCTION_GOVERNMENT_SYSTEM
```

---

# Boundary Declaration

The Institutional Approval Review public MVP remains:

- human-controlled;
- reviewer-oriented;
- evidence-centric;
- research-aligned;
- local-first;
- non-autonomous;
- non-production;
- pilot-oriented.
