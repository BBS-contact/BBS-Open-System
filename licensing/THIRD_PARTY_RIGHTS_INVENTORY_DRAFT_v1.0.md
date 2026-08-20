# LEO Third-Party Rights Inventory Draft v1.0

DOCUMENT STATUS:

DRAFT FOR HUMAN REVIEW

DOCUMENT TYPE:

THIRD-PARTY RIGHTS, LICENSING, PROVENANCE, AND PUBLICATION-RISK INVENTORY

REPOSITORY:

BBS-Open-System-publication-working

STRATEGIC TRACK:

LEO PUBLIC VISIBILITY & PUBLIC EVALUATION READINESS

VERSION:

1.0

DATE:

2026-08-20

REVIEW AUTHORITY:

HUMAN REVIEW REQUIRED

AUTONOMOUS RIGHTS DETERMINATION:

NOT AUTHORIZED

AUTONOMOUS RELICENSING:

NOT AUTHORIZED

PRODUCTION MUTATION:

NOT AUTHORIZED

GITHUB PUSH:

NOT AUTHORIZED BY THIS DOCUMENT

---

## 1. Purpose

This document establishes the initial controlled inventory of third-party
rights, dependency licensing, externally attributable materials, unresolved
rights questions, and provenance requirements relevant to the public
evaluation repository:

`BBS-Open-System-publication-working`

The inventory is intended to support:

- public evaluation readiness;
- artifact-level licensing review;
- third-party rights separation;
- provenance preservation;
- evidence lineage;
- publication-risk identification;
- human licensing review;
- future controlled correction planning.

This document does not attempt to force all repository artifacts into one
licensing regime.

It does not assume that the presence of an artifact in the repository proves
ownership.

It does not assume that the absence of an explicit third-party notice proves
that no third-party rights exist.

It does not infer rights from technical dependency alone.

It does not infer ownership from Git authorship alone.

It does not infer reuse rights from public visibility alone.

Its purpose is to record what is known, what is supported by repository
evidence, what remains unresolved, and what must receive human review before
publication or licensing conclusions are made.

---

## 2. Relationship to the Artifact-to-License Mapping

This inventory is a controlled follow-up artifact to:

`licensing/ARTIFACT_TO_LICENSE_MAPPING_REVIEW_v1.0.md`

and:

`licensing/ARTIFACT_TO_LICENSE_MAPPING_DRAFT_v1.0.md`

The artifact-to-license mapping established that the repository should not be
treated as if one universal licence automatically governs all artifact
classes.

The recommended architecture is:

`LAYERED_ARTIFACT_LEVEL_LICENSING`

with:

`HISTORICAL_RIGHTS_PRESERVATION`

and:

`THIRD_PARTY_RIGHTS_SEPARATION`

under:

`HUMAN_REVIEW_REQUIRED`

This inventory develops the third-party-rights component of that architecture.

It does not replace the artifact-to-license mapping.

It does not amend the mapping automatically.

Where this inventory discovers uncertainty, that uncertainty must remain
explicit until reviewed.

---

## 3. Inventory Scope

The initial inventory covers third-party-rights questions associated with:

1. runtime dependencies;
2. Python dependencies;
3. testing dependencies;
4. development tooling;
5. web and user-interface dependencies;
6. external libraries;
7. external frameworks;
8. external packages;
9. third-party notices;
10. licence notices;
11. screenshots;
12. visual evidence;
13. fonts;
14. logos;
15. trademarks;
16. externally sourced graphics;
17. externally sourced data;
18. generated artifacts containing potentially external material;
19. demonstration outputs;
20. archived or historical dependency evidence;
21. historical licensing representations;
22. repository metadata that may contain rights-related statements;
23. unresolved ownership or reuse questions;
24. publication artifacts whose rights status cannot be established solely
    from repository presence.

The inventory is evidence-driven.

A category being listed here does not imply that third-party material was
found in that category.

---

## 4. Out of Scope

This document does not:

- provide legal advice;
- determine copyright ownership as a matter of law;
- determine infringement;
- determine trademark infringement;
- determine patent rights;
- determine database rights;
- determine moral rights;
- determine contractual rights outside available evidence;
- establish exclusive ownership;
- establish institutional licensing authority;
- grant a licence;
- revoke a licence;
- transfer rights;
- terminate rights;
- replace professional legal review;
- automatically modify repository files;
- automatically generate attribution notices;
- automatically relicense dependencies;
- automatically classify uncertain artifacts as Foundation-owned;
- automatically classify uncertain artifacts as Author-owned;
- automatically classify uncertain artifacts as third-party-owned;
- authorize publication;
- authorize production deployment;
- authorize a GitHub push.

---

## 5. Governing Principles

The inventory follows the following control principles.

### 5.1 Evidence Before Conclusion

A rights classification must be supported by identifiable evidence.

Repository presence alone is insufficient.

Filename alone is insufficient.

Git authorship alone is insufficient.

A dependency import alone may establish technical use but does not, by itself,
establish the complete applicable rights framework.

---

### 5.2 Provenance Before Reuse

Where an artifact may contain third-party material, provenance should be
identified before a reuse classification is treated as resolved.

The relevant provenance may include:

- source repository;
- package registry;
- upstream project;
- licence file;
- copyright notice;
- attribution notice;
- commit history;
- generation process;
- source asset;
- external dataset;
- external service;
- human contributor;
- contractual source.

---

### 5.3 Uncertainty Must Remain Visible

Unknown rights are not equivalent to unrestricted rights.

Unknown provenance is not equivalent to third-party provenance.

Absence of a notice is not equivalent to absence of rights.

Absence of a detected third-party component is not equivalent to a legal
finding that no third-party rights exist.

The inventory therefore preserves unresolved states explicitly.

---

### 5.4 Historical Rights Must Be Preserved

Historical licence grants, notices, repository declarations, and rights
statements must not be silently erased from the evidence model.

Where a historical licence is superseded as current repository policy, its
historical evidentiary role remains relevant.

Historical evidence and current prospective licensing architecture must be
distinguished.

---

### 5.5 Human Review Is Mandatory

No unresolved third-party rights record may be converted automatically into a
final licensing conclusion.

No automated process may:

- declare ownership;
- declare infringement;
- grant permission;
- revoke permission;
- relicense an artifact;
- suppress historical licence evidence;
- determine that professional legal review is unnecessary.

Human review remains the governing control.

---

## 6. Rights-State Model

Each inventory record should use an explicit rights state.

The initial rights-state vocabulary is:

`RESOLVED_FOR_CURRENT_SCOPE`

`PARTIALLY_RESOLVED`

`UNRESOLVED`

`NOT_APPLICABLE`

`NOT_OBSERVED`

`REQUIRES_PROFESSIONAL_LEGAL_REVIEW`

These states have distinct meanings.

---

### 6.1 RESOLVED_FOR_CURRENT_SCOPE

Use when the evidence available for the current publication scope is
sufficient to establish the operational rights treatment required by this
inventory.

This state does not necessarily mean that every conceivable legal question is
resolved.

---

### 6.2 PARTIALLY_RESOLVED

Use when some relevant facts are established but one or more material rights
questions remain open.

Example:

- upstream package identified;
- licence identified;
- exact version or bundled notice status unresolved.

---

### 6.3 UNRESOLVED

Use when the available evidence does not establish a reliable rights
classification.

This state must not be converted into a permissive default.

---

### 6.4 NOT_APPLICABLE

Use when a third-party-rights classification is not applicable to the
particular artifact or category under review.

The basis for this state should still be recorded.

---

### 6.5 NOT_OBSERVED

Use when the review did not observe evidence of the relevant third-party
material.

This is an evidentiary state.

It is not equivalent to:

`DOES_NOT_EXIST`

and must not be represented as a legal conclusion.

---

### 6.6 REQUIRES_PROFESSIONAL_LEGAL_REVIEW

Use when repository evidence is insufficient and the remaining question
requires legal interpretation beyond an architectural or technical review.

---

## 7. Provenance-State Model

Third-party rights and provenance must remain separate dimensions.

The initial provenance states are:

`VERIFIED`

`PARTIALLY_VERIFIED`

`NOT_ESTABLISHED`

`NOT_APPLICABLE`

`CONFLICTING`

A rights record must not be marked resolved merely because repository
provenance is known.

For example:

a Git commit can establish when an asset entered the repository while leaving
the original creator, copyright owner, source material, and reuse permission
unresolved.

---

## 8. Evidence Confidence Model

Inventory conclusions should distinguish evidence strength.

The initial evidence-confidence levels are:

`HIGH`

`MEDIUM`

`LOW`

`INSUFFICIENT`

### HIGH

Direct repository or upstream evidence establishes the relevant fact with
little material ambiguity.

Examples may include:

- an applicable upstream licence file;
- package metadata tied to an identified dependency and version;
- a direct copyright notice;
- an explicit attribution record;
- a cryptographically matched archived artifact.

### MEDIUM

Multiple consistent indicators support the classification, but one or more
material details remain incomplete.

### LOW

The classification is based on indirect evidence and requires confirmation.

### INSUFFICIENT

The available evidence does not support a reliable classification.

Confidence is evidence confidence.

It is not legal certainty.

---

## 9. Required Inventory Fields

Where applicable, each material inventory record should capture:

`RECORD_ID`

`ARTIFACT_OR_COMPONENT`

`ARTIFACT_CLASS`

`REPOSITORY_LOCATION`

`TECHNICAL_ROLE`

`THIRD_PARTY_INDICATOR`

`UPSTREAM_OR_SOURCE`

`VERSION`

`COPYRIGHT_HOLDER`

`LICENCE_OR_RIGHTS_BASIS`

`LICENCE_EVIDENCE_LOCATION`

`NOTICE_REQUIREMENT`

`NOTICE_PRESENT`

`ATTRIBUTION_REQUIREMENT`

`ATTRIBUTION_PRESENT`

`REPOSITORY_PROVENANCE`

`ORIGINAL_PROVENANCE`

`RIGHTS_STATE`

`EVIDENCE_CONFIDENCE`

`PUBLICATION_RELEVANCE`

`PUBLIC_REUSE_STATUS`

`HUMAN_REVIEW_REQUIRED`

`PROFESSIONAL_LEGAL_REVIEW_REQUIRED`

`EVIDENCE_REFERENCES`

`NOTES`

Fields that cannot be established must remain explicitly unresolved.

They must not be populated through assumption.

---

## 10. Classification Boundary: Technical Use vs Rights

The inventory distinguishes:

`TECHNICAL_DEPENDENCY`

from:

`RIGHTS_CLASSIFICATION`

and from:

`PUBLICATION_PERMISSION`

A package may be technically required by tests without being distributed as
part of a runtime artifact.

A library may appear in generated output without being embedded in a
redistributable form.

A screenshot may visually contain third-party material even though the image
file itself was generated within a LEO workflow.

A public webpage may reference external assets without those assets being
owned by LEO or Fundacja BBS.

Therefore:

`TECHNICAL_USE != OWNERSHIP`

`REPOSITORY_PRESENCE != OWNERSHIP`

`PUBLIC_VISIBILITY != REUSE_PERMISSION`

`GIT_AUTHORSHIP != COPYRIGHT_OWNERSHIP`

`DEPENDENCY_REFERENCE != AUTOMATIC_REDISTRIBUTION_RIGHT`

---

## 11. Evidence Discovery Baseline

The initial evidence discovery established several important classes of
third-party-rights evidence.

These include:

1. dependency-related repository evidence;
2. test-tooling evidence;
3. historical licensing and notice evidence;
4. screenshot provenance evidence;
5. public-evaluation visual evidence;
6. unresolved external-content questions.

The evidence discovery phase was read-only.

No third-party licence was modified.

No dependency was relicensed.

No screenshot was deleted.

No attribution was added automatically.

No historical rights statement was removed.

---

## 12. Repository Dependency Rights Inventory

### 12.1 Purpose

This section records the third-party-rights status of software dependencies
identified within the current controlled publication repository scope.

The purpose is not to infer ownership or publication permission from technical
use.

The purpose is to distinguish:

`RUNTIME_DEPENDENCY`

from:

`TEST_DEPENDENCY`

from:

`DEVELOPMENT_TOOLING`

from:

`REDISTRIBUTED_THIRD_PARTY_COMPONENT`

and from:

`UNRESOLVED_RIGHTS_QUESTION`.

The review is limited to evidence available for:

`BBS-Open-System-publication-working`

at the reviewed repository state.

Absence of a dependency declaration or import is treated as an evidentiary
finding only.

It is not treated as proof that no third-party software is relevant to the
broader LEO development history.

---

### 12.2 Dependency Manifest Review

The tracked repository surface was reviewed for common dependency and package
manifest formats, including:

- `requirements*.txt`;
- `pyproject.toml`;
- `setup.py`;
- `setup.cfg`;
- `Pipfile`;
- `Pipfile.lock`;
- `poetry.lock`;
- `uv.lock`;
- `package.json`;
- `package-lock.json`;
- `yarn.lock`;
- `pnpm-lock.yaml`;
- `Cargo.toml`;
- `Cargo.lock`;
- `go.mod`;
- `go.sum`.

No tracked dependency or package manifest matching the reviewed set was
observed.

This finding is recorded as:

`DEPENDENCY_MANIFESTS: NOT_OBSERVED`

with:

`EVIDENCE_CONFIDENCE: HIGH`

for the reviewed tracked repository surface.

This finding does not establish that no dependencies were used during
development.

It establishes only that the reviewed publication repository does not presently
declare them through the examined tracked manifest classes.

---

### 12.3 Python Runtime Import Surface

The tracked Python surface contained eight Python files at the time of review.

The runtime and demonstration modules reviewed used Python standard-library
imports including:

- `__future__`;
- `json`;
- `csv`;
- `copy`;
- `dataclasses`;
- `datetime`;
- `pathlib`;
- `typing`.

No directly imported third-party Python runtime package was observed in the
reviewed runtime and demonstration modules.

The current evidentiary classification is therefore:

`DIRECT_THIRD_PARTY_RUNTIME_PYTHON_IMPORT: NOT_OBSERVED`

with:

`RIGHTS_STATE: NOT_OBSERVED`

`PROVENANCE_STATE: NOT_APPLICABLE`

`EVIDENCE_CONFIDENCE: HIGH`

for the reviewed import surface.

This classification must not be represented as:

`NO_THIRD_PARTY_RUNTIME_DEPENDENCIES_EXIST`.

The review establishes only what was directly observable in the tracked Python
import surface.

---

### 12.4 Test Dependency: pytest

The tracked test modules reviewed contain direct imports of:

`pytest`

The observed use is associated with the test surface rather than the reviewed
runtime modules.

The technical classification is:

`TEST_DEPENDENCY`

The third-party indicator is:

`CONFIRMED_BY_DIRECT_IMPORT`

The current record is:

**RECORD_ID:** `TPR-DEP-001`

**ARTIFACT_OR_COMPONENT:** `pytest`

**ARTIFACT_CLASS:** `TEST_TOOLING_DEPENDENCY`

**REPOSITORY_LOCATION:** tracked Python test modules

**TECHNICAL_ROLE:** test execution and test support

**THIRD_PARTY_INDICATOR:** direct `import pytest` statements

**UPSTREAM_OR_SOURCE:** pytest project; exact upstream package record not
established by the current repository evidence

**VERSION:** `UNRESOLVED`

**COPYRIGHT_HOLDER:** `UNRESOLVED_FROM_CURRENT_REPOSITORY_EVIDENCE`

**LICENCE_OR_RIGHTS_BASIS:** `UNRESOLVED_FROM_CURRENT_REPOSITORY_EVIDENCE`

**LICENCE_EVIDENCE_LOCATION:** no package-specific upstream licence record was
established within the reviewed publication repository

**NOTICE_REQUIREMENT:** `UNRESOLVED`

**NOTICE_PRESENT:** no pytest-specific notice was identified during the current
repository review

**ATTRIBUTION_REQUIREMENT:** `UNRESOLVED`

**ATTRIBUTION_PRESENT:** no pytest-specific attribution record was established
during the current repository review

**REPOSITORY_PROVENANCE:** `VERIFIED` for direct technical use through tracked
test imports

**ORIGINAL_PROVENANCE:** `PARTIALLY_VERIFIED`; package identity is established,
but exact version and corresponding upstream rights record have not yet been
tied to repository evidence

**RIGHTS_STATE:** `PARTIALLY_RESOLVED`

**EVIDENCE_CONFIDENCE:** `HIGH` for technical use; `INSUFFICIENT` for exact
version-specific rights treatment

**PUBLICATION_RELEVANCE:** `MEDIUM`

**PUBLIC_REUSE_STATUS:** `UNRESOLVED_FOR_REDISTRIBUTION`; no evidence currently
establishes that pytest itself is redistributed as repository source or binary
content

**HUMAN_REVIEW_REQUIRED:** `YES`

**PROFESSIONAL_LEGAL_REVIEW_REQUIRED:** `NOT_ESTABLISHED_AT_CURRENT_STAGE`

**EVIDENCE_REFERENCES:** tracked test imports and artifact-to-license mapping
evidence

**NOTES:** technical use of pytest must remain distinct from redistribution of
pytest. The current repository evidence establishes test use but does not, by
itself, establish that pytest code or binary artifacts are included in the
publication repository.

---

### 12.5 Runtime Dependency Finding

The current controlled review therefore distinguishes two different findings:

`THIRD_PARTY_TEST_TOOLING_OBSERVED`

and:

`DIRECT_THIRD_PARTY_RUNTIME_PYTHON_IMPORT_NOT_OBSERVED`

These findings must not be collapsed into either of the following statements:

`THE_REPOSITORY_HAS_NO_THIRD_PARTY_DEPENDENCIES`

or:

`PYTEST_IS_DISTRIBUTED_WITH_THE_RUNTIME`.

Neither statement is established by the current evidence.

---

### 12.6 Dependency Publication Treatment

For the current public-evaluation scope, the dependency review does not
establish a blocker to publication of the reviewed LEO-authored runtime source
solely because pytest is used by tests.

However, before a final dependency-rights record is treated as complete, the
following should remain visible:

1. exact pytest version is not established from a tracked dependency manifest;
2. corresponding upstream licence evidence is not currently tied to a specific
   version in this repository;
3. notice and attribution requirements have not yet been normalized into this
   inventory;
4. technical test use must not be represented as ownership of pytest;
5. absence of bundled pytest code should be distinguished from absence of pytest
   as development/test tooling.

For the current Commission-facing evaluation objective, these are controlled
rights-review items rather than evidence that the LEO method itself cannot be
presented.

---

## 13. Development and Test Tooling Rights Inventory

### 13.1 Purpose

Development tooling is treated separately from runtime redistribution.

A tool used to create, test, inspect, render, capture, or package a LEO artifact
does not automatically become part of the rights regime governing the LEO
artifact.

The relevant distinctions are:

`TOOL_USED_TO_CREATE_ARTIFACT`

`TOOL_OUTPUT_INCLUDED_IN_ARTIFACT`

`TOOL_COMPONENT_REDISTRIBUTED`

`TOOL_NOTICE_REPRODUCED`

`TOOL_RIGHTS_NOT_RELEVANT_TO_CURRENT_PUBLICATION_SCOPE`

These states must not be conflated.

---

### 13.2 Python Tooling

Python-generated execution and error output appears within parts of the
demonstration evidence surface.

The current repository review does not establish that the Python interpreter
itself is redistributed as part of the public repository.

Accordingly:

**ARTIFACT_CLASS:** `DEVELOPMENT_OR_EXECUTION_TOOLING`

**TECHNICAL_ROLE:** runtime execution and development environment

**THIRD_PARTY_INDICATOR:** external software environment

**REDISTRIBUTED_COMPONENT:** `NOT_OBSERVED`

**RIGHTS_STATE:** `PARTIALLY_RESOLVED`

**PUBLICATION_RELEVANCE:** dependent on whether software-generated output is
reproduced in a public artifact

**HUMAN_REVIEW_REQUIRED:** `YES` where tool-generated output is included in
demonstration material

This treatment does not make a legal determination regarding individual
software-generated messages.

---

### 13.3 pytest Tooling

`pytest` is recorded in Section 12 as a directly observed test dependency.

Its use is classified as:

`TEST_TOOLING`

rather than:

`OBSERVED_RUNTIME_COMPONENT`.

No separate duplicate rights record is required here.

The cross-reference is:

`TPR-DEP-001`.

---

### 13.4 Microsoft Windows PowerShell

Microsoft Windows PowerShell is observable within the demonstration PDF
evidence surface.

The reviewed technical runtime log material includes an explicit Windows
PowerShell identification and Microsoft copyright notice.

This establishes a positive third-party indicator.

The current record is:

**RECORD_ID:** `TPR-TOOL-001`

**ARTIFACT_OR_COMPONENT:** Microsoft Windows PowerShell textual material

**ARTIFACT_CLASS:** `EXTERNAL_SOFTWARE_GENERATED_OR_IDENTIFYING_CONTENT`

**REPOSITORY_LOCATION:**
`demonstration/LEO_Technical_Runtime_Logs.pdf`

**TECHNICAL_ROLE:** development/runtime shell environment represented in
technical demonstration evidence

**THIRD_PARTY_INDICATOR:** explicit Microsoft/Windows PowerShell identification
and copyright notice within the PDF content

**UPSTREAM_OR_SOURCE:** Microsoft Windows PowerShell environment

**VERSION:** `UNRESOLVED_FROM_CURRENT_EVIDENCE`

**COPYRIGHT_HOLDER:** Microsoft Corporation is explicitly identified in the
reproduced notice

**LICENCE_OR_RIGHTS_BASIS:** `UNRESOLVED_FOR_REPRODUCED_OUTPUT`

**LICENCE_EVIDENCE_LOCATION:** no dedicated Microsoft/PowerShell rights record
was identified within the reviewed repository licensing files

**NOTICE_REQUIREMENT:** `UNRESOLVED`

**NOTICE_PRESENT:** `YES`, as part of the captured/reproduced shell output

**ATTRIBUTION_REQUIREMENT:** `UNRESOLVED`

**ATTRIBUTION_PRESENT:** Microsoft is identified by the reproduced notice

**REPOSITORY_PROVENANCE:** `VERIFIED`; the containing PDF is tracked and its Git
introduction history has been reviewed

**ORIGINAL_PROVENANCE:** `PARTIALLY_VERIFIED`; the external software environment
is identifiable, while the complete rights basis for reproducing the captured
text has not been established by repository evidence

**RIGHTS_STATE:** `PARTIALLY_RESOLVED`

**EVIDENCE_CONFIDENCE:** `HIGH` for presence of Microsoft-attributable material;
`INSUFFICIENT` for a final redistribution-rights conclusion

**PUBLICATION_RELEVANCE:** `HIGH` because the material appears inside a tracked
public demonstration artifact

**PUBLIC_REUSE_STATUS:** `UNRESOLVED_FOR_CURRENT_SCOPE`

**HUMAN_REVIEW_REQUIRED:** `YES`

**PROFESSIONAL_LEGAL_REVIEW_REQUIRED:** `UNRESOLVED`; escalation should depend
on whether this PDF remains within the intended Commission-facing publication
surface

**NOTES:** this record does not characterize ordinary use of PowerShell as a
rights problem. The relevant issue is the reproduction of identifiable
third-party textual material inside a publication artifact.

---

### 13.5 Microsoft Word as PDF Generation Tool

The reviewed demonstration PDFs contain technical evidence consistent with
Microsoft Word having been used in their document-generation process.

Use of Microsoft Word as an authoring or PDF-generation tool must remain
separate from the rights status of the authored document content.

The current classification is:

`EXTERNAL_AUTHORING_TOOL`

No evidence reviewed establishes that Microsoft Word software itself is
redistributed in the repository.

Accordingly:

**RECORD_ID:** `TPR-TOOL-002`

**ARTIFACT_OR_COMPONENT:** Microsoft Word generation metadata/tooling

**ARTIFACT_CLASS:** `DOCUMENT_GENERATION_TOOL`

**TECHNICAL_ROLE:** PDF/document generation

**THIRD_PARTY_INDICATOR:** document technical metadata

**REDISTRIBUTED_COMPONENT:** `NOT_OBSERVED`

**RIGHTS_STATE:** `NOT_APPLICABLE` to redistribution of the Microsoft Word
software itself within the current repository scope

**PUBLICATION_RELEVANCE:** `LOW`, except where generation metadata or embedded
third-party resources create separate rights questions

**HUMAN_REVIEW_REQUIRED:** `NO` for tool use alone

**NOTES:** embedded font resources are a separate rights surface and are not
resolved by this classification.

---

### 13.6 Tooling Boundary

The current tooling inventory establishes the following boundary:

`USE_OF_EXTERNAL_TOOL != REDISTRIBUTION_OF_EXTERNAL_TOOL`

but:

`EXTERNAL_TOOL_OUTPUT_INSIDE_PUBLIC_ARTIFACT`

may create a distinct publication-rights question.

This distinction is particularly relevant to technical demonstration material.

For Commission-facing evaluation, technical authenticity should be preserved,
but raw development-environment output should not be included merely because it
exists historically.

Its inclusion should serve an identifiable evaluation purpose.

---

## 14. Web, UI, and Referenced Asset Rights Inventory

### 14.1 Reviewed Web Surface

The tracked repository contains nineteen HTML files within the reviewed
publication surface.

The review examined external-resource and embedded-resource indicators,
including:

- external HTTP and HTTPS references;
- protocol-relative references;
- `<script>` elements;
- `<link>` elements;
- `<img>` elements;
- CSS `@import`;
- font-family declarations;
- Google Fonts indicators;
- common CDN indicators;
- jsDelivr;
- unpkg;
- Bootstrap;
- jQuery;
- Font Awesome.

No directly observed CDN-hosted JavaScript library, externally loaded web font,
Bootstrap dependency, jQuery dependency, Font Awesome dependency, jsDelivr
dependency, unpkg dependency, or comparable third-party web library was
identified in the reviewed HTML surface.

The current classification is:

`DIRECT_EXTERNAL_WEB_LIBRARY_DEPENDENCY: NOT_OBSERVED`

with:

`EVIDENCE_CONFIDENCE: HIGH`

for the reviewed tracked HTML surface.

---

### 14.2 External Navigation Links

External `https://` links observed in the public landing material include links
to BBS-controlled or BBS-related GitHub repositories and GitHub Pages
destinations.

The reviewed evidence identifies these as navigation references rather than
resource-loading dependencies.

A hyperlink to an external platform does not establish redistribution of that
platform's software.

Accordingly, these links are not classified as embedded third-party software
dependencies.

This does not make a separate trademark or platform-policy determination.

---

### 14.3 System and Fallback Font References

HTML/CSS content contains font-family declarations referencing names including:

- `system-ui`;
- `Segoe UI`;
- `Roboto`;
- `Arial`;
- `Noto Sans`;
- `Consolas`.

No tracked `.woff`, `.woff2`, `.ttf`, `.otf`, or other reviewed font-file class
was observed in the repository artifact inventory.

No reviewed HTML evidence established remote Google Fonts or comparable
web-font loading.

The current classification is therefore:

`FONT_NAME_REFERENCE_WITHOUT_OBSERVED_FONT_FILE_REDISTRIBUTION`

A CSS font-family reference must not be treated as equivalent to redistribution
of a font program.

The current rights state for HTML font references is:

`NOT_APPLICABLE`

to bundled font-file redistribution within the reviewed web surface.

This classification does not apply automatically to fonts embedded inside PDF
files.

PDF font embedding is treated separately in Section 16.

---

### 14.4 Referenced but Absent CSS Asset

The reviewed legal HTML surface references:

`assets/css/main.css`

The controlled repository check established:

`FILESYSTEM_EXISTS: FALSE`

`TRACKED: NO`

`IGNORED: NO MATCH`

No related tracked `main.css` path was identified.

The current record is:

**RECORD_ID:** `TPR-WEB-001`

**ARTIFACT_OR_COMPONENT:** `assets/css/main.css`

**ARTIFACT_CLASS:** `REFERENCED_BUT_ABSENT_WEB_ASSET`

**REPOSITORY_LOCATION:** referenced from tracked HTML; asset itself absent

**TECHNICAL_ROLE:** stylesheet reference

**THIRD_PARTY_INDICATOR:** `NOT_ESTABLISHED`

**UPSTREAM_OR_SOURCE:** `NOT_ESTABLISHED`

**VERSION:** `NOT_APPLICABLE`

**COPYRIGHT_HOLDER:** `NOT_ESTABLISHED`

**LICENCE_OR_RIGHTS_BASIS:** `NOT_ESTABLISHED`

**REPOSITORY_PROVENANCE:** reference is observable; referenced asset is not
present

**ORIGINAL_PROVENANCE:** `NOT_ESTABLISHED`

**RIGHTS_STATE:** `UNRESOLVED`

**EVIDENCE_CONFIDENCE:** `HIGH` for absence from the reviewed repository;
`INSUFFICIENT` for rights classification

**PUBLICATION_RELEVANCE:** `MEDIUM`

**PUBLIC_REUSE_STATUS:** `NOT_ASSESSABLE_FROM_CURRENT_REPOSITORY`

**HUMAN_REVIEW_REQUIRED:** `YES`

**PROFESSIONAL_LEGAL_REVIEW_REQUIRED:** `NO` at the current stage

**NOTES:** this is primarily a publication-integrity and provenance issue. The
asset must not be classified as Foundation-owned, Author-owned, or third-party
solely from its HTML reference.

---

### 14.5 Referenced but Absent Favicon

The reviewed prototype HTML surface references:

`img/favicon.ico`

The controlled repository check established:

`FILESYSTEM_EXISTS: FALSE`

`TRACKED: NO`

`IGNORED: NO MATCH`

No related tracked favicon path was identified.

The current record is:

**RECORD_ID:** `TPR-WEB-002`

**ARTIFACT_OR_COMPONENT:** `img/favicon.ico`

**ARTIFACT_CLASS:** `REFERENCED_BUT_ABSENT_WEB_ASSET`

**TECHNICAL_ROLE:** favicon / user-interface identity asset

**THIRD_PARTY_INDICATOR:** `NOT_ESTABLISHED`

**UPSTREAM_OR_SOURCE:** `NOT_ESTABLISHED`

**COPYRIGHT_HOLDER:** `NOT_ESTABLISHED`

**LICENCE_OR_RIGHTS_BASIS:** `NOT_ESTABLISHED`

**REPOSITORY_PROVENANCE:** reference verified; referenced asset absent

**ORIGINAL_PROVENANCE:** `NOT_ESTABLISHED`

**RIGHTS_STATE:** `UNRESOLVED`

**EVIDENCE_CONFIDENCE:** `HIGH` for repository absence; `INSUFFICIENT` for
rights classification

**PUBLICATION_RELEVANCE:** `MEDIUM`

**PUBLIC_REUSE_STATUS:** `NOT_ASSESSABLE_FROM_CURRENT_REPOSITORY`

**HUMAN_REVIEW_REQUIRED:** `YES`

**PROFESSIONAL_LEGAL_REVIEW_REQUIRED:** `NO` at the current stage

**NOTES:** no assumption should be made about the visual identity, ownership, or
source of an asset that is not present in the reviewed repository.

---

### 14.6 Inline Script Surface

Tracked HTML contains inline script blocks.

The existence of inline JavaScript does not, by itself, establish third-party
provenance.

No identifiable external JavaScript library was established through the
reviewed resource-reference scan.

The current classification is therefore:

`INLINE_SCRIPT_PRESENT`

with:

`THIRD_PARTY_PROVENANCE: NOT_ESTABLISHED_FROM_REFERENCE_SCAN`

This finding should not be converted automatically into:

`FIRST_PARTY_SCRIPT_CONFIRMED`

or:

`THIRD_PARTY_SCRIPT_CONFIRMED`.

Where inline scripts form part of a Commission-facing evaluator path, their
functional behavior may be reviewed separately as implementation evidence.

A separate rights escalation is not required solely because inline JavaScript
exists.

---

### 14.7 Web Surface Publication Finding

For the reviewed HTML surface:

- common external web libraries were not observed;
- remote web-font loading was not observed;
- bundled font files were not observed;
- system/fallback font references are present;
- two referenced local assets are absent from the repository;
- inline scripts are present but were not identified as external libraries;
- external navigation links do not constitute observed dependency
  redistribution.

The two missing local assets should be treated as publication-integrity issues
before a polished evaluator-facing web surface is relied upon.

They do not currently establish a third-party-rights violation.

---

## 15. Screenshot and Visual Evidence Rights Inventory

### 15.1 Reviewed Screenshot Set

Seven tracked PNG files were reviewed:

1. `screenshots/institutional_approval_review/dashboard_overview.png`
2. `screenshots/institutional_approval_review/export_package_preview.png`
3. `screenshots/institutional_approval_review/human_review_form.png`
4. `screenshots/institutional_approval_review/review_record_state.png`
5. `screenshots/institutional_approval_review/selected_finding_review.png`
6. `screenshots/institutional_approval_review/top_priority_findings.png`
7. `screenshots/institutional_approval_review/zero_autonomy_boundary.png`

These screenshots form a coherent visual evidence set associated with the
Institutional Approval Review demonstration.

---

### 15.2 Repository Introduction Provenance

All seven PNG files were introduced into the repository through the same
reviewed Git commit:

`79a60efa6ea8fbac947efd5355d990ba9f722674`

with repository date:

`2026-05-16T21:44:46+02:00`

and Git author record:

`bbs.contact <bbs.contactproton.me@proton.me>`

The commit subject was:

`Add files via upload`

No later add/modify commit was observed for the reviewed files during the
controlled history inspection.

This establishes:

`COMMON_REPOSITORY_INTRODUCTION_PROVENANCE: VERIFIED`

It does not establish:

`COMMON_COPYRIGHT_AUTHORSHIP: VERIFIED`.

Git introduction and copyright authorship remain separate facts.

---

### 15.3 Content Integrity Hashes

The reviewed current SHA-256 values were:

`dashboard_overview.png`

`701D80947C6EEA90E1CA888EC4373D3387D7B8E98A06B630E00B7B233CEF1E43`

`export_package_preview.png`

`368990595261115529C1DFC49D23B8459E8735954BBFCF865A02D698AAEB759E`

`human_review_form.png`

`B5EBD77BC479DB9BE811647EDE262383410C81D4FEE0DDC58DFACBE05391963B`

`review_record_state.png`

`6665F030E1AE50A3C62C9F0F0EF84786B4C114F20BD1A5FAEBF63EB7100D1FB3`

`selected_finding_review.png`

`5105A5B5CDE1BD2EA589ED16BD3A21BCB2837CCE73B5140B23E2262BCDA51B98`

`top_priority_findings.png`

`64FE5ABDC7DDBE08C8EF8DAC4595ECD4CF698A68940F8537B29D7ECA5C8D8777`

`zero_autonomy_boundary.png`

`BC05AB99A42AED2E34FF4ED74152EBAF4B39BC8706EE983CF92DD3FB45A66D17`

These hashes establish content identity for the reviewed files.

They do not establish ownership.

---

### 15.4 Embedded Metadata Review

All seven PNG files exposed the same reviewed `System.Drawing` property-item
profile.

No readable embedded metadata identifying:

- author;
- copyright holder;
- creator;
- software;
- source URL;
- external asset provider;

was established from that metadata inspection.

The common metadata profile is consistent with a common generation or capture
workflow.

It is not sufficient to establish common authorship.

The provenance classification therefore remains:

`REPOSITORY_PROVENANCE: VERIFIED`

`ORIGINAL_PROVENANCE: PARTIALLY_VERIFIED`

rather than:

`ORIGINAL_PROVENANCE: VERIFIED`.

---

### 15.5 Visual Content Review

A direct visual review of all seven screenshots was performed.

The reviewed images depict a consistent:

`LEO Institutional Approval Review`

demonstration interface and related review/evidence states.

The visual review did not observe identifiable:

- third-party logos;
- externally branded user interfaces;
- stock photography;
- external illustrations;
- third-party promotional imagery;
- recognizable external application chrome;
- browser branding;
- operating-system desktop chrome;
- externally attributed artwork;
- embedded third-party websites;
- identifiable third-party visual marks requiring an immediate attribution
  conclusion.

The screenshots contain generic browser-rendered interface elements and text
rendering.

Those elements do not, by themselves, establish redistribution of the browser,
operating system, or font software.

The evidence finding is:

`NO_OBSERVED_THIRD_PARTY_VISUAL_CONTENT`

This is an evidentiary classification.

It must not be represented as:

`NO_THIRD_PARTY_RIGHTS_EXIST`.

---

### 15.6 Screenshot Inventory Record

The seven screenshots may be represented as one controlled rights record
because they share repository introduction history, demonstration context, and
reviewed visual characteristics.

**RECORD_ID:** `TPR-VIS-001`

**ARTIFACT_OR_COMPONENT:** Institutional Approval Review screenshot set

**ARTIFACT_CLASS:** `PUBLIC_EVALUATION_VISUAL_EVIDENCE`

**REPOSITORY_LOCATION:**
`screenshots/institutional_approval_review/`

**TECHNICAL_ROLE:** visual demonstration and evaluator evidence

**THIRD_PARTY_INDICATOR:** no identifiable third-party visual material observed
during direct visual review

**UPSTREAM_OR_SOURCE:** associated LEO Institutional Approval Review
demonstration; original capture workflow not independently documented to a
fully verified level

**VERSION:** `NOT_APPLICABLE`

**COPYRIGHT_HOLDER:** `NOT_ESTABLISHED_BY_CURRENT_EVIDENCE`

**LICENCE_OR_RIGHTS_BASIS:** governed by the applicable repository artifact
rights architecture subject to unresolved original-authorship evidence

**LICENCE_EVIDENCE_LOCATION:** artifact-to-license mapping and current
third-party-rights inventory

**NOTICE_REQUIREMENT:** no screenshot-specific third-party notice requirement
was identified from the reviewed visual content

**NOTICE_PRESENT:** `NOT_APPLICABLE` for observed third-party visual content

**ATTRIBUTION_REQUIREMENT:** no third-party attribution requirement was
identified from the reviewed visual content

**ATTRIBUTION_PRESENT:** `NOT_APPLICABLE` for observed third-party visual
content

**REPOSITORY_PROVENANCE:** `VERIFIED`

**ORIGINAL_PROVENANCE:** `PARTIALLY_VERIFIED`

**RIGHTS_STATE:** `PARTIALLY_RESOLVED`

**EVIDENCE_CONFIDENCE:** `HIGH` for repository provenance and visual-content
review; `INSUFFICIENT` for independent copyright-ownership determination

**PUBLICATION_RELEVANCE:** `HIGH`

**PUBLIC_REUSE_STATUS:** `REVIEW_REQUIRED_BEFORE_BROAD_REUSE`

**HUMAN_REVIEW_REQUIRED:** `YES`

**PROFESSIONAL_LEGAL_REVIEW_REQUIRED:** `NO` based solely on the currently
observed visual content; this may change if a broader ownership question becomes
material

**EVIDENCE_REFERENCES:** Git introduction history, SHA-256 review, PNG metadata
review, direct visual inspection

**NOTES:** the screenshot set is potentially strong Commission-facing evidence
because it demonstrates human review, evidence handling, review-record state,
export packaging, and the zero-autonomy boundary. Its evaluation value should
remain distinct from a legal ownership determination.

---

### 15.7 Commission-Facing Relevance of the Screenshot Set

The screenshot set has high evaluator relevance because it demonstrates
practical system behavior rather than architecture claims alone.

In particular, the reviewed images provide visual evidence of:

- structured findings;
- selected-finding review;
- human-review controls;
- review-record persistence/state;
- evidence/export packaging;
- prioritization;
- explicit zero-autonomy boundaries.

For the current public-evaluation objective, the screenshots should therefore
not be excluded merely because independent copyright ownership has not been
proven through Git metadata.

Instead, their publication treatment should remain subject to controlled human
review under the artifact-level licensing model.

---

## 16. Demonstration PDF Rights Inventory

### 16.1 Reviewed PDF Set

Two tracked PDF artifacts were reviewed:

1. `demonstration/LEO_Architecture_Overview.pdf`
2. `demonstration/LEO_Technical_Runtime_Logs.pdf`

Both were introduced through the same reviewed Git commit:

`7e0a7c41a12ae994ee7de80e2f39c92e3d0306b8`

with repository date:

`2026-03-10T19:37:10+01:00`

and Git author record:

`bbs.contact <bbs.contactproton.me@proton.me>`

with commit subject:

`Add files via upload`.

This establishes common repository introduction provenance.

It does not establish identical content provenance or rights treatment.

The two PDFs therefore require separate records.

---

### 16.2 Current PDF Integrity Identifiers

The reviewed current file identifiers were:

`demonstration/LEO_Architecture_Overview.pdf`

Size:

`184962 bytes`

SHA-256:

`7085773F1C6B3600CCC2EA156CDBBDB4AAD7181D0C79E025B1F9DFFBB337E152`

and:

`demonstration/LEO_Technical_Runtime_Logs.pdf`

Size:

`424430 bytes`

SHA-256:

`67079A8132503E654A1AEA8695747F14F4F9BF3834B302B00603E139852F4300`

These values identify the artifacts reviewed for this inventory.

---

### 16.3 LEO Architecture Overview

The content-level review of:

`demonstration/LEO_Architecture_Overview.pdf`

identified the document as an LEO architecture overview associated with the
author and Fundacja BBS.

No identifiable third-party:

- logo;
- photograph;
- screenshot;
- stock illustration;
- externally attributed artwork;

was observed in the reviewed visible document content.

The content-level evidence therefore supports:

`THIRD_PARTY_TEXT_OR_VISUAL_CONTENT: NOT_OBSERVED`

for the substantive reviewed architecture content.

This does not resolve embedded technical resources.

---

### 16.4 Embedded Fonts in Architecture Overview

The reviewed PDF contains embedded or subset font resources including font
families identified as:

- `Calibri`;
- `Calibri Bold`;
- `Arial`;
- `Symbol`.

These font resources constitute a separate third-party-rights surface from the
authored architecture text.

The current repository licensing evidence does not establish a complete
font-specific redistribution or embedding-rights record for these resources.

The current record is:

**RECORD_ID:** `TPR-PDF-001`

**ARTIFACT_OR_COMPONENT:** `LEO_Architecture_Overview.pdf`

**ARTIFACT_CLASS:** `DEMONSTRATION_PDF`

**REPOSITORY_LOCATION:**
`demonstration/LEO_Architecture_Overview.pdf`

**TECHNICAL_ROLE:** architecture explanation / public demonstration material

**THIRD_PARTY_INDICATOR:** embedded/subset font resources observed

**UPSTREAM_OR_SOURCE:** document-generation environment and font resources;
complete upstream rights chain not established from repository evidence

**VERSION:** `NOT_APPLICABLE` to the document; font versions unresolved

**COPYRIGHT_HOLDER:** LEO-authored document framing/content is identified in the
document; font-resource copyright ownership is not established by this
inventory

**LICENCE_OR_RIGHTS_BASIS:** `PARTIALLY_ESTABLISHED`; document rights treatment
and embedded font-resource treatment remain distinct

**LICENCE_EVIDENCE_LOCATION:** repository licensing architecture; no dedicated
font-rights record identified

**NOTICE_REQUIREMENT:** `UNRESOLVED_FOR_EMBEDDED_FONTS`

**NOTICE_PRESENT:** no dedicated font notice was established in the reviewed
repository evidence

**ATTRIBUTION_REQUIREMENT:** `UNRESOLVED_FOR_EMBEDDED_FONTS`

**ATTRIBUTION_PRESENT:** no dedicated font attribution record established

**REPOSITORY_PROVENANCE:** `VERIFIED`

**ORIGINAL_PROVENANCE:** `PARTIALLY_VERIFIED`

**RIGHTS_STATE:** `PARTIALLY_RESOLVED`

**EVIDENCE_CONFIDENCE:** `HIGH` for artifact identity and presence of embedded
font resources; `INSUFFICIENT` for final font redistribution-rights treatment

**PUBLICATION_RELEVANCE:** `MEDIUM_TO_HIGH`

**PUBLIC_REUSE_STATUS:** `HUMAN_REVIEW_REQUIRED`

**HUMAN_REVIEW_REQUIRED:** `YES`

**PROFESSIONAL_LEGAL_REVIEW_REQUIRED:** `UNRESOLVED`; required only if the PDF
is retained in a publication scope where font embedding rights cannot be
resolved operationally

**EVIDENCE_REFERENCES:** Git provenance, SHA-256 identification, PDF content
review, PDF technical-resource review

**NOTES:** no observed third-party visual material was identified in the
substantive architecture content. The unresolved rights surface is primarily
technical resource embedding rather than the architecture narrative itself.

---

### 16.5 LEO Technical Runtime Logs

The content-level review of:

`demonstration/LEO_Technical_Runtime_Logs.pdf`

identified a materially different third-party-rights surface.

The document contains LEO-authored framing and technical demonstration
material.

It also reproduces external software-generated or externally attributable
textual material.

Observed material includes explicit:

`Windows PowerShell`

identification and:

`Copyright (C) Microsoft Corporation. All rights reserved.`

within the captured technical environment.

The document also contains Python and PowerShell-generated execution,
traceback, diagnostic, and error output.

The inventory does not make a legal determination regarding the copyright
status of each generated diagnostic or error string.

However, such content must not be represented as wholly LEO-authored prose.

The correct evidentiary classification is:

`EXTERNAL_SOFTWARE_GENERATED_OR_ATTRIBUTABLE_TEXT_PRESENT`.

---

### 16.6 Embedded Fonts in Technical Runtime Logs

The reviewed technical runtime log PDF contains embedded/subset font resources
including identified families and variants associated with:

- `Calibri`;
- `Arial`;
- `Symbol`;
- `Segoe UI Symbol`;
- `Consolas`.

The current repository evidence does not establish a complete version-specific
font-rights record for those embedded resources.

As with the Architecture Overview PDF, font embedding is treated separately
from the authored document narrative.

---

### 16.7 Technical Runtime Logs Inventory Record

**RECORD_ID:** `TPR-PDF-002`

**ARTIFACT_OR_COMPONENT:** `LEO_Technical_Runtime_Logs.pdf`

**ARTIFACT_CLASS:** `DEMONSTRATION_PDF_WITH_EXTERNAL_SOFTWARE_OUTPUT`

**REPOSITORY_LOCATION:**
`demonstration/LEO_Technical_Runtime_Logs.pdf`

**TECHNICAL_ROLE:** historical technical demonstration / runtime evidence

**THIRD_PARTY_INDICATOR:** explicit Microsoft PowerShell notice; external
software-generated diagnostic/runtime text; embedded font resources

**UPSTREAM_OR_SOURCE:** LEO demonstration context plus external development and
runtime tooling

**VERSION:** document version not independently established; external tool/font
versions unresolved

**COPYRIGHT_HOLDER:** mixed or component-specific; must not be represented as a
single fully LEO-owned content surface based solely on repository presence

**LICENCE_OR_RIGHTS_BASIS:** `UNRESOLVED_FOR_EXTERNAL_COMPONENTS`

**LICENCE_EVIDENCE_LOCATION:** no dedicated PowerShell/Microsoft/font rights
record was identified within the reviewed repository licensing evidence

**NOTICE_REQUIREMENT:** `UNRESOLVED`

**NOTICE_PRESENT:** Microsoft copyright notice is visibly reproduced within the
artifact

**ATTRIBUTION_REQUIREMENT:** `UNRESOLVED`

**ATTRIBUTION_PRESENT:** Microsoft is identified by the reproduced PowerShell
notice

**REPOSITORY_PROVENANCE:** `VERIFIED`

**ORIGINAL_PROVENANCE:** `PARTIALLY_VERIFIED`

**RIGHTS_STATE:** `PARTIALLY_RESOLVED`

**EVIDENCE_CONFIDENCE:** `HIGH` for the presence of identifiable third-party
material; `INSUFFICIENT` for final redistribution-rights treatment

**PUBLICATION_RELEVANCE:** `MEDIUM`

**PUBLIC_REUSE_STATUS:** `REQUIRES_HUMAN_REVIEW_BEFORE_REPUBLICATION`

**HUMAN_REVIEW_REQUIRED:** `YES`

**PROFESSIONAL_LEGAL_REVIEW_REQUIRED:** `UNRESOLVED`; should depend on whether
this historical raw-runtime artifact is materially necessary to the intended
Commission-facing evaluation package

**EVIDENCE_REFERENCES:** Git provenance, SHA-256 identification, PDF
content-level review, external software notice observation, embedded font
review

**NOTES:** this artifact provides historical technical evidence, but its
Commission-facing value should be assessed against cleaner and more current
runtime/test evidence available elsewhere in the LEO evaluation architecture.
The existence of this historical PDF does not require it to remain a primary
evaluator-facing artifact.

---

### 16.8 PDF Publication Boundary

The two PDFs must not receive identical publication treatment merely because
they share a repository introduction commit.

The current evidence supports the distinction:

`LEO_Architecture_Overview.pdf`

→ substantive third-party textual/visual content not observed;

→ embedded third-party font-resource rights remain unresolved;

whereas:

`LEO_Technical_Runtime_Logs.pdf`

→ identifiable external software-generated/attributable textual material is
present;

→ explicit Microsoft PowerShell notice is present;

→ embedded third-party font-resource rights remain unresolved.

Accordingly, the Technical Runtime Logs PDF carries a higher third-party-rights
and publication-review burden.

For the current Commission-facing update, historical artifacts should not be
retained as primary evidence merely because they already exist publicly.

Where current, cleaner, reproducible runtime evidence exists, evaluator-facing
material should prefer that evidence, subject to the controlled publication
selection process.

This is a publication-readiness recommendation.

It is not an instruction to delete, suppress, rewrite, or remove either
historical PDF.

No such mutation is authorized by this inventory.

---

## 17. Historical Licensing, Notices, and Rights Representations Inventory

### 17.1 Purpose

Historical licensing and rights evidence must remain visible because current
publication decisions must not erase or overwrite prior repository
representations.

The inventory therefore distinguishes:

`HISTORICAL_RIGHTS_EVIDENCE`

from:

`CURRENT_PUBLICATION_POLICY`

and from:

`PROSPECTIVE_ARTIFACT_LEVEL_LICENSING`.

A historical licence, notice, repository statement, or publication declaration
may remain relevant as evidence even where the current publication architecture
is being revised.

Historical evidence must not be silently normalized into a new rights model.

---

### 17.2 Current Licensing Evidence Surface

The reviewed publication repository contains tracked licensing and rights
artifacts including:

- root `LICENSE`;
- `licensing/LICENSE`;
- `licensing/NOTICE`;
- `licensing/BBS_INSTITUTIONAL_LICENSE_v1.0.md`;
- `licensing/CORE_RUNTIME_PROPRIETARY_NOTICE_v1.0.md`;
- `licensing/LICENSE_STRATEGY_v1.0.md`;
- `licensing/LEO_IP_AND_LICENSING_MODEL_v1.0.md`;
- `licensing/ARTIFACT_TO_LICENSE_MAPPING_REVIEW_v1.0.md`;
- `licensing/ARTIFACT_TO_LICENSE_MAPPING_DRAFT_v1.0.md`.

These artifacts do not automatically establish that every repository artifact
shares one identical rights treatment.

Their significance is contextual and artifact-specific.

---

### 17.3 Root and Licensing-Directory Licence Separation

The repository contains both:

`LICENSE`

and:

`licensing/LICENSE`.

The presence of multiple licence locations is itself a rights-architecture
indicator.

The inventory does not assume:

`ROOT_LICENSE == UNIVERSAL_ARTIFACT_RIGHTS`

or:

`LICENSING_DIRECTORY_LICENSE == UNIVERSAL_ARTIFACT_RIGHTS`.

The existing artifact-to-license review established that the repository must
be treated through:

`LAYERED_ARTIFACT_LEVEL_LICENSING`

rather than a single automatic licence assignment.

This inventory adopts that architecture.

---

### 17.4 Historical Rights Preservation Record

**RECORD_ID:** `TPR-HIST-001`

**ARTIFACT_OR_COMPONENT:** existing licence and rights-history surface

**ARTIFACT_CLASS:** `HISTORICAL_AND_CURRENT_RIGHTS_EVIDENCE`

**REPOSITORY_LOCATION:** root and `licensing/`

**TECHNICAL_ROLE:** licensing, rights representation, institutional publication
control, historical evidence

**THIRD_PARTY_INDICATOR:** not inherently third-party; relevant to rights
classification and preservation

**UPSTREAM_OR_SOURCE:** repository history and institutional licensing records

**VERSION:** mixed

**COPYRIGHT_HOLDER:** artifact-specific; not inferred universally

**LICENCE_OR_RIGHTS_BASIS:** artifact-specific and historical-context dependent

**LICENCE_EVIDENCE_LOCATION:** tracked licence, notice, strategy, mapping, and
IP/licensing files

**NOTICE_REQUIREMENT:** artifact-specific

**NOTICE_PRESENT:** multiple repository-level and licensing-level notices exist

**ATTRIBUTION_REQUIREMENT:** artifact-specific

**ATTRIBUTION_PRESENT:** not universally established

**REPOSITORY_PROVENANCE:** `VERIFIED`

**ORIGINAL_PROVENANCE:** varies by artifact

**RIGHTS_STATE:** `PARTIALLY_RESOLVED`

**EVIDENCE_CONFIDENCE:** `HIGH` for repository presence and historical
representations; variable for their application to individual artifacts

**PUBLICATION_RELEVANCE:** `HIGH`

**PUBLIC_REUSE_STATUS:** must be derived at artifact level

**HUMAN_REVIEW_REQUIRED:** `YES`

**PROFESSIONAL_LEGAL_REVIEW_REQUIRED:** only where conflicting or materially
ambiguous rights representations remain relevant to intended publication

**EVIDENCE_REFERENCES:** tracked licensing artifacts and artifact-to-license
mapping review

**NOTES:** current licensing cleanup must not destroy historical rights evidence
or imply retroactive rights changes unsupported by evidence.

---

### 17.5 NOTICE Treatment

The tracked repository contains:

`licensing/NOTICE`

This confirms that a notice mechanism exists within the current publication
repository.

However, the existence of a general NOTICE file does not establish that:

- every third-party component requiring notice is listed;
- every historical attribution requirement is satisfied;
- every external software-generated artifact is covered;
- every embedded font resource is covered;
- every future publication artifact is automatically covered.

The current classification is therefore:

`GENERAL_NOTICE_PRESENT`

with:

`THIRD_PARTY_NOTICE_COMPLETENESS: NOT_ESTABLISHED`.

---

### 17.6 Historical and Current Policy Boundary

The inventory adopts the following control rule:

`HISTORICAL_RIGHTS_EVIDENCE MUST BE PRESERVED`

while:

`CURRENT_PUBLICATION_POLICY MAY BE CLARIFIED PROSPECTIVELY`

subject to:

`HUMAN_REVIEW`.

No current publication cleanup may imply that historical licences never
existed.

No prospective rights model may silently rewrite the legal or evidentiary
history of already published artifacts.

---

## 18. External Data, Documentation, Standards, and Content Inventory

### 18.1 Purpose

This section records third-party-rights exposure associated with data,
documentation, standards, external text, and non-code content.

The relevant categories include:

- external datasets;
- imported CSV or JSON material;
- copied or adapted documentation;
- standards text;
- regulatory text;
- externally sourced reports;
- institutional records;
- generated output incorporating external content;
- externally attributable technical text.

The current review must distinguish between:

`OBSERVED_EXTERNAL_CONTENT`

and:

`EXTERNAL_CONTENT_NOT_OBSERVED`.

---

### 18.2 Tracked Data Surface

The reviewed publication repository contains tracked CSV and JSON artifacts,
including demo inputs, demo outputs, and system-report attachments.

Repository presence does not establish whether those data files are:

- synthetic;
- internally generated;
- externally sourced;
- transformed from third-party material;
- derived from real institutional records.

Accordingly, no blanket ownership classification is applied to all CSV/JSON
content.

The current baseline is:

`DATA_PROVENANCE_REQUIRES_ARTIFACT_CONTEXT`.

---

### 18.3 Institutional Approval Demo Data

The Institutional Approval Review demo contains tracked input CSV files and
generated JSON outputs.

The reviewed structure and demonstration context support the classification:

`CONTROLLED_DEMONSTRATION_DATA_SURFACE`

but do not, by repository presence alone, establish the complete original
provenance of every field or value.

The current record is:

**RECORD_ID:** `TPR-DATA-001`

**ARTIFACT_OR_COMPONENT:** Institutional Approval Review demo data set

**ARTIFACT_CLASS:** `DEMONSTRATION_DATA`

**REPOSITORY_LOCATION:** `demos/institutional_approval_review/input/` and
associated output paths

**TECHNICAL_ROLE:** demonstration input, evidence generation, human review, and
output validation

**THIRD_PARTY_INDICATOR:** no direct third-party source attribution observed in
the reviewed repository evidence

**UPSTREAM_OR_SOURCE:** controlled demo context; exact original data-generation
record not fully established through current inventory evidence

**VERSION:** repository-state dependent

**COPYRIGHT_HOLDER:** `NOT_ESTABLISHED_BY_CURRENT_EVIDENCE`

**LICENCE_OR_RIGHTS_BASIS:** `UNRESOLVED_AT_DATASET_LEVEL`

**NOTICE_REQUIREMENT:** no specific third-party notice requirement observed

**NOTICE_PRESENT:** `NOT_APPLICABLE` based on currently observed evidence

**ATTRIBUTION_REQUIREMENT:** no specific third-party attribution requirement
observed

**ATTRIBUTION_PRESENT:** `NOT_APPLICABLE` based on currently observed evidence

**REPOSITORY_PROVENANCE:** `VERIFIED`

**ORIGINAL_PROVENANCE:** `PARTIALLY_VERIFIED`

**RIGHTS_STATE:** `PARTIALLY_RESOLVED`

**EVIDENCE_CONFIDENCE:** `MEDIUM`

**PUBLICATION_RELEVANCE:** `HIGH`

**PUBLIC_REUSE_STATUS:** `HUMAN_REVIEW_REQUIRED`

**HUMAN_REVIEW_REQUIRED:** `YES`

**PROFESSIONAL_LEGAL_REVIEW_REQUIRED:** `NO` based solely on current evidence

**NOTES:** demonstration data should be described accurately as controlled
evaluation material unless stronger provenance documentation supports a more
specific claim.

---

### 18.4 System Audit Attachments

Tracked system-report attachments include CSV and JSON inventory artifacts
generated from repository or filesystem inspection.

These artifacts appear operationally derived from the LEO development
environment rather than externally licensed datasets.

The current evidentiary classification is:

`SYSTEM_GENERATED_INVENTORY_OUTPUT`

with:

`THIRD_PARTY_DATASET_INDICATOR: NOT_OBSERVED`.

This classification does not resolve possible third-party names, filenames, or
tool-originated text appearing incidentally within generated reports.

---

### 18.5 Standards and Regulatory Text

The reviewed inventory evidence does not establish that complete standards,
regulations, or externally copyrighted legal publications are redistributed as
tracked repository artifacts solely because legal, policy, governance, or
regulatory concepts are referenced.

References to legal or policy frameworks must remain distinct from copying
protected third-party publications.

The current state is:

`REDISTRIBUTED_EXTERNAL_STANDARDS_TEXT: NOT_OBSERVED`

for the reviewed evidence surface.

This is not a legal conclusion regarding every sentence in every document.

---

### 18.6 External Documentation and Copied Text

No evidence reviewed to this point establishes a repository-wide corpus of
copied third-party documentation.

Where external software-generated text has been positively observed, such as
PowerShell identification and diagnostic output inside the Technical Runtime
Logs PDF, it is recorded separately.

The current baseline is:

`GENERAL_EXTERNALLY_COPIED_DOCUMENTATION: NOT_OBSERVED`

with:

`EVIDENCE_CONFIDENCE: MEDIUM`.

This classification remains subject to revision if specific provenance evidence
is later identified.

---

### 18.7 Data and Content Publication Boundary

For Commission-facing publication:

- controlled demo inputs and outputs may be used where their demonstration
  status is accurately described;
- generated system inventory output may be used as operational evidence;
- externally sourced datasets must not be assumed absent merely because no
  current notice exists;
- any future imported real-world data should require explicit source and rights
  provenance;
- legal and standards references should be cited or linked where appropriate
  rather than reproduced unnecessarily.

The current inventory does not identify a data-rights blocker requiring the
Commission-facing methodology package to stop.

---

## 19. Repository Metadata, Attribution, and Citation Inventory

### 19.1 Purpose

Repository metadata can contain rights-relevant statements even when it is not
part of runtime execution.

The inventory therefore includes:

- `CITATION.cff`;
- repository author metadata;
- project attribution;
- institutional attribution;
- public copyright pages;
- repository notices;
- Git history;
- documentation citation statements.

Metadata is evidence.

It is not automatically proof of legal ownership.

---

### 19.2 CITATION.cff

The tracked repository contains:

`CITATION.cff`

This provides a formal citation surface for the repository.

The presence of citation metadata supports:

- author attribution;
- project identification;
- evaluator citation;
- research provenance;
- repository discoverability.

It does not, by itself, determine third-party rights for every included
artifact.

The current classification is:

`REPOSITORY_CITATION_METADATA_PRESENT`.

---

### 19.3 Git Author Metadata

Git history provides useful evidence regarding:

- repository introduction;
- modification history;
- commit chronology;
- recorded contributor identity.

Git authorship remains governed by the established boundary:

`GIT_AUTHORSHIP != COPYRIGHT_OWNERSHIP`.

Git history may support provenance.

It must not be used alone to declare exclusive copyright ownership.

---

### 19.4 Institutional Attribution

The public repository contains material identifying:

`Fundacja BBS – Better Balance System`

and:

`LEO`

as institutional/project context.

This attribution is relevant to public evaluation and repository identity.

It must remain separate from unsupported claims that Fundacja BBS owns every
historical artifact, third-party dependency, generated output, or embedded
resource.

---

### 19.5 Public Copyright and Legal Pages

Tracked legal HTML includes a public copyright page and additional policy/legal
pages.

These pages form part of the repository's public rights representation.

Their existence does not override artifact-level evidence.

The current classification is:

`PUBLIC_RIGHTS_REPRESENTATION_PRESENT`

with:

`ARTIFACT_LEVEL_APPLICATION_REQUIRES_REVIEW`.

---

### 19.6 Attribution Completeness

Current repository evidence does not establish a complete third-party
attribution register covering all possible:

- test tooling;
- embedded font resources;
- software-generated content;
- historical imported material;
- external references.

Accordingly:

`THIRD_PARTY_ATTRIBUTION_COMPLETENESS: NOT_ESTABLISHED`.

This is a publication-readiness gap.

It is not evidence of infringement.

---

## 20. Consolidated Third-Party Rights Register

### 20.1 Purpose

This section consolidates the material rights records identified during the
current controlled review.

The register is designed to support publication decisions.

It is not intended to replace the detailed evidence contained in prior
sections.

---

### 20.2 Consolidated Register

| Record ID | Artifact / Component | Class | Third-Party Indicator | Rights State | Provenance State | Evidence Confidence | Publication Relevance | Human Review |
|---|---|---|---|---|---|---|---|---|
| `TPR-DEP-001` | pytest | Test tooling dependency | Direct import confirmed | `PARTIALLY_RESOLVED` | `PARTIALLY_VERIFIED` | High for use / insufficient for exact rights | Medium | Yes |
| `TPR-TOOL-001` | Microsoft Windows PowerShell textual material | External software-generated/identifying content | Explicit Microsoft notice present | `PARTIALLY_RESOLVED` | `PARTIALLY_VERIFIED` | High for presence | High within affected PDF | Yes |
| `TPR-TOOL-002` | Microsoft Word generation tooling | Document generation tool | Tool metadata | `NOT_APPLICABLE` to software redistribution | `PARTIALLY_VERIFIED` | Medium | Low | No for tool use alone |
| `TPR-WEB-001` | `assets/css/main.css` | Referenced but absent web asset | Source not established | `UNRESOLVED` | `NOT_ESTABLISHED` | High for absence | Medium | Yes |
| `TPR-WEB-002` | `img/favicon.ico` | Referenced but absent web asset | Source not established | `UNRESOLVED` | `NOT_ESTABLISHED` | High for absence | Medium | Yes |
| `TPR-VIS-001` | Institutional Approval Review screenshot set | Public evaluation visual evidence | No third-party visual content observed | `PARTIALLY_RESOLVED` | `PARTIALLY_VERIFIED` | High for reviewed visual content | High | Yes |
| `TPR-PDF-001` | `LEO_Architecture_Overview.pdf` | Demonstration PDF | Embedded font resources | `PARTIALLY_RESOLVED` | `PARTIALLY_VERIFIED` | High for artifact/resource presence | Medium to High | Yes |
| `TPR-PDF-002` | `LEO_Technical_Runtime_Logs.pdf` | Demonstration PDF with external tool output | Microsoft notice, software-generated text, embedded fonts | `PARTIALLY_RESOLVED` | `PARTIALLY_VERIFIED` | High for third-party presence | Medium | Yes |
| `TPR-HIST-001` | Historical/current licensing surface | Rights evidence | Mixed | `PARTIALLY_RESOLVED` | Mixed | High for repository presence | High | Yes |
| `TPR-DATA-001` | Institutional Approval Review demo data | Demonstration data | No external source directly observed | `PARTIALLY_RESOLVED` | `PARTIALLY_VERIFIED` | Medium | High | Yes |

---

### 20.3 Register Interpretation

The consolidated register does not identify any component as:

`UNRESTRICTED`

solely because no adverse rights evidence was observed.

Likewise, the register does not identify any artifact as:

`UNAUTHORIZED`

solely because rights evidence remains incomplete.

The inventory preserves the difference between:

`NO_OBSERVED_THIRD_PARTY_CONTENT`

and:

`RIGHTS_FULLY_RESOLVED`.

These are not equivalent.

---

## 21. Unresolved Rights Register

### 21.1 Purpose

All unresolved material rights questions should be visible in one place.

This prevents uncertainty from being hidden inside long-form analysis.

The unresolved register is also intended to prevent unnecessary repeated
research.

If an unresolved item can be safely contained through publication scope or
human review, it does not automatically require further immediate
investigation.

---

### 21.2 UR-001 — pytest Version and Upstream Rights Record

**ISSUE:** exact pytest version is not established by a tracked dependency
manifest.

**KNOWN:** direct test use is confirmed.

**UNKNOWN:** exact version-specific upstream licence/notice record tied to this
repository state.

**CURRENT IMPACT:** low to medium.

**PUBLICATION TREATMENT:** test tooling may be identified explicitly; do not
represent pytest as a LEO-owned dependency.

**NEXT ACTION:** resolve only if dependency attribution becomes necessary for
the final publication package.

---

### 21.3 UR-002 — Missing `assets/css/main.css`

**ISSUE:** tracked legal HTML references a stylesheet absent from the reviewed
repository.

**KNOWN:** reference exists; target asset does not.

**UNKNOWN:** original source, ownership, current intended use.

**CURRENT IMPACT:** publication integrity and presentation quality.

**PUBLICATION TREATMENT:** do not infer rights; either resolve the reference
before relying on the affected public pages or exclude the broken dependency
from the evaluator path.

**NEXT ACTION:** controlled publication-repair decision after inventory
completion.

---

### 21.4 UR-003 — Missing `img/favicon.ico`

**ISSUE:** tracked prototype pages reference an absent favicon.

**KNOWN:** reference exists; file is absent.

**UNKNOWN:** source and original rights.

**CURRENT IMPACT:** low rights impact; medium publication-polish impact.

**PUBLICATION TREATMENT:** do not infer ownership or third-party status.

**NEXT ACTION:** controlled publication-repair decision after inventory
completion.

---

### 21.5 UR-004 — Screenshot Original Copyright Provenance

**ISSUE:** repository introduction and visual review are established, but
independent original copyright ownership is not proven.

**KNOWN:** common repository introduction; coherent LEO demo interface; no
third-party visual material observed.

**UNKNOWN:** independently documented original capture/authorship chain.

**CURRENT IMPACT:** low to medium.

**PUBLICATION TREATMENT:** human-reviewed use may remain appropriate for
evaluation material.

**NEXT ACTION:** no additional forensic review required unless broader reuse or
external licensing makes ownership material.

---

### 21.6 UR-005 — Embedded Font Rights in Demonstration PDFs

**ISSUE:** embedded/subset third-party font resources are present.

**KNOWN:** relevant font families are identifiable.

**UNKNOWN:** complete version-specific embedding/redistribution rights record
for the reviewed PDFs.

**CURRENT IMPACT:** medium for PDF republication.

**PUBLICATION TREATMENT:** prefer current evaluator material that avoids
unnecessary unresolved embedded-resource complexity where equivalent evidence
exists.

**NEXT ACTION:** human decision whether each PDF is necessary to the final
Commission-facing package.

---

### 21.7 UR-006 — PowerShell and External Software Output in Runtime Log PDF

**ISSUE:** the Technical Runtime Logs PDF reproduces externally attributable
software text.

**KNOWN:** explicit Microsoft notice and software-generated diagnostic text are
present.

**UNKNOWN:** complete rights basis for redistribution of the full historical
capture.

**CURRENT IMPACT:** medium.

**PUBLICATION TREATMENT:** do not use this historical PDF as primary evidence if
cleaner current runtime evidence is available.

**NEXT ACTION:** evaluator-package selection decision.

---

### 21.8 UR-007 — Attribution Completeness

**ISSUE:** repository-wide third-party attribution completeness is not
established.

**KNOWN:** a general NOTICE exists and some third-party material is observable.

**UNKNOWN:** whether all current or historical attribution requirements are
captured.

**CURRENT IMPACT:** medium.

**PUBLICATION TREATMENT:** final publication package should contain only
artifacts whose relevant third-party treatment is understood sufficiently for
the intended scope.

**NEXT ACTION:** package-level review rather than unlimited repository-wide
forensics.

---

### 21.9 UR-008 — Historical Rights Representations

**ISSUE:** historical and prospective rights models coexist.

**KNOWN:** multiple licensing and rights artifacts exist.

**UNKNOWN:** whether every historical publication state can be fully reconciled
with the current prospective model.

**CURRENT IMPACT:** medium to high if historical rights are overwritten or
misrepresented.

**PUBLICATION TREATMENT:** preserve historical evidence; apply current model
prospectively.

**NEXT ACTION:** no destructive normalization.

---

## 22. Publication-Risk Classification

### 22.1 Purpose

Publication risk is assessed operationally for the current controlled
Commission-facing evaluation objective.

Publication risk is not a legal verdict.

The initial categories are:

`LOW`

`MODERATE`

`HIGH`

`EXCLUDE_FROM_PRIMARY_EVALUATOR_PATH_PENDING_REVIEW`

---

### 22.2 LOW-RISK MATERIAL

Material may be treated as relatively low publication risk where:

- no third-party component is directly observed;
- provenance is sufficiently clear for the current evaluation scope;
- no conflicting rights representation is known;
- no unnecessary embedded external material is present;
- evaluator value is high.

Examples may include current LEO-authored methodology documentation subject to
artifact-level licensing review.

---

### 22.3 MODERATE-RISK MATERIAL

Material should be treated as moderate risk where:

- third-party tooling use is known;
- exact dependency version is unresolved;
- provenance is partial but usable;
- embedded resource questions remain;
- missing referenced assets affect presentation;
- publication is possible with controlled human review.

Examples include:

- test tooling references;
- screenshot evidence;
- Architecture Overview PDF with unresolved embedded font treatment;
- demo data with partial original provenance.

---

### 22.4 HIGH-RISK MATERIAL

Material should be treated as high publication risk where:

- third-party content is directly embedded;
- rights basis is unresolved;
- attribution requirements may be incomplete;
- historical rights representations conflict;
- provenance is materially uncertain;
- the artifact is not necessary to demonstrate the current method.

High risk does not mean unlawful.

It means the artifact should not be treated casually within the publication
package.

---

### 22.5 EXCLUDE_FROM_PRIMARY_EVALUATOR_PATH_PENDING_REVIEW

An artifact may remain publicly archived or historically preserved while being
excluded from the primary evaluator path.

This treatment is particularly appropriate where:

- historical value exists;
- current explanatory value is weak;
- cleaner current evidence exists;
- third-party or provenance complexity is disproportionate to evaluation value.

The current evidence supports treating:

`LEO_Technical_Runtime_Logs.pdf`

as a candidate for:

`EXCLUDE_FROM_PRIMARY_EVALUATOR_PATH_PENDING_REVIEW`

rather than as primary Commission-facing evidence.

This is not a deletion recommendation.

It is a publication-navigation recommendation.

---

## 23. Human Review Requirements

### 23.1 Human Review Authority

Human review remains mandatory for all material publication decisions arising
from this inventory.

No automated system may determine:

- final ownership;
- final public reuse permission;
- licence compatibility;
- removal of historical rights evidence;
- repository publication scope;
- legal sufficiency of attribution;
- necessity of professional legal review.

---

### 23.2 Required Human Decisions Before Commission-Facing Publication

The following decisions require explicit human review:

1. which artifacts form the primary Commission-facing evaluator path;
2. whether `LEO_Technical_Runtime_Logs.pdf` remains part of that path;
3. whether `LEO_Architecture_Overview.pdf` remains necessary;
4. whether screenshot evidence is retained as current evaluator evidence;
5. whether missing `main.css` and favicon references are repaired, replaced, or
   excluded from evaluator navigation;
6. whether current NOTICE treatment is sufficient for the selected publication
   subset;
7. whether pytest attribution should be normalized for the selected public test
   evidence;
8. whether any historical licensing statement conflicts with the prospective
   publication package;
9. whether any unresolved item materially blocks the selected publication
   subset.

---

### 23.3 Human Review Standard

Human review should ask:

`IS THIS ARTIFACT NECESSARY TO EXPLAIN OR DEMONSTRATE THE CURRENT LEO METHOD?`

If:

`NO`

and the artifact introduces avoidable unresolved rights or provenance
complexity, it should not be elevated into the primary evaluator path merely
because it already exists historically.

If:

`YES`

the remaining rights uncertainty should be reviewed proportionately to its
actual publication importance.

---

## 24. Professional Legal Review Triggers

### 24.1 Purpose

Professional legal review should be targeted.

It should not be used as a substitute for technical evidence collection.

It should also not be invoked automatically for every unresolved metadata or
provenance question.

---

### 24.2 Trigger Conditions

Professional legal review should be considered where one or more of the
following materially affects the intended publication package:

1. conflicting licences appear to apply to the same artifact;
2. a third-party component is redistributed and the applicable licence cannot
   be established;
3. a required attribution or notice obligation is materially unclear;
4. an artifact contains third-party content essential to the evaluator package
   and reuse rights remain unresolved;
5. historical licensing representations may create continuing obligations;
6. a proposed prospective licence could conflict with historical grants;
7. ownership is disputed;
8. contractual rights affect publication;
9. third-party trademarks or protected visual assets become material;
10. a rights question cannot be contained through publication-scope selection.

---

### 24.3 Non-Trigger Conditions

Professional legal review is not automatically required solely because:

- an external development tool was used;
- Python was used;
- PowerShell was used;
- a CSS font-family references a system font;
- a Git author is known but copyright ownership is not independently proven;
- a third-party component was used only as test tooling;
- an absent file reference exists;
- an evidentiary status is `NOT_OBSERVED`;
- a historical artifact is excluded from the primary evaluator path.

---

### 24.4 Current Professional-Legal-Review Position

The current inventory does not establish that the entire Commission-facing LEO
publication update requires professional legal review before any progress can
continue.

Instead:

`PROFESSIONAL_LEGAL_REVIEW SHOULD BE TRIGGERED AT THE ARTIFACT OR RIGHTS-ISSUE
LEVEL WHERE MATERIAL UNCERTAINTY CANNOT BE CONTAINED THROUGH PUBLICATION
SELECTION OR HUMAN REVIEW`.

This position prevents unresolved historical or peripheral issues from blocking
the controlled presentation of the LEO methodology where the selected evidence
surface can be made sufficiently clear.

It also preserves escalation where genuinely material rights questions remain.

---

## 25. Commission-Facing Publication Boundary

### 25.1 Purpose

This section defines the operational publication boundary supported by the
current third-party-rights inventory.

The purpose is not to declare the repository legally cleared in full.

The purpose is to determine whether sufficient evidence exists to support a
controlled Commission-facing update built around the strongest current LEO
methodology and practical evidence.

The publication boundary therefore distinguishes:

`PRIMARY_EVALUATOR_PATH`

from:

`SUPPORTING_EVIDENCE`

from:

`HISTORICAL_REFERENCE`

from:

`EXCLUDE_FROM_PRIMARY_PATH_PENDING_REVIEW`.

This classification is intended to reduce unnecessary publication complexity
while preserving historical evidence.

---

### 25.2 Primary Evaluator Path Principle

The primary evaluator path should contain only artifacts that materially help
an external reviewer understand:

1. what LEO is;
2. what institutional problem the method addresses;
3. how the method works;
4. what is currently implemented;
5. what is demonstrated;
6. what remains experimental;
7. where evidence comes from;
8. how provenance is preserved;
9. where human review occurs;
10. what the system is explicitly not authorized to do.

The primary evaluator path should not be treated as a mirror of the full
historical repository.

The governing rule is:

`PUBLICATION_SCOPE SHOULD FOLLOW EVALUATION VALUE`

subject to:

`RIGHTS_CONTROL`

`PROVENANCE_CONTROL`

and:

`HUMAN_REVIEW`.

---

### 25.3 Strong Candidate Material for Primary Evaluator Path

The current rights review does not identify a third-party-rights reason to
exclude current LEO methodology documentation solely because it describes the
method.

Subject to artifact-level review, strong candidate material includes current
documentation that explains:

- human-controlled institutional review;
- evidence lineage;
- provenance preservation;
- process-mode classification;
- evidence-derived characteristics;
- controlled signal eligibility;
- anomaly interpretation;
- human review requirements;
- non-autonomous enforcement boundaries;
- reproducibility;
- runtime validation;
- current implementation limits.

These artifacts should be selected from the current canonical LEO state rather
than historical public material where the public material no longer accurately
represents the method.

---

### 25.4 Practical Demonstration Evidence

Practical evidence should be preferred over unsupported capability claims.

Strong candidate evidence includes:

- current runtime slices;
- current tests;
- controlled reviewed examples;
- evaluator-reproducible demonstrations;
- screenshots that accurately reflect the current method;
- evidence reports;
- human-review packages;
- validation output;
- provenance records;
- documented failure and limitation boundaries.

Publication should prefer:

`CURRENT_REPRODUCIBLE_EVIDENCE`

over:

`HISTORICAL_CLAIM_ONLY`.

---

### 25.5 Screenshot Publication Boundary

The reviewed Institutional Approval Review screenshot set has:

`HIGH_EVALUATOR_RELEVANCE`

and:

`NO_OBSERVED_THIRD_PARTY_VISUAL_CONTENT`.

The screenshots may therefore remain candidates for primary or supporting
evaluation material subject to human review.

Their use should accurately represent them as:

`DEMONSTRATION_EVIDENCE`

rather than proof that the entire LEO system is production-complete.

No deletion or relicensing is authorized by this classification.

---

### 25.6 Demonstration PDF Publication Boundary

`LEO_Architecture_Overview.pdf`

may remain a supporting or historical architecture artifact, but current
Commission-facing material should prefer more current architecture
documentation if the PDF no longer accurately represents the present LEO
method.

Its unresolved embedded-font rights surface creates additional review cost but
does not automatically make the document unusable.

`LEO_Technical_Runtime_Logs.pdf`

should not be relied upon as primary evaluator evidence where current,
cleaner, reproducible runtime evidence is available.

Its current recommended classification is:

`HISTORICAL_OR_SUPPORTING_REFERENCE`

or:

`EXCLUDE_FROM_PRIMARY_EVALUATOR_PATH_PENDING_REVIEW`.

This recommendation is based on:

- historical age relative to current LEO development;
- identifiable external software-generated content;
- explicit Microsoft notice;
- embedded font-resource uncertainty;
- availability of potentially stronger current runtime evidence.

This classification does not authorize deletion.

---

### 25.7 Missing Web Asset Boundary

Pages that depend on absent:

`assets/css/main.css`

or:

`img/favicon.ico`

should not be treated as polished primary evaluator surfaces until the
publication-integrity issue is resolved.

The current inventory does not authorize restoration, replacement, or removal
of those references.

Such repair belongs to a later controlled publication-correction step.

---

### 25.8 Historical Repository Material

Historical material remains part of the repository evidence model.

Historical material may remain:

`ARCHIVED`

`REFERENCE_ONLY`

or:

`SUPPORTING_EVIDENCE`

without being elevated into the primary Commission-facing evaluator path.

This preserves institutional memory while reducing evaluator confusion.

The governing rule is:

`HISTORICAL_PRESERVATION != PRIMARY_PRESENTATION_REQUIREMENT`.

---

### 25.9 Publication Selection Rule

For each artifact considered for the Commission-facing update, the human
reviewer should determine:

`EVALUATION_VALUE`

`CURRENT_ACCURACY`

`RIGHTS_CLARITY`

`PROVENANCE_CLARITY`

`REPRODUCIBILITY`

`PUBLICATION_RISK`

and:

`NECESSITY`.

An artifact should be preferred where evaluation value is high and avoidable
rights/provenance complexity is low.

An artifact should not be included merely because it already exists in the
public repository.

---

### 25.10 Current Publication Boundary Decision

The current inventory supports the following operational conclusion:

`CONTROLLED_COMMISSION_FACING_PUBLICATION_UPDATE_CAN_CONTINUE`

subject to:

`ARTIFACT_LEVEL_SELECTION`

`HUMAN_REVIEW`

`HISTORICAL_RIGHTS_PRESERVATION`

`NO_AUTOMATIC_RELICENSING`

and:

`NO_UNSUPPORTED_RIGHTS_CLAIMS`.

The inventory does not identify a repository-wide third-party-rights blocker
that requires the entire Commission-facing update to stop.

Material unresolved issues can be contained through artifact selection,
explicit unresolved states, human review, or targeted legal review.

---

## 26. Cross-Artifact Rights Consistency Assessment

### 26.1 Purpose

The rights inventory must remain consistent with the existing LEO licensing
architecture.

This section evaluates whether the current third-party-rights findings
contradict or support the artifact-to-license mapping and broader public
evaluation strategy.

---

### 26.2 Consistency with Layered Artifact-Level Licensing

The current findings support:

`LAYERED_ARTIFACT_LEVEL_LICENSING`.

Different artifact classes demonstrate materially different rights surfaces:

- test tooling;
- runtime source;
- screenshots;
- demonstration PDFs;
- generated outputs;
- historical licences;
- absent referenced assets;
- embedded font resources;
- external software-generated text.

This confirms that a single universal licence assumption would not accurately
represent the reviewed repository.

---

### 26.3 Consistency with Historical Rights Preservation

The inventory supports:

`HISTORICAL_RIGHTS_PRESERVATION`.

No reviewed evidence justifies removing historical licence or notice records.

Historical rights evidence remains relevant even where the current publication
architecture is clarified prospectively.

No contradiction was identified between the inventory and this preservation
principle.

---

### 26.4 Consistency with Third-Party Rights Separation

The inventory demonstrates why:

`THIRD_PARTY_RIGHTS_SEPARATION`

is required.

Observed third-party or externally attributable surfaces include:

- pytest test tooling;
- Microsoft PowerShell material;
- software-generated diagnostic output;
- embedded font resources.

Unresolved possible external surfaces include:

- missing web assets;
- incomplete attribution coverage;
- partial original provenance for selected visual/data artifacts.

These surfaces must remain separate from LEO-authored method and runtime claims.

---

### 26.5 Consistency with Human-Control Principles

The inventory remains consistent with LEO governance principles.

No automatic process has:

- declared copyright ownership;
- declared infringement;
- relicensed third-party material;
- deleted historical evidence;
- determined publication permission;
- replaced professional legal review.

All material unresolved rights questions remain subject to human review.

---

### 26.6 Consistency with Public Evaluation Readiness

The rights inventory supports rather than blocks:

`LEO PUBLIC VISIBILITY & PUBLIC EVALUATION READINESS`.

Its primary function is to enable controlled selection of evaluator-facing
material.

The current findings support the strategy:

`SHOW WHAT IS STRONG, CURRENT, PRACTICAL, AND EVIDENCE-BACKED`

while:

`PRESERVING UNCERTAINTY WHERE RIGHTS OR PROVENANCE ARE NOT FULLY ESTABLISHED`.

---

### 26.7 Cross-Artifact Assessment

Current assessment:

`PASS_WITH_DOCUMENTED_UNRESOLVED_RIGHTS_ITEMS`.

No cross-artifact contradiction was identified that requires abandonment of
the Commission-facing publication track.

The unresolved items require controlled treatment, not uncontrolled expansion
of the audit scope.

---

## 27. Architectural Risks Assessment

### 27.1 Risk: Licensing Work Becomes the Primary Project

**RISK:** the rights inventory could expand indefinitely and displace the
Commission-readiness objective.

**IMPACT:** high.

**MITIGATION:** use artifact-level unresolved states and targeted review rather
than repository-wide exhaustive legal forensics.

**STATUS:** controlled by the current publication-boundary model.

---

### 27.2 Risk: Historical Material Is Mistaken for Current LEO

**RISK:** old public artifacts may cause evaluators to assess obsolete system
architecture or capability claims.

**IMPACT:** high.

**MITIGATION:** distinguish current evaluator path from historical reference
material.

**STATUS:** material issue requiring the next publication phase.

---

### 27.3 Risk: Third-Party Rights Are Hidden by First-Party Framing

**RISK:** repository or institutional attribution may be interpreted as
ownership of embedded third-party components.

**IMPACT:** high.

**MITIGATION:** maintain third-party records and artifact-level classification.

**STATUS:** controlled by this inventory.

---

### 27.4 Risk: Unknown Provenance Is Converted into Ownership

**RISK:** missing provenance may be incorrectly normalized into Foundation or
author ownership.

**IMPACT:** high.

**MITIGATION:** preserve `NOT_ESTABLISHED`, `PARTIALLY_VERIFIED`, and
`UNRESOLVED` states.

**STATUS:** controlled.

---

### 27.5 Risk: Commission Package Becomes Too Large

**RISK:** attempting to publish all historical and current material may obscure
the actual LEO method.

**IMPACT:** high.

**MITIGATION:** use a deliberately selected evaluator path.

**STATUS:** requires active publication curation.

---

### 27.6 Risk: Strong Method Is Undermined by Weak Historical Presentation

**RISK:** evaluators may judge LEO through stale architecture descriptions,
historical demos, broken asset references, or old runtime evidence.

**IMPACT:** critical for the current evaluation objective.

**MITIGATION:** conduct a current-vs-public evaluator-significant delta review
after this licensing gate closes.

**STATUS:** next-phase priority.

---

### 27.7 Risk: Rights Uncertainty Is Mistaken for Technical Immaturity

**RISK:** normal unresolved rights-review items may be presented in a way that
makes the methodology appear technically incomplete.

**IMPACT:** medium.

**MITIGATION:** separate:

`TECHNICAL_MATURITY`

from:

`RIGHTS_REVIEW_STATUS`.

**STATUS:** controlled conceptually; presentation review required.

---

### 27.8 Risk: Technical Capability Is Overstated

**RISK:** efforts to strengthen Commission-facing material could produce claims
that exceed actual implementation evidence.

**IMPACT:** critical.

**MITIGATION:** preserve explicit distinction between:

`IMPLEMENTED`

`DEMONSTRATED`

`ARCHITECTURAL`

`PLANNED`.

**STATUS:** mandatory requirement for the next phase.

---

## 28. Publication Readiness Assessment

### 28.1 Rights Readiness

The repository is not assessed as:

`FULLY_RIGHTS_CLEARED`.

That conclusion is neither established nor required for the current controlled
evaluation objective.

The current rights readiness state is:

`SUFFICIENT_FOR_CONTROLLED_ARTIFACT_SELECTION`

subject to:

- human review;
- unresolved-rights preservation;
- targeted treatment of selected artifacts;
- no automatic relicensing;
- no unsupported ownership claims.

---

### 28.2 Provenance Readiness

Repository provenance is strong for many reviewed artifacts.

Original provenance remains partial for selected:

- screenshots;
- demo data;
- embedded resources;
- historical artifacts.

Current provenance readiness is:

`PARTIAL_BUT_OPERATIONALLY_USABLE_FOR_CONTROLLED_PUBLICATION`.

---

### 28.3 Evaluator Readiness

This inventory alone does not make the repository evaluator-ready.

It removes one major uncertainty:

`WHAT CAN BE CONSIDERED FOR CONTROLLED PUBLICATION`.

Evaluator readiness still requires:

1. current-vs-public repository delta review;
2. selection of the current LEO methodology slice;
3. update of evaluator-facing architecture;
4. current runtime/test evidence;
5. clear maturity statements;
6. reproducibility route;
7. navigation repair;
8. controlled rights treatment;
9. fresh-clone evaluation.

---

### 28.4 Current Readiness Classification

Current state:

`PUBLICATION_RIGHTS_GATE: PASS_WITH_CONTROLLED_UNRESOLVED_ITEMS`

`COMMISSION_PACKAGE_READINESS: NOT_YET_COMPLETE`

`NEXT_STAGE_AUTHORIZED: CURRENT_LEO_TO_PUBLIC_REPOSITORY_DELTA_REVIEW`

No GitHub publication is authorized by this assessment.

---

## 29. Formal Review Decision

### 29.1 Review Decision

The Third-Party Rights Inventory review determines:

`PASS_WITH_CONTROLLED_UNRESOLVED_RIGHTS_ITEMS`.

---

### 29.2 Rationale

The decision is based on the following findings:

1. directly observed third-party technical use is limited and identifiable
   within the reviewed evidence surface;
2. no direct third-party Python runtime import was observed in the reviewed
   publication runtime modules;
3. pytest is directly observed as test tooling;
4. common external web libraries and bundled web fonts were not observed in the
   reviewed HTML surface;
5. missing referenced web assets remain unresolved but are containable;
6. screenshot visual review did not identify observable third-party visual
   material;
7. demonstration PDFs contain embedded third-party font resources;
8. the Technical Runtime Logs PDF contains identifiable Microsoft/PowerShell
   material and external software-generated output;
9. historical licensing evidence exists and must be preserved;
10. unresolved attribution and provenance questions remain visible;
11. no current finding requires the Commission-facing methodology update to
    stop as a whole;
12. artifact-level selection can contain the material unresolved issues.

---

### 29.3 What This Decision Does Not Mean

This decision does not mean:

`ALL_RIGHTS_RESOLVED`

`ALL_ARTIFACTS_PUBLICATION_APPROVED`

`ALL_THIRD_PARTY_LICENCES_VERIFIED`

`LEGAL_CLEARANCE_COMPLETE`

`PUBLICATION_AUTHORIZED`

`GITHUB_PUSH_AUTHORIZED`.

The decision is an internal architectural and publication-readiness decision.

---

### 29.4 What This Decision Authorizes

This review supports moving to the next controlled planning phase:

`CURRENT_LEO_TO_PUBLIC_REPOSITORY_EVALUATOR_SIGNIFICANT_DELTA_REVIEW`.

This is a read-only review phase initially.

It does not authorize repository mutation automatically.

---

## 30. Architectural Continuity Statement

The Third-Party Rights Inventory preserves continuity with the existing LEO
public-evaluation and licensing architecture.

It maintains the following principles:

`HUMAN_REVIEW_REQUIRED`

`NO_AUTONOMOUS_RIGHTS_DETERMINATION`

`NO_AUTOMATIC_RELICENSING`

`NO_UNSUPPORTED_OWNERSHIP_INFERENCE`

`HISTORICAL_RIGHTS_PRESERVATION`

`THIRD_PARTY_RIGHTS_SEPARATION`

`ARTIFACT_LEVEL_LICENSING`

`PROVENANCE_PRESERVATION`

`EVIDENCE_LINEAGE`

`PUBLICATION_SCOPE_CONTROL`.

The inventory also preserves the broader LEO governance direction:

- humans remain responsible for final decisions;
- technical evidence remains distinct from legal conclusions;
- uncertainty remains explicit;
- current implementation claims must remain evidence-backed;
- historical evidence is retained without being confused with current method;
- public evaluation material is selected deliberately rather than published by
  repository inertia.

The current licensing phase therefore remains consistent with the larger LEO
architecture.

---

## 31. Next Authorized Phase

### 31.1 Immediate Next Phase

The next authorized phase is:

`CURRENT_LEO_TO_PUBLIC_REPOSITORY_EVALUATOR_SIGNIFICANT_DELTA_REVIEW`

---

### 31.2 Purpose

The purpose of the next phase is to determine:

1. what the current canonical LEO method actually contains;
2. what the public repository currently represents;
3. which evaluator-significant elements are missing, stale, incomplete, or
   misleading;
4. which current artifacts best explain the LEO method;
5. which runtime/test evidence demonstrates that method practically;
6. which historical public artifacts should remain reference-only;
7. which materials should form the primary Commission-facing path.

---

### 31.3 Repository Boundary

The next phase must maintain strict separation between:

`CANONICAL LEO ROOT`

`D:\BBS-09-01-2026`

and:

`PUBLICATION WORKING REPOSITORY`

`D:\BBS-09-01-2026\repository_publication_staging\BBS-Open-System-publication-working`

and:

`VERIFICATION CLONES`.

No artifact may be assumed identical across those repository classes without
verification.

---

### 31.4 Initial Mode

The next phase begins:

`READ_ONLY`.

No canonical file is to be deleted or changed.

No publication repository file is to be changed until the evaluator-significant
delta is understood.

No fresh clone is to be used as a working-edit repository.

No GitHub push is authorized automatically.

---

### 31.5 Commission-Facing Objective

The next phase must serve the following objective:

`PRESENT THE CURRENT LEO METHOD AS A COHERENT, HUMAN-CONTROLLED,
EVIDENCE-BACKED, PRACTICALLY DEMONSTRABLE INSTITUTIONAL INTEGRITY METHOD
WITHOUT CLAIMING PRODUCT COMPLETENESS`.

The Commission-facing package should demonstrate:

- the problem addressed;
- the LEO methodological response;
- the architecture linking evidence, provenance, process classification,
  anomaly interpretation, and human review;
- practical implementation evidence;
- governance limits;
- reproducibility;
- current maturity;
- future development direction.

The package should not attempt to present every LEO artifact.

---

### 31.6 Final Status

`THIRD_PARTY_RIGHTS_INVENTORY_STATUS: COMPLETE_FOR_CURRENT_CONTROLLED_SCOPE`

`PUBLICATION_RIGHTS_GATE: PASS_WITH_CONTROLLED_UNRESOLVED_ITEMS`

`GITHUB_PUBLICATION: NOT_AUTHORIZED_BY_THIS DOCUMENT`

`NEXT_AUTHORIZED_PHASE: CURRENT_LEO_TO_PUBLIC_REPOSITORY_EVALUATOR_SIGNIFICANT_DELTA_REVIEW`

`HUMAN_REVIEW_REQUIRED: YES`
