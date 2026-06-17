# LEO Institutional Approval Review Workflow Overview v1.0

## Status

PUBLIC MVP DEMONSTRATION — REVIEW READY

---

# Purpose

This document explains the operational workflow of the public MVP slice:

```text
institutional_approval_review
```

The goal of this document is to help external users understand:

- how the workflow operates;
- what the system generates;
- where human review occurs;
- what the evidence layer means;
- how the export package works;
- where the zero-autonomy boundary exists.

This document is written for:

- researchers;
- reviewers;
- civic-tech contributors;
- institutional observers;
- governance tooling developers;
- non-programmers interested in the workflow.

---

# Core Workflow

The Institutional Approval Review demo follows this workflow:

```text
INPUT
→ INPUT QUALITY VALIDATION
→ ANALYSIS
→ EVIDENCE GENERATION
→ HUMAN REVIEW
→ EXPORT PACKAGE
→ RELOAD REVIEW STATE
```

This workflow is local-first and human-controlled.

---

# Workflow Philosophy

The workflow is designed around one central principle:

```text
LEO generates evidence and reviewer guidance.
Humans remain responsible for interpretation and decisions.
```

The workflow intentionally avoids autonomous institutional authority.

---

# Stage 1 — Input

The workflow begins with structured local input data.

Example input categories:

- approval requests;
- approval chains;
- approval statuses;
- reviewer roles;
- escalation metadata;
- institutional workflow states.

The input layer is intentionally structured and reproducible.

---

# Input Directory

Typical input location:

```text
input/
```

The public MVP uses local demonstration datasets.

The datasets are intended to be:

- synthetic;
- safe for publication;
- reproducible;
- understandable.

---

# Stage 2 — Input Quality Validation

The first executable stage is:

```text
institutional_approval_input_quality_report.py
```

Purpose:

- verify structural integrity of input data;
- detect missing required fields;
- detect malformed workflow states;
- identify data quality issues.

Expected output:

```text
institutional_approval_input_quality_report.json
```

This stage improves reviewer trust in the dataset before analysis begins.

---

# Why Input Validation Matters

LEO intentionally separates:

```text
bad_input_data
!=
evidence
```

The system attempts to expose input quality problems before generating review findings.

This is part of the evidence-centric design philosophy.

---

# Stage 3 — Analysis

The next stage is:

```text
institutional_approval_review_pipeline.py
```

Purpose:

- analyze approval workflow structure;
- identify review-oriented signals;
- generate findings;
- generate evidence objects;
- generate reviewer guidance.

The pipeline is analytical only.

It does not execute institutional actions.

---

# Typical Review Signals

Example signal categories include:

- missing required approvals;
- unresolved rejection followed by approval;
- execution-ready request with pending review;
- missing legal review;
- undocumented emergency override;
- missing decision owner;
- undocumented escalation path.

These signals are intended to support reviewers.

They are NOT legal conclusions.

---

# Stage 4 — Evidence Generation

The pipeline generates:

```text
institutional_approval_evidence_report.json
```

The evidence report contains:

- findings;
- evidence objects;
- workflow metadata;
- severity levels;
- reviewer questions;
- suggested review-oriented next actions.

The report is structured for human inspection.

---

# Findings

A finding represents:

```text
A review-oriented signal requiring human attention.
```

A finding is NOT:

```text
A legal verdict
```

and NOT:

```text
An autonomous institutional decision
```

---

# Severity Levels

Example severity levels:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

Severity helps reviewers prioritize attention.

Severity does not create autonomous enforcement.

---

# Evidence Objects

Each finding may reference one or more evidence objects.

Evidence objects may include:

- workflow context;
- related approvals;
- related escalation states;
- linked reviewer questions;
- supporting metadata.

The goal is traceability.

---

# Reviewer Questions

The workflow intentionally generates reviewer-oriented questions.

Example:

```text
Why was the request marked execution-ready before all required approvals were completed?
```

These questions help structure human review.

---

# Stage 5 — Evidence Validation

The validation stage is:

```text
institutional_approval_evidence_report_validator.py
```

Purpose:

- verify report structure;
- verify workflow consistency;
- verify evidence linkage;
- verify safety boundary assumptions.

This stage improves workflow integrity and reproducibility.

---

# Validation Philosophy

The validator exists because:

```text
Generated output
!=
trusted output automatically
```

The workflow intentionally separates:

- generation;
- validation;
- review.

---

# Stage 6 — Human Review

Human review occurs in:

```text
leo_institutional_approval_dashboard.html
```

The dashboard is a local reviewer interface.

The dashboard allows a reviewer to:

- inspect findings;
- inspect evidence;
- prioritize severe signals;
- record review actions;
- add reviewer notes;
- export review state.

---

# Human Review Actions

Example review actions:

```text
ESCALATE_FOR_REVIEW
ACCEPT_AS_JUSTIFIED
MARK_FALSE_POSITIVE
REQUEST_MORE_EVIDENCE
DEFER_REVIEW
```

These actions are classifications only.

They do not trigger autonomous institutional execution.

---

# Reviewer Accountability

The reviewer remains responsible for:

- interpretation;
- escalation;
- institutional judgment;
- follow-up decisions;
- accountability.

This boundary is intentional.

---

# Stage 7 — Export Package

The dashboard can export:

```text
institutional_approval_human_review_package.json
```

The export package preserves:

- reviewed findings;
- reviewer actions;
- reviewer notes;
- evidence linkage;
- follow-up state;
- review metadata.

The export package is a local workflow artifact.

---

# Export Package Philosophy

The export package exists to support:

- review continuity;
- auditability;
- reviewer traceability;
- reproducible workflow state.

The export package is NOT:

- a legal decision;
- an enforcement order;
- a production governance artifact.

---

# Stage 8 — Reload Review State

The dashboard can reload the exported package.

This allows:

- restoration of review state;
- preservation of reviewer workflow;
- continuation of local review sessions.

This functionality demonstrates round-trip workflow persistence.

---

# Full Public MVP Workflow

The complete public workflow is:

```text
INPUT
→ INPUT QUALITY VALIDATION
→ ANALYSIS
→ EVIDENCE GENERATION
→ EVIDENCE VALIDATION
→ HUMAN REVIEW
→ EXPORT PACKAGE
→ RELOAD REVIEW STATE
```

This workflow is the core public MVP identity of the LEO project.

---

# Zero-Autonomy Boundary

The workflow preserves the following invariant:

```text
EVIDENCE_GENERATION
!=
AUTONOMOUS_AUTHORITY
```

and:

```text
HUMAN_REVIEW
!=
AUTONOMOUS_ENFORCEMENT
```

The workflow intentionally avoids autonomous institutional control.

---

# Current Validated Baseline

Current validated baseline:

```text
Dashboard v0.2 manually validated
Review package round-trip validated
Combined runtime baseline: 2451 passed in 56.87s
```

---

# Current Limitations

Current limitations include:

- research/pilot status;
- local-first execution only;
- no production integrations;
- no institutional deployment support;
- evolving architecture;
- limited cross-domain integration.

These limitations are intentional.

---

# Recommended Public Use

Recommended use cases:

- governance tooling research;
- reviewer workflow experimentation;
- auditability research;
- evidence-review workflow studies;
- transparency infrastructure research;
- local-first civic-tech exploration.

---

# Not Recommended Use

This workflow is NOT intended for:

- autonomous governance;
- legal automation;
- production institutional control;
- automated punishment systems;
- replacing human review structures.

---

# Design Philosophy

LEO attempts to structure uncertainty into:

- evidence;
- reviewer questions;
- traceable review actions;
- reproducible workflow state.

Humans remain accountable.

---

# Boundary Declaration

This workflow preserves the following invariant:

```text
PUBLIC_WORKFLOW_DEMONSTRATION
!=
AUTONOMOUS_GOVERNMENT_PLATFORM
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
