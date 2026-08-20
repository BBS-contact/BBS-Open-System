# LEO Artifact-to-License Mapping Draft v1.0

DOCUMENT STATUS:

DRAFT FOR HUMAN REVIEW

DOCUMENT TYPE:

ARTIFACT-LEVEL LICENSING, RIGHTS, PUBLICATION, AND PROVENANCE MAPPING

REPOSITORY:

BBS-Open-System-publication-working

STRATEGIC TRACK:

LEO PUBLIC VISIBILITY & PUBLIC EVALUATION READINESS

MAPPING BASIS:

- `licensing/ARTIFACT_TO_LICENSE_MAPPING_REVIEW_v1.0.md`;
- `licensing/LEO_IP_AND_LICENSING_MODEL_v1.0.md`;
- `licensing/LICENSE_STRATEGY_v1.0.md`;
- current root `LICENSE`;
- historical root `LICENSE` states recovered through Git history;
- `licensing/LICENSE`;
- `licensing/NOTICE`;
- `licensing/BBS_INSTITUTIONAL_LICENSE_v1.0.md`;
- `licensing/CORE_RUNTIME_PROPRIETARY_NOTICE_v1.0.md`;
- `TRADEMARK_POLICY.md`;
- `CONTRIBUTING.md`;
- `CITATION.cff`;
- `legal/copyright.html`;
- current public-entry documentation;
- tracked artifact inventory;
- tracked code import/dependency review;
- historical archive evidence;
- canonical `leo/pyproject.toml` provenance verified by SHA-256 match.

HUMAN REVIEW REQUIRED:

YES

LEGAL EFFECT:

NONE BY ITSELF

AUTONOMOUS RIGHTS ASSIGNMENT:

NOT AUTHORIZED

AUTONOMOUS RELICENSING:

NOT AUTHORIZED

PRODUCTION MUTATION:

NOT AUTHORIZED

PUBLICATION MUTATION:

NOT AUTHORIZED

---

## 1. Purpose

This document provides a concrete artifact-level rights and licensing map for
the public BBS Open System / LEO evaluation repository.

Its purpose is to make repository rights classification inspectable without
collapsing materially different artifact classes into one repository-wide
licensing assumption.

The mapping distinguishes:

- current public visibility;
- artifact type;
- prospective publication layer;
- known rights provenance;
- current licence evidence;
- historical licence evidence;
- third-party rights;
- trademark constraints;
- security/publication constraints;
- unresolved legal questions;
- human-review state.

This document is a mapping draft.

It does not itself:

- grant a licence;
- revoke a licence;
- terminate a licence;
- relicense historical material;
- establish ownership;
- establish exclusive ownership;
- establish institutional licensing authority;
- determine infringement;
- authorize commercial deployment;
- authorize GitHub publication changes.

---

## 2. Mapping Principles

### 2.1 Public Visibility Is Not a Licence

An artifact being publicly visible does not by itself establish:

- permission to modify;
- permission to redistribute;
- permission to commercialize;
- copyright ownership;
- trademark permission;
- sublicensing authority.

PUBLICATION STATUS and LICENSING STATUS must remain distinct.

---

### 2.2 Current Licence Evidence Is Not Automatically Repository-Wide

The presence of a root licence file does not automatically establish that
every current and historical artifact is governed exclusively by that licence.

The repository contains evidence of multiple historical and current licensing
states.

Therefore:

`ROOT LICENCE PRESENT`

does not automatically mean:

`UNIVERSAL ARTIFACT LICENCE CONFIRMED`.

---

### 2.3 Historical Grants Must Be Preserved

Historical licensing evidence includes, among other things:

- BBS Public License v1.0;
- Apache License 2.0;
- GNU Affero General Public License v3;
- historical CC BY-NC-SA 4.0 strategy;
- historical institutional licensing framework;
- historical protected/proprietary core treatment.

A later repository state must not be interpreted as silently erasing rights
that may previously have been granted.

---

### 2.4 Rights Classification Is Evidence-Based

Artifact rights should be classified from reviewed evidence including:

- file-level licence statements;
- repository-level licence files;
- Git history;
- authorship evidence;
- archive records;
- contributor provenance;
- institutional agreements where available;
- third-party notices;
- dependency licences;
- publication intent;
- security classification.

Directory name alone is insufficient.

---

### 2.5 Third-Party Rights Remain Separate

Third-party rights do not disappear because material is located inside LEO.

Third-party code, test tooling, datasets, media, fonts, documentation,
standards, dependencies, external assets, and contributions must retain their
own rights status.

---

### 2.6 Trademark Rights Remain Separate

Copyright permission does not automatically grant:

- official-project status;
- Foundation endorsement;
- trademark ownership;
- misleading branding rights;
- authorization to present a derivative as an official LEO release.

Likewise, trademark restrictions must not be used to revoke copyright rights
validly granted under an applicable licence.

---

### 2.7 Public Description and Protected Implementation Are Different

Public conceptual documentation about LEO may be openly inspectable without
making the underlying protected implementation public.

Therefore:

`PUBLIC DESCRIPTION`

does not equal:

`PUBLIC IMPLEMENTATION`.

---

### 2.8 Human Review Governs Final Classification

Every final legally consequential classification requires human review.

Where evidence is incomplete, the correct state is:

`RIGHTS_REVIEW_REQUIRED`

or:

`LEGAL_REVIEW_REQUIRED`

rather than an unsupported conclusion.

---

## 3. Mapping Status Vocabulary

The following values are used throughout this document.

### Publication Layer

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

`LAYER_II_CONTROLLED_COLLABORATION_AND_INTEGRATION`

`LAYER_III_PROTECTED_CORE_TECHNOLOGY`

`HISTORICAL_PROVENANCE`

`UNRESOLVED`

---

### Public Status

`PUBLIC`

`PUBLIC_EVALUATION`

`CONTROLLED`

`PROTECTED`

`HISTORICAL_PUBLIC_RECORD`

`UNRESOLVED`

---

### Rights Status

`CURRENT_LICENCE_EVIDENCE_PRESENT`

`HISTORICAL_LICENCE_EVIDENCE_PRESENT`

`ARTIFACT_LEVEL_MAPPING_REQUIRED`

`RIGHTS_REVIEW_REQUIRED`

`LEGAL_REVIEW_REQUIRED`

`THIRD_PARTY_REVIEW_REQUIRED`

`MOSTLY_ALIGNED`

`UNRESOLVED`

---

### Security Classification

`PUBLIC`

`PUBLIC_AFTER_REVIEW`

`CONTROLLED`

`SECURITY_REVIEW_REQUIRED`

`PROTECTED`

`NOT_APPLICABLE`

---

### Human Approval

`REQUIRED`

`NOT_YET_RECORDED`

`APPROVED`

---

## 4. Repository-Level Historical Licensing Baseline

### MAP-ROOT-001 — Historical BBS Public License

ARTIFACT / PATH:

Historical root `LICENSE`

ARTIFACT CLASS:

Repository-level licence artifact

PUBLICATION LAYER:

`HISTORICAL_PROVENANCE`

CURRENT PUBLIC STATUS:

`HISTORICAL_PUBLIC_RECORD`

RIGHTS HOLDER / SOURCE:

Historical text identifies Pavlo Martseniuk as Author and rights holder.

APPLICABLE CURRENT LICENCE:

Not applicable as current root licence.

HISTORICAL LICENCE:

`BBS Public License v1.0 (BBS-PL)`

PROVENANCE:

Full historical text recovered from:

`8d8c9ec^:LICENSE`

Historical sequence confirmed:

`34230b9 Create LICENSE`

→

`300bb48 Update LICENSE`

→

`8d8c9ec Delete LICENSE`

HISTORICAL COMPLETE TEXT:

`CONFIRMED`

THIRD-PARTY RIGHTS:

Not determined by the licence text itself.

TRADEMARK STATUS:

Separate trademark review required.

SECURITY CLASSIFICATION:

`NOT_APPLICABLE`

LEGAL REVIEW STATUS:

`LEGAL_REVIEW_REQUIRED_FOR_HISTORICAL_RIGHTS_EFFECT`

HUMAN APPROVAL:

`REQUIRED`

EFFECTIVE DATE:

Historical repository state; exact legal effective scope not determined.

MAPPING DECISION:

`PRESERVE AS HISTORICAL LICENSING EVIDENCE`

DO NOT:

- recreate it as current licence without review;
- delete its provenance;
- assume its historical grants were revoked;
- assume all repository artifacts were governed by it;
- assume all embedded BBS-PL references are currently enforceable.

---

### MAP-ROOT-002 — Current Root Apache Licence

ARTIFACT / PATH:

`LICENSE`

ARTIFACT CLASS:

Repository-level licence artifact

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC`

RIGHTS HOLDER / SOURCE:

Current header identifies:

`Copyright 2026 Pavlo Martseniuk. All rights reserved.`

with institutional-context wording concerning Fundacja BBS.

APPLICABLE LICENCE:

`Apache License 2.0`

HISTORICAL LICENCE CONTEXT:

The current root Apache lineage follows deletion of the historical BBS-PL root
licence.

Confirmed transition:

`8d8c9ec Delete LICENSE`

2026-02-20T08:27:53+01:00

→

`802d58b Create LICENSE`

2026-02-20T08:34:19+01:00

The licence created by `802d58b` was Apache License 2.0.

Later root licence commits include:

- `df7b0a3 Update LICENSE file to latest Apache License version`;
- `b7b0f8c Update copyright year and owner in LICENSE file`;
- `1b6b820 Update LICENSE`;
- `1e64fa1 Align public IP licensing and governance model`.

THIRD-PARTY RIGHTS:

Not resolved by the root licence alone.

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`NOT_APPLICABLE`

LEGAL REVIEW STATUS:

`ARTIFACT_SCOPE_REVIEW_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

The root Apache licence is valid current repository evidence.

It must not yet be represented as automatically governing every current or
historical artifact.

---

### MAP-ROOT-003 — Historical AGPL Licence Artifact

ARTIFACT / PATH:

`licensing/LICENSE`

ARTIFACT CLASS:

Historical / licensing-directory licence artifact

PUBLICATION LAYER:

`HISTORICAL_PROVENANCE`

CURRENT PUBLIC STATUS:

`PUBLIC`

RIGHTS HOLDER / SOURCE:

GNU Affero General Public License v3 text.

APPLICABLE CURRENT ARTIFACT SCOPE:

`NOT YET ESTABLISHED`

HISTORICAL LICENCE:

`GNU Affero General Public License v3`

HISTORICAL STRATEGY CONTEXT:

`licensing/LICENSE_STRATEGY_v1.0.md` historically associated AGPLv3 with
Layer II — Institutional Integration Layer.

`licensing/NOTICE` preserves historical AGPL context while explicitly
rejecting automatic application to every current or future Layer II artifact.

THIRD-PARTY RIGHTS:

Potentially relevant where AGPL-covered third-party or historical code exists.

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`NOT_APPLICABLE`

LEGAL REVIEW STATUS:

`ARTIFACT_SCOPE_AND_HISTORICAL_EFFECT_REVIEW_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`PRESERVE`

Do not delete or reinterpret as universal current Layer II licence without
artifact-level evidence.

---

## 5. Historical Licensing Strategy Documents

### MAP-HIST-001 — Historical Licensing Strategy

ARTIFACT / PATH:

`licensing/LICENSE_STRATEGY_v1.0.md`

ARTIFACT CLASS:

Historical licensing strategy

PUBLICATION LAYER:

`HISTORICAL_PROVENANCE`

CURRENT PUBLIC STATUS:

`HISTORICAL_PUBLIC_RECORD`

CURRENT AUTHORITY:

`NO`

HISTORICAL MODEL:

Layer I:

`CC BY-NC-SA 4.0`

Layer II:

`AGPLv3`

Layer III:

Protected / proprietary intent.

RIGHTS HOLDER / SOURCE:

Historical document identifies Pavlo Martseniuk as Author / Owner and Fundacja
BBS as institutional operator / historical claimed exclusive licensee.

CURRENT STATUS NOTICE:

Explicitly marks those fixed licensing and institutional-authority statements
as historical / superseded and not verified current legal facts.

THIRD-PARTY RIGHTS:

Not resolved.

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`HISTORICAL_LEGAL_EFFECT_UNRESOLVED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`PRESERVE WITHOUT SUBSTANTIVE HISTORICAL REWRITING`

---

### MAP-HIST-002 — Historical Institutional Licence

ARTIFACT / PATH:

`licensing/BBS_INSTITUTIONAL_LICENSE_v1.0.md`

ARTIFACT CLASS:

Historical / proposed institutional licensing framework

PUBLICATION LAYER:

`HISTORICAL_PROVENANCE`

CURRENT PUBLIC STATUS:

`PUBLIC`

CURRENT AUTHORITY:

`NOT ESTABLISHED`

CURRENT STATUS NOTICE:

`UNVERIFIED LICENSING ARTIFACT / LEGAL REVIEW REQUIRED`

HISTORICAL CONTENT INCLUDES:

- academic / research use;
- institutional pilot use;
- commercial restrictions;
- sublicensing restrictions;
- automatic termination;
- destruction-of-copies language;
- commercial transition;
- institutional management statements.

APPLICABLE CURRENT LICENCE:

`NOT ESTABLISHED`

THIRD-PARTY RIGHTS:

Not resolved.

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`LEGAL_REVIEW_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`PRESERVE AS HISTORICAL / UNVERIFIED LICENSING EVIDENCE`

---

### MAP-HIST-003 — Historical Core Proprietary Notice

ARTIFACT / PATH:

`licensing/CORE_RUNTIME_PROPRIETARY_NOTICE_v1.0.md`

ARTIFACT CLASS:

Historical protected-core rights notice

PUBLICATION LAYER:

`HISTORICAL_PROVENANCE`

CURRENT PUBLIC STATUS:

`PUBLIC`

CURRENT STATUS NOTICE:

`HISTORICAL / LEGAL REVIEW REQUIRED`

HISTORICAL INTENT:

Protected / proprietary treatment of selected core LEO components.

CURRENT OWNERSHIP EFFECT:

`NOT ESTABLISHED BY THIS NOTICE ALONE`

CURRENT EXCLUSIVITY EFFECT:

`NOT ESTABLISHED`

CURRENT COMMERCIAL LICENSING ROUTE:

`NOT ESTABLISHED`

THIRD-PARTY RIGHTS:

Must remain distinct.

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`LEGAL_REVIEW_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`PRESERVE AS HISTORICAL RIGHTS EVIDENCE`

---

## 6. Current Prospective Licensing Architecture

### MAP-CURRENT-001 — Current IP and Licensing Model

ARTIFACT / PATH:

`licensing/LEO_IP_AND_LICENSING_MODEL_v1.0.md`

ARTIFACT CLASS:

Current prospective licensing architecture

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC`

ROLE:

Primary prospective architecture for:

- authorship;
- institutional role;
- artifact-level licensing;
- historical rights preservation;
- third-party rights;
- contributor rights;
- protected-core boundaries;
- human review;
- future rights classification.

CURRENT LEGAL EFFECT:

`POLICY / ARCHITECTURAL MODEL`

NOT:

`UNIVERSAL LICENCE GRANT`

OWNERSHIP POSITION:

Pavlo Martseniuk is identified as Author, Developer, and Original Rights
Holder of LEO, subject to identifiable third-party and contribution-specific
rights.

FUNDAJA BBS ROLE:

Institutional environment / operator context.

The document does not establish Fundacja BBS as automatic owner or verified
exclusive licensee of all LEO intellectual property.

THIRD-PARTY RIGHTS:

Explicitly preserved.

HISTORICAL LICENCES:

Explicitly preserved.

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`TARGETED_LEGAL_REVIEW_REQUIRED_FOR_HIGH_RISK_RIGHTS_DECISIONS`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`CURRENT PROSPECTIVE ARCHITECTURAL REFERENCE`

---

## 7. Public Entry Documentation

### MAP-PUBLIC-001 — README

ARTIFACT / PATH:

`README.md`

ARTIFACT CLASS:

Public entry documentation

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC`

CURRENT LICENSING POSITION:

The README acknowledges:

- licensing-related artifacts;
- historical licensing statements;
- third-party dependencies;
- unresolved licensing consistency;
- separate licensing review gate.

It explicitly avoids representing the repository as already fully reconciled.

APPLICABLE LICENCE:

`ARTIFACT_LEVEL_MAPPING_REQUIRED`

HISTORICAL LICENCE:

Potentially affected by repository licensing history.

THIRD-PARTY RIGHTS:

Acknowledged as unresolved.

TRADEMARK STATUS:

Fundacja BBS / LEO branding applies separately.

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`NO_IMMEDIATE_BLOCKER_IDENTIFIED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`MOSTLY_ALIGNED`

IMMEDIATE CORRECTION:

`NOT REQUIRED`

FINAL ACTION:

Recheck after final artifact-to-license map is approved.

---

### MAP-PUBLIC-002 — Project Status

ARTIFACT / PATH:

`PROJECT_STATUS.md`

ARTIFACT CLASS:

Public project-status / governance checkpoint documentation

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC`

CURRENT LICENSING POSITION:

Explicitly treats licensing, IP, and third-party dependency consistency as a
separate review gate.

It does not authorize automatic modification of licensing artifacts.

APPLICABLE LICENCE:

`ARTIFACT_LEVEL_MAPPING_REQUIRED`

HISTORICAL LICENCE:

Potentially affected by historical repository states.

THIRD-PARTY RIGHTS:

Explicitly acknowledged.

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`NO_IMMEDIATE_BLOCKER_IDENTIFIED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`ALIGNED WITH CURRENT REVIEW MODEL`

IMMEDIATE CORRECTION:

`NOT REQUIRED`

---

### MAP-PUBLIC-003 — Public Demo Catalog

ARTIFACT / PATH:

`PUBLIC_DEMO_CATALOG.md`

ARTIFACT CLASS:

Public evaluation navigation / demo catalog

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC`

LICENSING ROLE:

Public discovery/navigation artifact.

The current repository surface already references the separate:

`LICENSE / IP / THIRD-PARTY LICENSING CONSISTENCY REVIEW`

gate.

APPLICABLE LICENCE:

`ARTIFACT_LEVEL_MAPPING_REQUIRED`

THIRD-PARTY RIGHTS:

May apply to linked artifacts individually.

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`FINAL_CONSISTENCY_RECHECK`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`PUBLIC_NAVIGATION_ARTIFACT`

---

### MAP-PUBLIC-004 — Public Landing Page

ARTIFACT / PATH:

`index.html`

ARTIFACT CLASS:

Public evaluator / project landing page

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC`

LICENSING ROLE:

Public communication and evaluator navigation.

Current content explicitly acknowledges licensing / IP / third-party
consistency review requirements.

APPLICABLE LICENCE:

`ARTIFACT_LEVEL_MAPPING_REQUIRED`

THIRD-PARTY RIGHTS:

Must include review of any embedded:

- fonts;
- CSS libraries;
- scripts;
- icons;
- images;
- externally sourced content.

Current STEP 10 identified no tracked JavaScript/TypeScript source files, but
that does not independently establish absence of all external web assets.

TRADEMARK STATUS:

`TRADEMARK_POLICY_APPLIES_SEPARATELY`

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`THIRD_PARTY_ASSET_REVIEW_REQUIRED_IF_EXTERNAL_ASSETS_EXIST`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`PUBLIC_EVALUATION_ENTRY_ARTIFACT`

---

## 8. Public Demo Source Code

### MAP-DEMO-CODE-001 — Institutional Approval Demo Runtime Source

ARTIFACT / PATHS:

- `demos/institutional_approval_review/institutional_approval_evidence_report_validator.py`;
- `demos/institutional_approval_review/institutional_approval_human_review_package.py`;
- `demos/institutional_approval_review/institutional_approval_input_quality_report.py`;
- `demos/institutional_approval_review/institutional_approval_review_pipeline.py`.

ARTIFACT CLASS:

Public demonstration source code

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC_EVALUATION`

KNOWN IMPORT SURFACE:

Python standard library only:

- `__future__`;
- `csv`;
- `json`;
- `copy`;
- `dataclasses`;
- `datetime`;
- `pathlib`;
- `typing`.

DIRECT THIRD-PARTY RUNTIME IMPORT:

`NOT IDENTIFIED IN REVIEWED IMPORT SURFACE`

DECLARED HISTORICAL/CANONICAL RUNTIME DEPENDENCIES:

`dependencies = []`

from:

`D:\BBS-09-01-2026\leo\pyproject.toml`

Historical identity verified against March 2026 archive via SHA-256:

`f1f23a8fd4471bafc623e6b31239c9a9f64de3284492682ca6f4b33dc9bee875`

APPLICABLE CURRENT LICENCE:

`NOT YET EXPLICITLY ESTABLISHED AT ARTIFACT LEVEL`

ROOT APACHE RELATIONSHIP:

`REQUIRES SCOPE CONFIRMATION`

HISTORICAL BBS-PL RELATIONSHIP:

`REQUIRES ARTIFACT-HISTORY REVIEW IF MATERIAL`

HISTORICAL AGPL RELATIONSHIP:

`NOT AUTOMATICALLY ESTABLISHED`

THIRD-PARTY RIGHTS:

No direct third-party runtime import identified.

This does not establish that no third-party rights exist in all source
provenance.

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`PUBLIC_AFTER_PUBLICATION_REVIEW`

LEGAL REVIEW STATUS:

`LICENCE_CLASS_SELECTION_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`PUBLIC_DEMO_CODE_REQUIRES_EXPLICIT_LICENCE_CLASS`

---

## 9. Public Demo Test Code

### MAP-DEMO-TEST-001 — Institutional Approval Demo Tests

ARTIFACT / PATHS:

- `demos/institutional_approval_review/tests/test_institutional_approval_evidence_report_validator.py`;
- `demos/institutional_approval_review/tests/test_institutional_approval_human_review_package.py`;
- `demos/institutional_approval_review/tests/test_institutional_approval_input_quality_report.py`;
- `demos/institutional_approval_review/tests/test_institutional_approval_review_pipeline.py`.

ARTIFACT CLASS:

Public test / evaluation source code

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC_EVALUATION`

THIRD-PARTY DEPENDENCY:

`pytest`

PYTEST ROLE:

`TEST_TOOLING`

PYTEST MINIMUM VERSION:

`>= 7.0`

SOURCE:

Canonical:

`leo/pyproject.toml`

with:

`[tool.pytest.ini_options]`

`minversion = "7.0"`

ARCHIVAL PROVENANCE:

March 2026 archive recorded:

Path:

`leo/pyproject.toml`

Size:

`413`

Timestamp:

`2026-02-02T04:10:08+00:00`

SHA-256:

`f1f23a8fd4471bafc623e6b31239c9a9f64de3284492682ca6f4b33dc9bee875`

Current canonical file matches that SHA-256 exactly.

APPLICABLE CURRENT LEO TEST-CODE LICENCE:

`NOT YET EXPLICITLY ESTABLISHED AT ARTIFACT LEVEL`

PYTEST LICENCE:

`THIRD_PARTY_RIGHTS_RECORD_REQUIRED`

No repository-local pytest attribution/licence notice was identified during
the current evidence-completion search.

THIRD-PARTY RIGHTS:

`CONFIRMED`

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`THIRD_PARTY_DEPENDENCY_MAPPING_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

The LEO test code and pytest dependency must remain separately classified.

Public test-code licensing must not represent pytest as original proprietary
LEO technology.

---

## 10. Current Part 1 Mapping Decision

Part 1 establishes that the repository cannot be accurately governed through
one undifferentiated licence statement.

Confirmed artifact-rights domains already include:

1. historical BBS-PL licensing evidence;
2. current Apache root licensing evidence;
3. historical AGPL evidence;
4. historical CC BY-NC-SA strategy evidence;
5. historical institutional licensing evidence;
6. historical protected-core proprietary intent;
7. current prospective layered licensing architecture;
8. public entry documentation;
9. public demo runtime source;
10. public demo tests;
11. third-party pytest dependency.

The evidence supports:

`LAYERED_ARTIFACT_LEVEL_LICENSING`

with:

`HISTORICAL_RIGHTS_PRESERVATION`

and:

`THIRD_PARTY_RIGHTS_SEPARATION`

and:

`HUMAN_REVIEW_REQUIRED`.

No final public licence class for demo code or test code is selected in Part 1.

No repository mutation is authorized.

No historical licence evidence is authorized for deletion.

No historical rights are declared terminated.

No root Apache scope is declared universal.

No BBS-PL scope is declared currently enforceable.

No AGPL scope is declared automatically applicable.

No proprietary status is imposed retroactively.

---

## 11. Public Demo Data and Input Fixtures

### MAP-DEMO-DATA-001 — Institutional Approval Demo Input Data

ARTIFACT / PATH CLASS:

Input data, fixtures, examples, and structured records used by:

`demos/institutional_approval_review/`

ARTIFACT CLASS:

Public demonstration data / evaluation fixture

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC_EVALUATION`

LICENSING CHARACTER:

Data and source code must not automatically be treated as the same rights
class.

An Apache or other software licence applying to code does not by itself
establish the legal status of:

- factual records;
- synthetic records;
- manually authored examples;
- third-party data;
- personal data;
- database rights;
- copied institutional records;
- externally sourced evidence.

SOURCE / PROVENANCE REQUIREMENT:

Each publicly distributed dataset or fixture should be classifiable as one of:

`SYNTHETIC`

`ORIGINAL_PROJECT_AUTHORED`

`PUBLIC_DOMAIN_SOURCE`

`THIRD_PARTY_LICENSED`

`INSTITUTIONALLY_AUTHORIZED`

`ANONYMIZED_OR_TRANSFORMED_SOURCE`

`UNRESOLVED`

PERSONAL DATA STATUS:

`REVIEW_REQUIRED`

No assumption that demo data is personal data or non-personal data should be
made solely from its location in a demo directory.

THIRD-PARTY RIGHTS:

`REVIEW_REQUIRED`

DATABASE RIGHTS:

`REVIEW_IF_APPLICABLE`

APPLICABLE LICENCE:

`ARTIFACT_LEVEL_MAPPING_REQUIRED`

TRADEMARK STATUS:

Usually not applicable to raw data, except where names, marks, logos, or
branded material occur within the dataset.

SECURITY CLASSIFICATION:

`PUBLIC_AFTER_DATA_AND_PROVENANCE_REVIEW`

LEGAL REVIEW STATUS:

`RIGHTS_AND_DATA_ORIGIN_REVIEW_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`DEMO_DATA_MUST_HAVE_PROVENANCE_CLASSIFICATION_BEFORE FINAL PUBLIC LICENCE ASSIGNMENT`

---

## 12. Generated Demo Outputs

### MAP-DEMO-OUTPUT-001 — Generated Evidence and Quality Reports

ARTIFACT / PATH CLASS:

Generated outputs produced by public demonstration pipelines, including
structured evidence reports, quality reports, review packages, validation
results, and related machine-generated artifacts.

ARTIFACT CLASS:

Generated evaluation output

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC_EVALUATION` where explicitly included in the publication package.

DERIVATION MODEL:

Generated output may derive from:

`INPUT DATA`

+

`LEO DEMO PROCESSING LOGIC`

+

`HUMAN-DEFINED CONFIGURATION / REVIEW RULES`

Therefore its rights and publication status cannot be inferred from code
licensing alone.

EVIDENCE LINEAGE REQUIREMENT:

`REQUIRED`

Where an output is presented as evaluation evidence, provenance should preserve
the relationship:

`SOURCE INPUT`

→

`PROCESSING / VALIDATION`

→

`GENERATED OUTPUT`

→

`HUMAN REVIEW`

GENERATED STATUS:

Generated does not mean rights-free.

Generated does not mean authoritative.

Generated does not mean human-approved.

Generated does not mean legally determinative.

APPLICABLE LICENCE:

`ARTIFACT_LEVEL_MAPPING_REQUIRED`

THIRD-PARTY RIGHTS:

May inherit or reflect rights constraints from source data.

PERSONAL / SENSITIVE DATA:

`REVIEW_REQUIRED`

TRADEMARK STATUS:

Separate where branded material is reproduced.

SECURITY CLASSIFICATION:

`PUBLIC_AFTER_SOURCE_AND_OUTPUT_REVIEW`

LEGAL REVIEW STATUS:

`SOURCE_DEPENDENT`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`GENERATED_OUTPUT_REQUIRES_SOURCE-LINEAGE-AWARE RIGHTS CLASSIFICATION`

---

## 13. Evidence Reports as Evaluation Artifacts

### MAP-EVIDENCE-001 — Public Evidence Reports

ARTIFACT / PATH CLASS:

Evidence reports intentionally included to demonstrate LEO review behaviour.

ARTIFACT CLASS:

Public evaluation evidence

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC_EVALUATION`

ARCHITECTURAL ROLE:

These artifacts demonstrate system behaviour and evidence lineage.

They are not themselves autonomous institutional decisions.

They must not be represented as:

- fraud verdicts;
- legal verdicts;
- autonomous enforcement decisions;
- final institutional determinations;
- production authorization.

RIGHTS CLASSIFICATION:

The report structure may be original project material.

The underlying evidence may have separate rights.

Therefore:

`REPORT_FORMAT_RIGHTS`

and:

`SOURCE_EVIDENCE_RIGHTS`

must remain distinguishable.

APPLICABLE LICENCE:

`ARTIFACT_LEVEL_MAPPING_REQUIRED`

THIRD-PARTY RIGHTS:

`SOURCE_DEPENDENT`

SECURITY CLASSIFICATION:

`PUBLIC_AFTER_EVIDENCE_REVIEW`

LEGAL REVIEW STATUS:

`CONTEXT_DEPENDENT`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`PUBLIC_EVALUATION_EVIDENCE_WITH_PRESERVED_SOURCE_LINEAGE`

---

## 14. Screenshots and Visual Demonstration Evidence

### MAP-VISUAL-001 — Screenshots

ARTIFACT / PATH CLASS:

Screenshots included in public evaluation documentation, demo walkthroughs,
reports, or repository pages.

ARTIFACT CLASS:

Visual evidence / documentation

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC` or `PUBLIC_EVALUATION` where already published.

RIGHTS MODEL:

A screenshot may contain multiple independently protected elements:

- LEO interface material;
- operating-system UI;
- browser UI;
- third-party software UI;
- third-party logos;
- fonts;
- external websites;
- personal information;
- institutional information;
- source evidence.

Therefore screenshot ownership cannot be inferred solely from who created the
screenshot.

APPLICABLE LICENCE:

`SOURCE_DEPENDENT`

THIRD-PARTY RIGHTS:

`REVIEW_REQUIRED`

PRIVACY STATUS:

`REVIEW_REQUIRED`

TRADEMARK STATUS:

`REVIEW_IF_MARKS_VISIBLE`

SECURITY CLASSIFICATION:

`PUBLIC_AFTER_VISUAL_REVIEW`

LEGAL REVIEW STATUS:

`CONTEXT_DEPENDENT`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`SCREENSHOT_PUBLICATION_REQUIRES CONTENT-LEVEL REVIEW`

---

## 15. Public Architecture Documentation

### MAP-DOC-001 — LEO Architecture and Evaluation Documentation

ARTIFACT / PATH CLASS:

Public-facing architectural, explanatory, evaluator, governance, and
methodology documentation describing LEO.

ARTIFACT CLASS:

Project-authored documentation

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC`

EXPECTED CONTENT:

- architectural models;
- governance principles;
- evidence-lineage explanations;
- Process Mode explanations;
- evaluation procedures;
- review boundaries;
- public capability descriptions;
- non-production limitations;
- research documentation.

LICENSING HISTORY:

Historical licensing strategy associated public knowledge material with:

`CC BY-NC-SA 4.0`

That historical strategy is explicitly superseded as current authority.

Therefore it cannot automatically establish the current licence for all
documentation.

CURRENT ROOT APACHE RELATIONSHIP:

`SCOPE_CONFIRMATION_REQUIRED`

APPLICABLE CURRENT LICENCE:

`EXPLICIT DOCUMENTATION LICENCE CLASS REQUIRED`

THIRD-PARTY RIGHTS:

May exist for quoted material, standards, diagrams, external references,
images, or incorporated documentation.

TRADEMARK STATUS:

`TRADEMARK_POLICY_APPLIES_SEPARATELY`

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`LICENCE_CLASS_SELECTION_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

Public documentation should receive an explicit, intentional licence class
rather than inheriting one through historical assumption.

---

## 16. Architectural Diagrams and Models

### MAP-DOC-002 — Diagrams, Schemas, and Conceptual Models

ARTIFACT / PATH CLASS:

LEO-created architectural diagrams, conceptual models, process diagrams,
evidence-lineage diagrams, governance models, and similar explanatory
materials.

ARTIFACT CLASS:

Documentation / visual architecture

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC` where intentionally included.

RIGHTS HOLDER / SOURCE:

`PROJECT-AUTHORED WHERE VERIFIED`

This classification must not be extended to imported diagrams or third-party
visuals without provenance.

APPLICABLE LICENCE:

`EXPLICIT DOCUMENTATION LICENCE CLASS REQUIRED`

HISTORICAL LICENCE CONTEXT:

Potential historical CC BY-NC-SA 4.0 strategy relevance must be preserved
where applicable.

THIRD-PARTY RIGHTS:

`REVIEW_IF_EXTERNAL_ELEMENTS_EXIST`

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`PUBLIC_AFTER_ARCHITECTURAL_DISCLOSURE_REVIEW`

LEGAL REVIEW STATUS:

`RIGHTS_REVIEW_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`PUBLIC_ARCHITECTURE_MATERIAL`

with explicit rights classification required before final publication
normalization.

---

## 17. Governance Documentation

### MAP-GOV-001 — GOVERNANCE.md

ARTIFACT / PATH:

`GOVERNANCE.md`

ARTIFACT CLASS:

Public institutional governance documentation

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC`

CURRENT REPRESENTATIONS INCLUDE:

- institutional framework of Fundacja BBS;
- research-driven governance;
- institutional accountability;
- responsible AI practices;
- institutional oversight;
- non-replacement of institutional authority;
- absence of legally binding LEO decisions;
- protected LEO core technology;
- separation between Foundation role and LEO IP ownership.

CURRENT RIGHTS POSITION:

The document does not represent Fundacja BBS as owner of LEO intellectual
property.

APPLICABLE LICENCE:

`EXPLICIT DOCUMENTATION LICENCE CLASS REQUIRED`

THIRD-PARTY RIGHTS:

No conclusion beyond reviewed repository evidence.

TRADEMARK STATUS:

`TRADEMARK_POLICY_APPLIES`

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`INSTITUTIONAL_REPRESENTATION_REVIEW_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`PUBLIC GOVERNANCE DOCUMENTATION`

---

## 18. Contribution Documentation

### MAP-GOV-002 — CONTRIBUTING.md

ARTIFACT / PATH:

`CONTRIBUTING.md`

ARTIFACT CLASS:

Contribution governance documentation

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC`

CURRENT CONTRIBUTION RIGHTS LANGUAGE:

Contributors confirm that:

- they have the right to submit material;
- their contribution does not violate third-party rights;
- they agree to repository licensing terms.

RISK:

`repository licensing terms`

is potentially ambiguous while artifact-level licensing remains under
reconciliation.

The contribution document does not itself establish:

- copyright assignment;
- Contributor License Agreement;
- Developer Certificate of Origin;
- patent grant beyond an applicable underlying licence;
- Foundation ownership of contributions.

CONTRIBUTOR RIGHTS STATUS:

`REQUIRES EXPLICIT CONTRIBUTION MODEL`

APPLICABLE LICENCE:

`DOCUMENTATION LICENCE CLASS REQUIRED`

THIRD-PARTY RIGHTS:

`CONTRIBUTOR_PROVENANCE_REQUIRED`

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`CONTRIBUTION_RIGHTS_REVIEW_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`FOLLOW-UP CORRECTION LIKELY REQUIRED AFTER LICENSING MODEL APPROVAL`

No correction is authorized by this draft.

---

## 19. Citation Metadata

### MAP-META-001 — CITATION.cff

ARTIFACT / PATH:

`CITATION.cff`

ARTIFACT CLASS:

Academic citation metadata

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC`

CURRENT AUTHOR RECORD:

Pavlo Martseniuk

CURRENT AFFILIATION:

Fundacja BBS — Better Balance System

CURRENT LICENCE FIELD:

`See /licensing directory`

RIGHTS EFFECT:

Citation metadata does not itself establish a licence grant.

Affiliation does not itself establish institutional ownership.

APPLICABLE LICENCE:

`METADATA / DOCUMENTATION CLASS TO BE CONFIRMED`

THIRD-PARTY RIGHTS:

Not established by this file.

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`LOWER RISK / FINAL CONSISTENCY REVIEW REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`CURRENTLY COMPATIBLE WITH LAYERED LICENSING APPROACH`

---

## 20. Trademark Policy

### MAP-TM-001 — TRADEMARK_POLICY.md

ARTIFACT / PATH:

`TRADEMARK_POLICY.md`

ARTIFACT CLASS:

Trademark / brand policy

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC`

PROTECTED IDENTIFIERS LISTED:

- Fundacja BBS — Better Balance System;
- BBS;
- LEO — Logical Epistemic Oversight;
- associated logos and graphical materials.

CURRENT LICENSING STATEMENT:

The policy states that source code in the repository is licensed under:

`Apache License 2.0`

MAPPING CONCERN:

That statement is broader than the artifact-level licensing model currently
supported by the licensing review.

It risks being interpreted as a universal source-code licence assertion even
though:

- historical AGPL evidence exists;
- historical BBS-PL evidence exists;
- protected-core treatment exists;
- artifact-level classification remains required.

TRADEMARK / COPYRIGHT SEPARATION:

Conceptually correct.

Trademark restrictions must remain separate from copyright licensing.

APPLICABLE LICENCE TO POLICY DOCUMENT:

`DOCUMENTATION LICENCE CLASS REQUIRED`

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`CORRECTION_RECOMMENDED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`SUBSTANTIVE LICENSING-SCOPE CORRECTION REQUIRED BEFORE FINAL PUBLICATION READINESS`

No correction is authorized by this draft.

---

## 21. Website Copyright Notice

### MAP-LEGAL-001 — legal/copyright.html

ARTIFACT / PATH:

`legal/copyright.html`

ARTIFACT CLASS:

Public website legal notice

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC`

CURRENT GENERAL OWNERSHIP STATEMENT:

The notice states that unless otherwise indicated, website content is the
intellectual property of Fundacja BBS.

CURRENT LEO-SPECIFIC STATEMENT:

The same document separately states that:

- original LEO IP is attributed to Pavlo Martseniuk;
- identifiable third-party rights remain relevant;
- contributor-specific rights remain relevant;
- historical licensing grants remain relevant;
- Fundacja BBS is not represented as LEO owner or verified exclusive licensee.

MAPPING CONCERN:

The general website ownership statement and the LEO-specific qualification
must be read together.

For an evaluator, the broad first statement may create ambiguity where LEO
materials appear on the same website.

APPLICABLE LICENCE:

`DOCUMENTATION / WEBSITE RIGHTS CLASS REQUIRED`

THIRD-PARTY RIGHTS:

Explicitly recognized for LEO.

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`CLARIFICATION_RECOMMENDED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`MOSTLY_ALIGNED WITH A RESIDUAL OWNERSHIP-CLARITY RISK`

No mutation is authorized.

---

## 22. licensing/NOTICE

### MAP-LEGAL-002 — Historical AGPL Notice

ARTIFACT / PATH:

`licensing/NOTICE`

ARTIFACT CLASS:

Historical licensing notice

PUBLICATION LAYER:

`HISTORICAL_PROVENANCE`

CURRENT PUBLIC STATUS:

`PUBLIC`

CURRENT STATUS:

The notice preserves historical AGPL licensing context for the Institutional
Integration Layer.

It explicitly states that this historical context does not establish:

- Fundacja BBS ownership;
- verified exclusive licensing authority;
- automatic AGPL application to every current or future Layer II artifact.

HISTORICAL LICENCE:

`AGPLv3`

CURRENT LICENCE EFFECT:

`ARTIFACT_SPECIFIC / NOT UNIVERSAL`

THIRD-PARTY RIGHTS:

Separate.

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`PUBLIC`

LEGAL REVIEW STATUS:

`HISTORICAL_EFFECT_REVIEW_REQUIRED WHERE MATERIAL`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`PRESERVE`

---

## 23. Prototype and Research Implementation Code

### MAP-PROTOTYPE-001 — Publicly Exposed Prototype Code

ARTIFACT / PATH CLASS:

Prototype, research-grade, experimental, evaluator-facing, or demonstration
implementation code intentionally present in the public repository.

ARTIFACT CLASS:

Research / prototype source code

PUBLICATION LAYER:

Potentially:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

or:

`LAYER_II_CONTROLLED_COLLABORATION_AND_INTEGRATION`

depending on artifact function and disclosure intent.

CURRENT PUBLIC STATUS:

`ARTIFACT_SPECIFIC`

LICENSING HISTORY:

Historical Layer II strategy used AGPLv3.

Current prospective architecture does not automatically retain AGPLv3 for all
such artifacts.

ROOT APACHE RELATIONSHIP:

`ARTIFACT_SCOPE_CONFIRMATION_REQUIRED`

BBS-PL RELATIONSHIP:

`HISTORICAL_PROVENANCE_REVIEW_REQUIRED WHERE APPLICABLE`

APPLICABLE LICENCE:

`NOT SAFE TO ASSIGN BY DIRECTORY ALONE`

THIRD-PARTY RIGHTS:

`DEPENDENCY_AND_PROVENANCE_REVIEW_REQUIRED`

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`PUBLIC_AFTER_ARCHITECTURAL_AND_SECURITY_REVIEW`

LEGAL REVIEW STATUS:

`ARTIFACT_CLASSIFICATION_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

Each prototype must be mapped individually or through a reviewed homogeneous
artifact group.

---

## 24. Institutional Integration Artifacts

### MAP-LAYER-II-001 — Integration Interfaces and Institutional Modules

ARTIFACT / PATH CLASS:

Selected interfaces, integration modules, pilot components, institutional
adapters, and related research-grade implementation artifacts.

ARTIFACT CLASS:

Institutional integration technology

PUBLICATION LAYER:

`LAYER_II_CONTROLLED_COLLABORATION_AND_INTEGRATION`

unless separately approved for Layer I publication.

HISTORICAL LICENSING CONTEXT:

AGPLv3 was historically proposed for Layer II.

This remains historical evidence and not an automatic current assignment.

CURRENT LICENCE:

`ARTIFACT_LEVEL_DECISION_REQUIRED`

ACCESS MODEL:

`CONTROLLED_OR_PUBLIC_BY_EXPLICIT_ARTIFACT_DECISION`

THIRD-PARTY RIGHTS:

`REVIEW_REQUIRED`

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`SECURITY_REVIEW_REQUIRED`

LEGAL REVIEW STATUS:

`RIGHTS_AND_DEPLOYMENT_REVIEW_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`NO DEFAULT PUBLIC LICENCE ASSIGNMENT`

---

## 25. Protected Core Runtime

### MAP-CORE-001 — LEO Core Runtime and Governance-Critical Technology

ARTIFACT / PATH CLASS:

Technology corresponding to protected LEO core functionality where supported
by current architecture and artifact-level review.

Potential categories include:

- epistemic core processing;
- governance-critical state-transition mechanisms;
- evidence-integrity mechanisms;
- cryptographic integrity components;
- signature and identity architecture;
- protected institutional integrity mechanisms;
- other implementation artifacts explicitly classified as protected core.

ARTIFACT CLASS:

Protected core technology

PUBLICATION LAYER:

`LAYER_III_PROTECTED_CORE_TECHNOLOGY`

CURRENT PUBLIC STATUS:

`PROTECTED`

unless a specific artifact has already been validly published under another
licence.

CURRENT LICENCE:

`PROSPECTIVE PROTECTED / PROPRIETARY TREATMENT SUBJECT TO RIGHTS REVIEW`

CRITICAL NON-RETROACTIVITY RULE:

Protected-core classification must not be used to retroactively revoke rights
already granted under:

- Apache License 2.0;
- AGPLv3;
- BBS-PL;
- another applicable licence.

Historical publication and licence provenance must be checked first.

THIRD-PARTY RIGHTS:

`REVIEW_REQUIRED`

SECURITY CLASSIFICATION:

`PROTECTED`

LEGAL REVIEW STATUS:

`HIGH_PRIORITY_RIGHTS_REVIEW_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`DEFAULT NON-PUBLICATION FOR UNRELEASED PROTECTED CORE`

subject to artifact-level rights and provenance review.

---

## 26. Governance-Critical Logic

### MAP-CORE-002 — Governance and Human-Control Enforcement Boundaries

ARTIFACT / PATH CLASS:

Implementation that controls or materially affects:

- human review requirements;
- evidence acceptance;
- state transitions;
- review authorization;
- provenance preservation;
- integrity boundaries;
- production mutation restrictions;
- institutional decision boundaries.

ARTIFACT CLASS:

Governance-critical implementation

PUBLICATION LAYER:

Potentially:

`LAYER_III_PROTECTED_CORE_TECHNOLOGY`

unless explicitly classified otherwise.

ARCHITECTURAL REQUIREMENTS:

Any licensing or publication decision must preserve the distinction between:

`SOFTWARE RIGHTS`

and:

`SYSTEM GOVERNANCE AUTHORITY`.

Possession of source code does not itself grant institutional authority.

Modification rights do not automatically grant authority to represent a
modified implementation as official LEO.

CURRENT LICENCE:

`ARTIFACT_SPECIFIC`

THIRD-PARTY RIGHTS:

`REVIEW_REQUIRED`

TRADEMARK STATUS:

`OFFICIAL-LEO REPRESENTATION RESTRICTIONS APPLY SEPARATELY`

SECURITY CLASSIFICATION:

`PROTECTED_OR_SECURITY_REVIEW_REQUIRED`

LEGAL REVIEW STATUS:

`HIGH_PRIORITY`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`NO AUTOMATIC PUBLICATION OR LICENSING ASSIGNMENT`

---

## 27. Process Mode Architecture Documentation

### MAP-PROCESS-001 — Process Mode Public Architectural Material

ARTIFACT / PATH CLASS:

Public descriptions of the LEO Process Mode architecture, including the
canonical process modes:

- `DETERMINISTIC_PROCESS`;
- `STOCHASTIC_PROCESS`;
- `MIXED_PROCESS`;
- `UNKNOWN_REQUIRES_REVIEW`.

ARTIFACT CLASS:

Architectural documentation / evaluation material

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC` where intentionally published.

ARCHITECTURAL LINEAGE:

The public model may describe:

`SOURCE EVIDENCE`

→

`EVIDENCE-DERIVED CHARACTERISTICS`

→

`SIGNAL ELIGIBILITY`

→

`DETERMINISTIC / STOCHASTIC SIGNAL COUNTS`

→

`PROCESS MODE PROPOSAL`

→

`HUMAN REVIEW`

PUBLICATION LIMIT:

Publication of this conceptual architecture does not automatically authorize
publication of protected implementation details.

APPLICABLE LICENCE:

`DOCUMENTATION LICENCE CLASS REQUIRED`

THIRD-PARTY RIGHTS:

`REVIEW_IF_EXTERNAL_MATERIAL_INCLUDED`

TRADEMARK STATUS:

Separate.

SECURITY CLASSIFICATION:

`PUBLIC_AFTER_DISCLOSURE_REVIEW`

LEGAL REVIEW STATUS:

`RIGHTS_CLASSIFICATION_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`PUBLIC ARCHITECTURAL KNOWLEDGE`

---

## 28. Process Mode Runtime Implementation

### MAP-PROCESS-002 — Process Mode Implementation

ARTIFACT / PATH CLASS:

Executable implementation of Process Mode classification, confidence
estimation, signal derivation, review state management, or related runtime
logic.

ARTIFACT CLASS:

LEO runtime implementation

PUBLICATION LAYER:

`ARTIFACT_SPECIFIC`

Potentially Layer II or Layer III depending on implementation scope,
publication history, and rights provenance.

CURRENT PUBLIC STATUS:

`REQUIRES ARTIFACT-LEVEL DETERMINATION`

LICENSING PRINCIPLE:

Public architectural description does not automatically determine the licence
of runtime implementation.

CURRENT LICENCE:

`RIGHTS_REVIEW_REQUIRED`

HISTORICAL LICENCE:

Must be established from artifact history if previously published.

THIRD-PARTY RIGHTS:

`DEPENDENCY_REVIEW_REQUIRED`

SECURITY CLASSIFICATION:

`SECURITY_REVIEW_REQUIRED`

LEGAL REVIEW STATUS:

`ARTIFACT_LEVEL_REVIEW_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`DO NOT CLASSIFY FROM ARCHITECTURAL NAME ALONE`

---

## 29. Archive and Historical Evidence

### MAP-ARCHIVE-001 — LEO Archive Material

ARTIFACT / PATH CLASS:

Historical reports, snapshots, inventories, evidence packages, preserved
documents, historical licensing records, and other archived material.

ARTIFACT CLASS:

Historical provenance / institutional memory

PUBLICATION LAYER:

`HISTORICAL_PROVENANCE`

CURRENT PUBLIC STATUS:

`ARTIFACT_SPECIFIC`

ARCHITECTURAL ROLE:

The archive is part of LEO institutional memory.

Archival preservation does not imply:

- current endorsement;
- current licence assignment;
- current architectural authority;
- current legal validity;
- authorization to rewrite historical evidence.

RIGHTS MODEL:

Each archived artifact retains its own provenance and historical rights
context.

APPLICABLE LICENCE:

`SOURCE_AND_TIME_SPECIFIC`

THIRD-PARTY RIGHTS:

`PRESERVE`

SECURITY CLASSIFICATION:

`ARTIFACT_SPECIFIC`

LEGAL REVIEW STATUS:

`CONTEXT_DEPENDENT`

HUMAN APPROVAL:

`REQUIRED FOR RECLASSIFICATION OR REPUBLICATION`

MAPPING DECISION:

`PRESERVE PROVENANCE`

Do not normalize archive licensing by overwriting historical states.

---

## 30. March 2026 Archive Evidence

### MAP-ARCHIVE-002 — Archived pyproject.toml Inventory Record

ARCHIVAL REFERENCE:

`foundation/reports/march_2026/march_2026/attachments/FILES.csv`

and:

`foundation/reports/march_2026/march_2026/attachments/FILES.json`

and:

`foundation/reports/march_2026/march_2026/attachments/SYSTEM_REALITY_AUDIT_REPORT.md`

RECORDED ARTIFACT:

`leo/pyproject.toml`

RECORDED SIZE:

`413`

RECORDED TIMESTAMP:

`2026-02-02T04:10:08+00:00`

RECORDED SHA-256:

`f1f23a8fd4471bafc623e6b31239c9a9f64de3284492682ca6f4b33dc9bee875`

CURRENT CANONICAL FILE:

`D:\BBS-09-01-2026\leo\pyproject.toml`

CURRENT SIZE:

`413`

CURRENT SHA-256:

`f1f23a8fd4471bafc623e6b31239c9a9f64de3284492682ca6f4b33dc9bee875`

HASH MATCH:

`TRUE`

PROVENANCE DETERMINATION:

The current canonical file is byte-identical to the artifact represented by
the March 2026 archive hash.

VERIFIED CONTENT INCLUDES:

`license = { text = "Proprietary" }`

and:

`dependencies = []`

and:

`pytest minversion = "7.0"`

IMPORTANT INTERPRETATION LIMIT:

The historical `license = { text = "Proprietary" }` field is strong evidence
of the recorded package metadata state.

It does not by itself establish:

- current ownership of every LEO artifact;
- current licence of every public repository artifact;
- retroactive proprietary status for previously licensed artifacts;
- legal termination of historical grants.

LEGAL REVIEW STATUS:

`EVIDENCE CONFIRMED / LEGAL EFFECT ARTIFACT-SPECIFIC`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`PRESERVE AS HIGH-VALUE LICENSING PROVENANCE EVIDENCE`

---

## 31. Embedded Historical BBS-PL Declarations

### MAP-BBSPL-001 — Artifacts Containing BBS-PL References

ARTIFACT / PATH CLASS:

Current or historical artifacts containing embedded references to:

- `BBS Public License`;
- `BBS-PL`;
- BBS-PL restrictions;
- BBS-PL attribution;
- BBS-PL derivative-work requirements.

ARTIFACT CLASS:

Mixed historical licensing evidence

PUBLICATION LAYER:

`ARTIFACT_SPECIFIC`

CURRENT PUBLIC STATUS:

`ARTIFACT_SPECIFIC`

RIGHTS INTERPRETATION:

An embedded BBS-PL declaration is relevant evidence.

It must not be silently removed.

However, an embedded declaration does not automatically prove:

- the declaration was legally effective for the entire artifact;
- the declarant owned all included material;
- the declaration remains the current licence;
- later valid licensing grants did not occur;
- the artifact may now be relicensed without rights review.

CURRENT LICENCE:

`ARTIFACT_HISTORY_REVIEW_REQUIRED`

HISTORICAL LICENCE:

`BBS-PL EVIDENCE PRESENT`

THIRD-PARTY RIGHTS:

`REVIEW_REQUIRED`

SECURITY CLASSIFICATION:

`ARTIFACT_SPECIFIC`

LEGAL REVIEW STATUS:

`HIGH_PRIORITY WHERE PUBLICLY DISTRIBUTED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`PRESERVE AND MAP INDIVIDUALLY OR BY VERIFIED HOMOGENEOUS GROUP`

---

## 32. Third-Party Software Dependencies

### MAP-3P-001 — Runtime Dependencies

EVIDENCE SOURCE:

Canonical and archival-matched:

`leo/pyproject.toml`

DECLARED DEPENDENCIES:

`[]`

CURRENT EVIDENCE DETERMINATION:

No runtime dependency is declared in this pyproject artifact.

PUBLIC DEMO IMPORT REVIEW:

Reviewed Institutional Approval demo runtime source uses Python standard
library imports.

DIRECT THIRD-PARTY RUNTIME IMPORT IDENTIFIED:

`NO`

INTERPRETATION LIMIT:

This does not prove that every repository artifact is free of third-party
software dependencies.

It establishes only the reviewed dependency surface.

THIRD-PARTY RIGHTS STATUS:

`NO DIRECT RUNTIME DEPENDENCY IDENTIFIED IN REVIEWED SURFACE`

LEGAL REVIEW STATUS:

`CONTINUE ARTIFACT-SPECIFIC REVIEW WHERE REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

---

### MAP-3P-002 — pytest

THIRD-PARTY COMPONENT:

`pytest`

ROLE:

Testing framework / development and validation tooling

EVIDENCE:

Test source imports pytest.

Canonical `leo/pyproject.toml` records:

`minversion = "7.0"`

REPOSITORY-LOCAL THIRD-PARTY NOTICE IDENTIFIED DURING CURRENT REVIEW:

`NO`

THIRD-PARTY LICENCE RECORD STATUS:

`REQUIRED`

LEO OWNERSHIP:

`NO`

LEO LICENSING EFFECT:

LEO licensing must not imply ownership of pytest.

SECURITY CLASSIFICATION:

`NOT_APPLICABLE`

LEGAL REVIEW STATUS:

`THIRD_PARTY_NOTICE_AND_LICENCE_MAPPING_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`ADD TO THIRD-PARTY RIGHTS REGISTER / NOTICE MODEL BEFORE FINAL PUBLICATION READINESS`

No file creation or modification is authorized by this mapping draft.

---

## 33. Python Standard Library

### MAP-3P-003 — Standard Library Imports

REVIEWED IMPORTS INCLUDE:

- `csv`;
- `json`;
- `copy`;
- `dataclasses`;
- `datetime`;
- `pathlib`;
- `typing`;
- `__future__`.

CLASSIFICATION:

`PYTHON STANDARD LIBRARY`

MAPPING ROLE:

These imports do not constitute bundled project-authored LEO code.

They should not be represented as LEO intellectual property.

DISTRIBUTION REVIEW:

If Python itself or Python runtime components are distributed with a future
package, their applicable licensing and notices must be handled separately.

CURRENT SOURCE-ONLY PUBLICATION IMPACT:

`NO MATERIAL BLOCKER IDENTIFIED FROM IMPORTS ALONE`

---

## 34. Foundation-Specific Institutional Materials

### MAP-INST-001 — Fundacja BBS Institutional Content

ARTIFACT / PATH CLASS:

Documents and website materials specifically authored as institutional
materials of Fundacja BBS rather than as LEO software or LEO architectural
content.

ARTIFACT CLASS:

Institutional documentation

PUBLICATION LAYER:

`INSTITUTIONAL / PUBLIC`

CURRENT PUBLIC STATUS:

`ARTIFACT_SPECIFIC`

RIGHTS HOLDER:

`MUST BE ESTABLISHED FROM AUTHORSHIP / INSTITUTIONAL PROVENANCE`

Do not infer Foundation ownership merely from:

- repository location;
- Foundation branding;
- institutional context;
- LEO affiliation.

Likewise, do not infer Pavlo Martseniuk ownership of Foundation-authored
material without evidence.

APPLICABLE LICENCE:

`ARTIFACT_SPECIFIC`

TRADEMARK STATUS:

`FUNDACJA BBS TRADEMARK / BRAND POLICY MAY APPLY`

SECURITY CLASSIFICATION:

`ARTIFACT_SPECIFIC`

LEGAL REVIEW STATUS:

`RIGHTS_PROVENANCE_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`SEPARATE FOUNDATION INSTITUTIONAL CONTENT FROM LEO IP CLASSIFICATION`

---

## 35. Mixed LEO / Foundation Materials

### MAP-INST-002 — Mixed Institutional and LEO Documentation

ARTIFACT / PATH CLASS:

Documents combining:

- LEO architecture;
- Foundation institutional information;
- LEO authorship statements;
- Foundation governance role;
- branding;
- licensing information;
- public evaluation material.

ARTIFACT CLASS:

Mixed-rights institutional/project documentation

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

CURRENT PUBLIC STATUS:

`PUBLIC` where intentionally published.

RIGHTS RISK:

A single document may contain content with different provenance.

Therefore a blanket statement such as:

`all content belongs to Fundacja BBS`

or:

`all content belongs to Pavlo Martseniuk`

must not be applied without evidence.

APPLICABLE LICENCE:

`ARTIFACT_LEVEL_OR_CONTENT-CLASS REVIEW REQUIRED`

TRADEMARK STATUS:

`SEPARATE`

SECURITY CLASSIFICATION:

`PUBLIC_AFTER_REVIEW`

LEGAL REVIEW STATUS:

`RIGHTS_ATTRIBUTION_REVIEW_REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`DO NOT COLLAPSE INSTITUTIONAL ROLE INTO IP OWNERSHIP`

---

## 36. Third-Party Contributions

### MAP-CONTRIB-001 — External Contributions

ARTIFACT / PATH CLASS:

Pull requests, patches, documentation, code, tests, designs, datasets, or
other materials contributed by persons or organizations other than the
verified original rights holder for the relevant material.

ARTIFACT CLASS:

Contributor-originated material

PUBLICATION LAYER:

`ARTIFACT_SPECIFIC`

CURRENT RIGHTS MODEL:

`NOT FULLY DEFINED`

CURRENT CONTRIBUTING DOCUMENT:

Requires contributors to confirm that they have rights to submit their
material and that contributions comply with repository licensing terms.

CURRENT GAP:

No evidence reviewed in this phase establishes a universal:

- copyright assignment;
- CLA;
- DCO;
- separate patent agreement;
- Foundation ownership transfer.

RIGHTS HOLDER:

`CONTRIBUTOR OR OTHER VERIFIED RIGHTS HOLDER UNLESS VALID TRANSFER EXISTS`

APPLICABLE LICENCE:

Depends on valid contribution terms and applicable artifact licence.

THIRD-PARTY RIGHTS:

`HIGH RELEVANCE`

LEGAL REVIEW STATUS:

`CONTRIBUTION_MODEL_REQUIRED BEFORE BROADER EXTERNAL CONTRIBUTION PROGRAM`

HUMAN APPROVAL:

`REQUIRED`

MAPPING DECISION:

`CONTRIBUTOR RIGHTS MUST REMAIN TRACEABLE`

---

## 37. Artifact Provenance Minimum Record

Before an artifact receives a final public licensing classification, the
mapping should preserve at minimum:

`ARTIFACT_PATH`

`ARTIFACT_CLASS`

`ORIGIN`

`AUTHOR_OR_SOURCE`

`KNOWN_RIGHTS_HOLDER`

`CREATION_OR_IMPORT_CONTEXT`

`HISTORICAL_LICENCE`

`CURRENT_PROPOSED_LICENCE`

`THIRD_PARTY_COMPONENTS`

`PUBLICATION_STATUS`

`SECURITY_CLASSIFICATION`

`TRADEMARK_CONSTRAINTS`

`PROVENANCE_REFERENCE`

`HUMAN_REVIEW_STATUS`

`LEGAL_REVIEW_STATUS`

`EFFECTIVE_DATE_IF_APPLICABLE`

`SUPERSEDED_STATUS_IF_APPLICABLE`

This record is required because licensing decisions without provenance can
destroy the distinction between:

- original LEO material;
- Foundation institutional material;
- contributor material;
- third-party material;
- historical licensing states;
- current licensing proposals.

---

## 38. Rights-State Transition Rule

Licensing classification must be treated as a reviewed state transition.

A safe conceptual sequence is:

`ARTIFACT IDENTIFIED`

→

`PROVENANCE ESTABLISHED`

→

`HISTORICAL RIGHTS IDENTIFIED`

→

`THIRD-PARTY RIGHTS IDENTIFIED`

→

`PUBLICATION / SECURITY CLASS DETERMINED`

→

`PROPOSED LICENCE CLASS`

→

`HUMAN REVIEW`

→

`LEGAL REVIEW WHERE REQUIRED`

→

`APPROVED LICENCE STATE`

→

`PUBLIC REPRESENTATION`

No step in this sequence authorizes autonomous relicensing.

No missing evidence should be replaced with an inferred rights grant.

---

## 39. Non-Retroactivity Control

The future licensing architecture must preserve the following control:

`NEW CLASSIFICATION != RETROACTIVE REVOCATION`

A new protected classification cannot automatically revoke rights already
granted.

A new open licence cannot automatically relicense material whose rights are
not controlled by the proposed licensor.

A new institutional role cannot automatically transfer ownership.

A new trademark policy cannot cancel copyright permissions.

A repository move cannot change legal rights by itself.

A filename change cannot change legal rights by itself.

A documentation update cannot erase historical grants by itself.

This is a mandatory continuity requirement.

---

## 40. Public Evaluation Rights Boundary

The public evaluation package should expose enough material for an evaluator
to understand and inspect:

- what LEO claims to do;
- what LEO demonstrably does today;
- how evidence lineage is preserved;
- how human review operates;
- what process-mode proposals mean;
- what the system does not autonomously decide;
- what tests and demonstrations exist;
- what limitations remain;
- what licensing class applies to the exposed artifact.

Public evaluation readiness does not require:

- publication of every implementation artifact;
- disclosure of protected core technology;
- universal open-source licensing;
- removal of historical licence evidence;
- waiver of trademarks;
- transfer of ownership;
- disclosure of sensitive institutional information.

The licensing model should therefore support:

`INSPECTABILITY WITHOUT RIGHTS AMBIGUITY`

and:

`PUBLIC EVALUATION WITHOUT FORCED UNIVERSAL DISCLOSURE`.

---

## 41. Part 2 Risk Findings

The current mapping identifies the following concrete follow-up risks.

### RISK-LIC-001 — Trademark Policy Overbreadth

`TRADEMARK_POLICY.md` currently states that source code in the repository is
licensed under Apache License 2.0.

This may be broader than the evidence-supported artifact-level licensing
position.

STATUS:

`CORRECTION RECOMMENDED`

MUTATION AUTHORIZED:

`NO`

---

### RISK-LIC-002 — Contribution Terms Ambiguity

`CONTRIBUTING.md` refers contributors to the repository's licensing terms
without defining a sufficiently precise artifact-level contribution rights
model.

STATUS:

`CONTRIBUTION MODEL REQUIRED`

MUTATION AUTHORIZED:

`NO`

---

### RISK-LIC-003 — Website Ownership Generalization

`legal/copyright.html` contains a broad Foundation ownership statement while
later separately qualifying LEO ownership.

The combined text is substantially safer than an unqualified Foundation
ownership claim, but residual ambiguity remains.

STATUS:

`CLARIFICATION RECOMMENDED`

MUTATION AUTHORIZED:

`NO`

---

### RISK-LIC-004 — Third-Party pytest Notice

pytest is confirmed as test tooling, but the current evidence-completion
review did not identify a repository-local third-party licence/notice record
for it.

STATUS:

`THIRD_PARTY NOTICE / RIGHTS RECORD REQUIRED`

MUTATION AUTHORIZED:

`NO`

---

### RISK-LIC-005 — Public Demo Code Licence Class

Public demo source code is visible but does not yet have a sufficiently
explicit artifact-level licensing classification under the new layered model.

STATUS:

`LICENCE CLASS SELECTION REQUIRED`

MUTATION AUTHORIZED:

`NO`

---

### RISK-LIC-006 — Public Documentation Licence Class

Public architectural and evaluator documentation requires an explicit current
licence class.

Historical CC BY-NC-SA strategy must not be silently treated as current
authority.

STATUS:

`LICENCE CLASS SELECTION REQUIRED`

MUTATION AUTHORIZED:

`NO`

---

### RISK-LIC-007 — Protected Core Boundary

The prospective protected-core model requires artifact-level identification
before public licensing normalization.

The historical `Proprietary` pyproject metadata is relevant provenance but
does not alone define every current protected-core artifact.

STATUS:

`BOUNDARY MAPPING REQUIRED`

MUTATION AUTHORIZED:

`NO`

---

### RISK-LIC-008 — Historical BBS-PL Scope

Historical BBS-PL text and repository transition are now evidenced.

The artifact population actually governed by BBS-PL during historical states
still requires artifact-specific interpretation where legally consequential.

STATUS:

`HISTORICAL RIGHTS PRESERVATION REQUIRED`

MUTATION AUTHORIZED:

`NO`

---

## 42. Part 2 Interim Decision

The evidence continues to support:

`LAYERED_ARTIFACT_LEVEL_LICENSING`

rather than:

`ONE UNIVERSAL REPOSITORY LICENCE`.

The current mapping also supports a minimum separation among:

1. public project documentation;
2. public demo source code;
3. public test code;
4. public demo data;
5. generated evaluation outputs;
6. visual evidence;
7. Foundation institutional materials;
8. mixed LEO / Foundation materials;
9. contributor-originated materials;
10. third-party software and assets;
11. controlled integration technology;
12. protected core technology;
13. historical provenance artifacts.

The following controls remain mandatory:

`HISTORICAL_RIGHTS_PRESERVATION`

`THIRD_PARTY_RIGHTS_SEPARATION`

`CONTRIBUTOR_RIGHTS_TRACEABILITY`

`TRADEMARK_AND_COPYRIGHT_SEPARATION`

`NON_RETROACTIVE_RIGHTS_CLASSIFICATION`

`EVIDENCE_LINEAGE_PRESERVATION`

`HUMAN_REVIEW_REQUIRED`

No licensing mutation is authorized by Part 2.

No existing file is authorized for deletion.

No existing licence is declared revoked.

No historical licence is declared universally current.

No current root licence is declared universally applicable.

No protected-core classification is authorized for retroactive application.

---

## 43. Proposed Artifact Licence Classes

The following licence classes are proposed as a controlled classification
framework.

They are not yet legally effective grants.

They are intended to replace ambiguous repository-wide assumptions with
artifact-level decisions.

---

### LICENCE-CLASS-A — Public Documentation and Evaluation Material

INTENDED ARTIFACTS:

- public architecture documentation;
- evaluator guides;
- governance documentation;
- public methodology documentation;
- public process descriptions;
- public evaluation explanations;
- non-sensitive diagrams;
- public demo documentation;
- public review walkthroughs.

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

DEFAULT PUBLICATION INTENT:

`PUBLIC`

PROPOSED LICENSING CHARACTER:

A permissive or documentation-appropriate public licence should be selected
explicitly after historical rights review.

CURRENT HISTORICAL CONTEXT:

Historical Layer I strategy referenced:

`CC BY-NC-SA 4.0`

CURRENT ROOT CONTEXT:

Current root licence is:

`Apache License 2.0`

DECISION STATUS:

`FINAL LICENCE NOT YET SELECTED`

REASON:

The correct current documentation licence must account for:

- historical CC BY-NC-SA strategy;
- current Apache root licence;
- artifact-specific authorship;
- third-party material;
- Foundation institutional content;
- mixed LEO / Foundation material;
- previously published versions.

HUMAN APPROVAL:

`REQUIRED`

LEGAL REVIEW:

`RECOMMENDED BEFORE FINAL PUBLIC LICENCE NORMALIZATION`

---

### LICENCE-CLASS-B — Public Demo Source Code

INTENDED ARTIFACTS:

Publicly distributed demonstration code intentionally exposed for evaluation,
reproducibility, and technical inspection.

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

DEFAULT PUBLICATION INTENT:

`PUBLIC_EVALUATION`

PROPOSED LICENSING CHARACTER:

Explicit software licence required.

CURRENT EVIDENCE:

- current root Apache License 2.0 exists;
- historical AGPL strategy exists;
- historical BBS-PL evidence exists;
- public demo runtime source has no identified direct third-party runtime
  import within the reviewed Institutional Approval demo surface.

DECISION STATUS:

`LICENCE CLASS SELECTION REQUIRED`

NO ASSUMPTION:

The current root Apache licence must not be interpreted as universally
applicable to demo code until scope is confirmed.

The historical AGPL strategy must not be interpreted as automatically current.

The historical BBS-PL must not be interpreted as automatically current.

HUMAN APPROVAL:

`REQUIRED`

---

### LICENCE-CLASS-C — Public Demo Test Code

INTENDED ARTIFACTS:

Public test suites distributed with evaluator-facing demonstrations.

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

DEFAULT PUBLICATION INTENT:

`PUBLIC_EVALUATION`

PROJECT CODE LICENCE:

`EXPLICIT LICENCE REQUIRED`

THIRD-PARTY TEST TOOLING:

`pytest`

SEPARATE THIRD-PARTY RECORD:

`REQUIRED`

LICENSING PRINCIPLE:

LEO test-code licensing and third-party pytest licensing must remain distinct.

HUMAN APPROVAL:

`REQUIRED`

---

### LICENCE-CLASS-D — Demo Data and Evaluation Fixtures

INTENDED ARTIFACTS:

- synthetic test records;
- fixture CSV files;
- sample institutional records;
- demonstration inputs;
- example configuration data.

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

DEFAULT PUBLICATION INTENT:

`PUBLIC_EVALUATION`

LICENSING CHARACTER:

`DATA-SPECIFIC RIGHTS CLASSIFICATION REQUIRED`

MANDATORY FIELDS:

- source;
- synthetic / real classification;
- personal-data status;
- institutional authorization where applicable;
- third-party rights;
- database rights where applicable.

NO DEFAULT SOFTWARE LICENCE:

A software licence must not automatically be applied to data without
appropriate rights analysis.

HUMAN APPROVAL:

`REQUIRED`

---

### LICENCE-CLASS-E — Generated Evaluation Outputs

INTENDED ARTIFACTS:

- generated reports;
- evidence packages;
- validation outputs;
- generated review artifacts;
- reproducibility outputs.

PUBLICATION LAYER:

`LAYER_I_PUBLIC_KNOWLEDGE_AND_EVALUATION`

DEFAULT PUBLICATION INTENT:

`PUBLIC_EVALUATION`

LICENSING CHARACTER:

`SOURCE-LINEAGE-AWARE`

RIGHTS CLASSIFICATION MUST CONSIDER:

- generating code;
- input data;
- report structure;
- third-party material;
- human-authored annotations;
- personal or sensitive information.

HUMAN APPROVAL:

`REQUIRED`

---

### LICENCE-CLASS-F — Controlled Institutional Integration Technology

INTENDED ARTIFACTS:

- institutional adapters;
- controlled pilot integrations;
- internal APIs;
- integration components;
- deployment-specific adapters;
- selected research-grade implementation artifacts.

PUBLICATION LAYER:

`LAYER_II_CONTROLLED_COLLABORATION_AND_INTEGRATION`

DEFAULT PUBLICATION INTENT:

`CONTROLLED`

HISTORICAL CONTEXT:

Historical strategy associated this layer with AGPLv3.

CURRENT LICENCE:

`ARTIFACT_LEVEL_DECISION_REQUIRED`

ACCESS MODEL:

May include:

- controlled source access;
- institutional evaluation agreements;
- limited research access;
- explicitly approved public release.

NO DEFAULT AGPL ASSIGNMENT:

Historical AGPL strategy remains evidence, not an automatic current decision.

HUMAN APPROVAL:

`REQUIRED`

LEGAL REVIEW:

`REQUIRED WHERE ACCESS OR REDISTRIBUTION RIGHTS ARE CONTRACTUAL`

---

### LICENCE-CLASS-G — Protected Core Technology

INTENDED ARTIFACTS:

Unreleased or specifically protected implementation corresponding to verified
LEO core technology.

PUBLICATION LAYER:

`LAYER_III_PROTECTED_CORE_TECHNOLOGY`

DEFAULT PUBLICATION INTENT:

`PROTECTED`

PROPOSED LICENSING CHARACTER:

`PROPRIETARY / ALL RIGHTS RESERVED`

subject to:

- verified ownership;
- third-party rights;
- historical public grants;
- contributor rights;
- artifact-specific provenance;
- executed agreements where relevant.

NON-RETROACTIVITY:

This class must not be applied retroactively to material validly distributed
under an earlier public licence.

HUMAN APPROVAL:

`REQUIRED`

LEGAL REVIEW:

`HIGH PRIORITY`

---

### LICENCE-CLASS-H — Historical Provenance Artifacts

INTENDED ARTIFACTS:

- historical licences;
- superseded strategies;
- archived legal notices;
- historical rights documents;
- historical reports;
- previous public licensing states.

PUBLICATION LAYER:

`HISTORICAL_PROVENANCE`

DEFAULT PUBLICATION INTENT:

`PRESERVE`

LICENSING CHARACTER:

`SOURCE-AND-TIME-SPECIFIC`

MUTATION PRINCIPLE:

Historical text should not be rewritten to create artificial consistency.

Where clarification is necessary, use:

`STATUS NOTICE`

or:

`CONTEXT NOTICE`

while preserving original historical content.

HUMAN APPROVAL:

`REQUIRED`

---

### LICENCE-CLASS-I — Foundation Institutional Materials

INTENDED ARTIFACTS:

Material verified as Fundacja BBS institutional content rather than LEO
software or original LEO architectural IP.

PUBLICATION LAYER:

`INSTITUTIONAL`

DEFAULT PUBLICATION INTENT:

`ARTIFACT_SPECIFIC`

RIGHTS HOLDER:

`VERIFY`

LICENCE:

`ARTIFACT_SPECIFIC`

LEO OWNERSHIP:

`DO NOT INFER`

FOUNDATION OWNERSHIP:

`DO NOT INFER WITHOUT PROVENANCE`

HUMAN APPROVAL:

`REQUIRED`

---

### LICENCE-CLASS-J — Third-Party Material

INTENDED ARTIFACTS:

Any externally sourced:

- software;
- dependency;
- dataset;
- image;
- font;
- icon;
- documentation;
- standard;
- quotation;
- media;
- externally contributed material.

PUBLICATION LAYER:

`ARTIFACT_SPECIFIC`

LICENCE:

`THIRD-PARTY LICENCE CONTROLS`

LEO OWNERSHIP:

`NO UNLESS VALID RIGHTS TRANSFER EXISTS`

NOTICE REQUIREMENT:

`PRESERVE WHERE REQUIRED`

HUMAN APPROVAL:

`REQUIRED`

---

## 44. Proposed Artifact Rights Register

A future controlled rights register should record one entry for every
licensing-significant public artifact or reviewed homogeneous artifact class.

Recommended fields:

| Field | Meaning |
| --- | --- |
| `ARTIFACT_ID` | Stable mapping identifier |
| `PATH` | Repository path or controlled path group |
| `ARTIFACT_CLASS` | Documentation, code, data, test, output, archive, etc. |
| `PUBLICATION_LAYER` | Layer I, Layer II, Layer III, historical |
| `PUBLIC_STATUS` | Public, public evaluation, controlled, protected |
| `AUTHOR_OR_SOURCE` | Known author, institution, contributor, third party |
| `RIGHTS_HOLDER_STATUS` | Verified, claimed, unresolved |
| `CURRENT_LICENCE` | Current artifact licence if established |
| `HISTORICAL_LICENCE` | Relevant historical licence evidence |
| `THIRD_PARTY_RIGHTS` | None identified, present, unresolved |
| `TRADEMARK_CONSTRAINTS` | Relevant trademark / branding controls |
| `SECURITY_CLASSIFICATION` | Public, controlled, protected, review required |
| `PROVENANCE_REFERENCE` | Git commit, archive hash, source record, agreement |
| `LEGAL_REVIEW_STATUS` | Not required, recommended, required, unresolved |
| `HUMAN_REVIEW_STATUS` | Pending, approved, rejected, superseded |
| `EFFECTIVE_DATE` | Date of approved licence state |
| `SUPERSEDES` | Previous approved mapping where applicable |
| `NOTES` | Material limitations or unresolved issues |

The register should be:

`APPEND-AWARE`

`PROVENANCE-PRESERVING`

`HUMAN-REVIEWED`

and:

`REVERSIBLE THROUGH HISTORY`

It must not erase previous rights states.

---

## 45. Proposed Rights-State Values

The following rights-holder states are recommended:

`VERIFIED_PROJECT_ORIGINAL`

`VERIFIED_FOUNDATION_ORIGINAL`

`VERIFIED_CONTRIBUTOR_ORIGINAL`

`THIRD_PARTY`

`MIXED_RIGHTS`

`CLAIMED_NOT_VERIFIED`

`UNRESOLVED`

The following licence states are recommended:

`LICENCE_CONFIRMED`

`LICENCE_PROPOSED`

`HISTORICAL_LICENCE_CONFIRMED`

`MULTIPLE_HISTORICAL_LICENCES`

`RIGHTS_REVIEW_REQUIRED`

`LEGAL_REVIEW_REQUIRED`

`NO_PUBLIC_LICENCE_ASSIGNED`

The following review states are recommended:

`NOT_REVIEWED`

`EVIDENCE_REVIEWED`

`HUMAN_APPROVED`

`LEGAL_REVIEW_REQUIRED`

`SUPERSEDED`

`REJECTED`

---

## 46. Required Correction Package

The evidence-completion phase identified a limited set of current-facing
artifacts that are likely to require correction or additional rights
documentation.

No correction is authorized merely by this list.

This section defines the candidate correction package for later human
approval.

---

### CORRECTION-001 — TRADEMARK_POLICY.md

CURRENT ISSUE:

The document states:

`The source code in this repository is licensed under the Apache License 2.0.`

RISK:

This can be interpreted as a universal source-code licensing assertion.

That is broader than the current artifact-level evidence model because:

- historical AGPL evidence exists;
- historical BBS-PL evidence exists;
- protected-core treatment exists;
- current artifact-level classification is incomplete.

PROPOSED DIRECTION:

Replace repository-wide certainty with artifact-level wording.

Target meaning:

- trademarks remain separate from copyright licensing;
- applicable software licences are determined at artifact level;
- root Apache evidence remains visible;
- historical grants remain preserved;
- no universal relicensing is implied.

CHANGE STATUS:

`RECOMMENDED`

AUTHORIZED:

`NO`

---

### CORRECTION-002 — CONTRIBUTING.md

CURRENT ISSUE:

The contribution model refers contributors to:

`the repository's licensing terms`

without defining the exact rights model for contributions made to differently
licensed artifact classes.

RISK:

Contributor rights and project licensing could become ambiguous.

PROPOSED DIRECTION:

Define a controlled contribution rights model before broader external
contribution activity.

The future policy should clarify:

- contributor ownership;
- licence granted by contribution;
- whether DCO, CLA, or another mechanism is used;
- patent terms where relevant;
- third-party-content prohibition;
- contribution provenance;
- artifact-specific licence destination;
- Foundation role;
- LEO authorship / ownership distinction.

CHANGE STATUS:

`RECOMMENDED`

AUTHORIZED:

`NO`

---

### CORRECTION-003 — legal/copyright.html

CURRENT ISSUE:

The document contains a broad statement that website content belongs to
Fundacja BBS unless otherwise indicated.

The same document later provides a more precise LEO ownership qualification.

RISK:

A public evaluator may interpret the general statement before reaching the
LEO-specific qualification.

PROPOSED DIRECTION:

Clarify the separation among:

- Foundation-owned institutional material;
- original LEO material;
- contributor material;
- third-party material;
- historically licensed material.

CHANGE STATUS:

`CLARIFICATION RECOMMENDED`

AUTHORIZED:

`NO`

---

### CORRECTION-004 — Third-Party Rights Record

CURRENT ISSUE:

pytest is confirmed as public test tooling.

A dedicated repository-local third-party rights record was not identified
during the current evidence review.

PROPOSED DIRECTION:

Create a controlled third-party rights inventory or notice model containing at
minimum:

- dependency name;
- role;
- version / version constraint where known;
- upstream source;
- applicable licence;
- required attribution / notice;
- artifact paths using the dependency;
- distribution status;
- human-review status.

CURRENT CONFIRMED ENTRY:

`pytest`

ROLE:

`TEST TOOLING`

MINIMUM VERSION:

`>= 7.0`

SOURCE EVIDENCE:

Canonical `leo/pyproject.toml`, verified by SHA-256 against March 2026 archive.

CHANGE STATUS:

`REQUIRED BEFORE FINAL PUBLICATION READINESS`

AUTHORIZED:

`NO`

---

### CORRECTION-005 — Public Demo Code Licence Declaration

CURRENT ISSUE:

Public demo code is distributed for evaluation, but the artifact-level current
licence class is not explicit enough under the layered model.

PROPOSED DIRECTION:

After human and legal review, select an explicit licence class for public demo
code and state its scope clearly.

The decision must consider:

- current Apache root evidence;
- historical AGPL strategy;
- historical BBS-PL evidence;
- code provenance;
- third-party dependencies;
- previously published states.

CHANGE STATUS:

`REQUIRED`

AUTHORIZED:

`NO`

---

### CORRECTION-006 — Public Documentation Licence Declaration

CURRENT ISSUE:

Public documentation currently lacks a final explicit current documentation
licence class under the new artifact-level architecture.

PROPOSED DIRECTION:

Select an intentional documentation licence after reviewing:

- historical CC BY-NC-SA strategy;
- current root Apache representation;
- previous publication;
- mixed institutional content;
- third-party content;
- trademark separation.

CHANGE STATUS:

`REQUIRED`

AUTHORIZED:

`NO`

---

### CORRECTION-007 — Protected Core Boundary Record

CURRENT ISSUE:

The architectural model supports prospective protected-core treatment, but a
current artifact-level protected-core inventory is not yet part of the public
licensing package.

PROPOSED DIRECTION:

Create a rights-sensitive protected-core classification record without
publishing protected implementation content.

The record should identify:

- protected artifact class;
- whether artifact is currently public;
- historical licence evidence;
- third-party components;
- ownership status;
- security status;
- publication status;
- human approval.

CHANGE STATUS:

`REQUIRED BEFORE STRONG PROPRIETARY PUBLIC CLAIMS`

AUTHORIZED:

`NO`

---

### CORRECTION-008 — Embedded BBS-PL References

CURRENT ISSUE:

Five current tracked server documentation artifacts contain:

`Released under the BBS Public License v1.0 (BBS-PL).`

CONFIRMED PATHS:

- `server/api/index.md`;
- `server/auth/index.md`;
- `server/bridge/index.md`;
- `server/gateway/index.md`;
- `server/security/index.md`.

HISTORICAL EVIDENCE:

Full BBS Public License v1.0 text existed historically at root `LICENSE`.

CURRENT BBS-PL ROOT TEXT:

No longer present.

PROPOSED DIRECTION:

Do not delete or rewrite these declarations until artifact-level historical
scope is reviewed.

Possible future outcomes include:

- retain as valid current declaration;
- retain with historical-status notice;
- supersede with explicit new licence statement;
- preserve historical statement in archive while updating current artifact
  rights representation.

CHANGE STATUS:

`HIGH-PRIORITY RIGHTS REVIEW`

AUTHORIZED:

`NO`

---

## 47. Files Not Requiring Immediate Licensing Mutation

The current review does not identify an immediate licensing contradiction
requiring mutation in:

`README.md`

or:

`PROJECT_STATUS.md`

Both currently act as review-gate documentation rather than unsupported final
licensing declarations.

Their status is:

`MOSTLY ALIGNED`

and:

`FINAL CONSISTENCY RECHECK REQUIRED`

Similarly, historical licensing artifacts should remain unchanged unless a
separate human-approved clarification mechanism is used.

---

## 48. Licensing Evidence Completion Summary

The following evidence targets have been materially addressed.

### Current Prospective Licensing Architecture

STATUS:

`REVIEWED`

SOURCE:

`licensing/LEO_IP_AND_LICENSING_MODEL_v1.0.md`

---

### Historical Licensing Strategy

STATUS:

`REVIEWED`

SOURCE:

`licensing/LICENSE_STRATEGY_v1.0.md`

CONFIRMED HISTORICAL MODEL:

Layer I:

`CC BY-NC-SA 4.0`

Layer II:

`AGPLv3`

Layer III:

`PROTECTED / PROPRIETARY INTENT`

---

### Historical BBS Public License

STATUS:

`FULL TEXT CONFIRMED`

SOURCE:

Historical root `LICENSE`

RECOVERED FROM:

`8d8c9ec^:LICENSE`

---

### BBS-PL to Apache Repository Transition

STATUS:

`CONFIRMED`

TIMELINE:

`300bb48`

2025-12-03T21:16:12+01:00

Historical BBS-PL state.

`8d8c9ec`

2026-02-20T08:27:53+01:00

Root `LICENSE` deleted.

`802d58b`

2026-02-20T08:34:19+01:00

New Apache License 2.0 root `LICENSE` created.

LEGAL RELICENSING EFFECT:

`NOT DETERMINED`

---

### Embedded BBS-PL References

STATUS:

`CONFIRMED`

COUNT:

`5`

CURRENT RIGHTS EFFECT:

`UNRESOLVED`

---

### Current Public Entry Licensing Representations

README:

`MOSTLY ALIGNED`

PROJECT_STATUS:

`ALIGNED WITH CURRENT REVIEW MODEL`

---

### Third-Party Dependency Surface

PUBLIC DEMO RUNTIME:

No direct third-party runtime import identified in the reviewed Python source.

TEST SURFACE:

`pytest` confirmed.

---

### Historical pyproject.toml Provenance

STATUS:

`STRONGLY CONFIRMED`

ARCHIVE PATH:

`leo/pyproject.toml`

ARCHIVE SIZE:

`413`

ARCHIVE SHA-256:

`f1f23a8fd4471bafc623e6b31239c9a9f64de3284492682ca6f4b33dc9bee875`

CURRENT CANONICAL SIZE:

`413`

CURRENT CANONICAL SHA-256:

`f1f23a8fd4471bafc623e6b31239c9a9f64de3284492682ca6f4b33dc9bee875`

HASH MATCH:

`TRUE`

CONTENT CONFIRMED:

`license = { text = "Proprietary" }`

`dependencies = []`

`pytest minversion = "7.0"`

INTERPRETATION:

Historical package metadata is verified.

Universal legal effect is not inferred.

---

## 49. Evidence Gaps Remaining After Completion Phase

The evidence-completion phase is sufficient for architectural mapping, but
several legal or artifact-level questions remain unresolved.

### GAP-001 — Final Public Documentation Licence

STATUS:

`UNRESOLVED`

---

### GAP-002 — Final Public Demo Code Licence

STATUS:

`UNRESOLVED`

---

### GAP-003 — Exact Historical BBS-PL Artifact Scope

STATUS:

`UNRESOLVED WHERE LEGALLY MATERIAL`

---

### GAP-004 — Current Scope of Root Apache License

STATUS:

`ARTIFACT-SPECIFIC CONFIRMATION REQUIRED`

---

### GAP-005 — Contributor Rights Model

STATUS:

`NOT FORMALLY COMPLETED`

---

### GAP-006 — Third-Party Rights Inventory

STATUS:

`PARTIAL`

Confirmed:

`pytest`

Further artifact-specific review may identify additional external material.

---

### GAP-007 — Protected Core Artifact Inventory

STATUS:

`NOT YET FORMALLY CREATED`

---

### GAP-008 — Foundation / LEO Mixed-Content Ownership Boundary

STATUS:

`ARTIFACT-SPECIFIC REVIEW REQUIRED`

---

### GAP-009 — Demonstration Data Provenance

STATUS:

`ARTIFACT-SPECIFIC REVIEW REQUIRED`

---

### GAP-010 — Visual / Screenshot Rights Review

STATUS:

`ARTIFACT-SPECIFIC REVIEW REQUIRED`

---

## 50. Architectural Risks Assessment

### Risk A — Repository-Wide Licence Overgeneralization

SEVERITY:

`HIGH`

DESCRIPTION:

A root licence may be interpreted as governing all repository artifacts even
where historical, third-party, institutional, or protected-core rights differ.

MITIGATION:

Artifact-level rights register.

STATUS:

`OPEN / CONTROLLED`

---

### Risk B — Silent Historical Relicensing

SEVERITY:

`HIGH`

DESCRIPTION:

Historical BBS-PL, AGPL, CC BY-NC-SA, or other grants could be obscured by
current repository normalization.

MITIGATION:

Historical provenance preservation and non-retroactivity rule.

STATUS:

`CONTROLLED BY CURRENT REVIEW MODEL`

---

### Risk C — Contributor Rights Ambiguity

SEVERITY:

`HIGH`

DESCRIPTION:

External contributions may enter differently licensed artifact classes without
a sufficiently explicit contribution-rights framework.

MITIGATION:

Controlled contribution model.

STATUS:

`OPEN`

---

### Risk D — Third-Party Rights Omission

SEVERITY:

`MEDIUM TO HIGH`

DESCRIPTION:

External dependencies or assets may be redistributed without a sufficient
rights record.

CONFIRMED EXAMPLE:

`pytest`

MITIGATION:

Third-party rights inventory.

STATUS:

`OPEN`

---

### Risk E — Protected-Core Overclaim

SEVERITY:

`HIGH`

DESCRIPTION:

Protected-core language could be applied too broadly and conflict with
historical public grants or third-party rights.

MITIGATION:

Protected-core artifact inventory plus provenance review.

STATUS:

`OPEN / CONTROLLED`

---

### Risk F — Foundation / LEO Ownership Conflation

SEVERITY:

`HIGH`

DESCRIPTION:

Institutional role may be interpreted as ownership, or LEO authorship may be
interpreted as ownership of Foundation or third-party material.

MITIGATION:

Explicit content-class and provenance mapping.

STATUS:

`PARTIALLY CONTROLLED`

---

### Risk G — Trademark / Copyright Conflation

SEVERITY:

`MEDIUM`

DESCRIPTION:

Trademark restrictions may be interpreted as broader copyright restrictions,
or open licensing may be interpreted as trademark permission.

MITIGATION:

Separate trademark policy and artifact-level copyright licensing.

STATUS:

`CONCEPTUALLY CONTROLLED / WORDING CORRECTION REQUIRED`

---

### Risk H — Demo Data Rights Ambiguity

SEVERITY:

`MEDIUM TO HIGH`

DESCRIPTION:

Public fixtures may contain synthetic, institutional, third-party, personal,
or derived material without explicit origin classification.

MITIGATION:

Demo-data provenance register.

STATUS:

`OPEN`

---

### Risk I — False Legal Certainty

SEVERITY:

`HIGH`

DESCRIPTION:

Historical or prospective licensing text may be represented as current
enforceable legal fact without sufficient legal evidence.

MITIGATION:

Human review, legal-review flags, explicit unresolved states.

STATUS:

`CONTROLLED BY CURRENT DOCUMENTATION MODEL`

---

## 51. Implementation Readiness Assessment

ARCHITECTURAL MODEL:

`READY`

EVIDENCE COMPLETION:

`SUFFICIENT FOR CONTROLLED MAPPING`

HISTORICAL LICENSING PROVENANCE:

`SUFFICIENT FOR CURRENT ARCHITECTURAL DECISION`

PUBLIC DEMO RIGHTS MAPPING:

`PARTIAL / READY FOR FINAL CLASS SELECTION`

PUBLIC DOCUMENTATION RIGHTS MAPPING:

`PARTIAL / READY FOR FINAL CLASS SELECTION`

THIRD-PARTY RIGHTS INVENTORY:

`PARTIAL`

CONTRIBUTOR RIGHTS MODEL:

`NOT READY`

PROTECTED-CORE ARTIFACT INVENTORY:

`NOT READY`

DEMO DATA RIGHTS INVENTORY:

`NOT READY`

PUBLIC LICENSING MUTATION:

`NOT YET READY`

GITHUB PUSH OF LICENSING CORRECTION PACKAGE:

`NOT YET AUTHORIZED`

FINAL PUBLICATION READINESS:

`NOT YET ACHIEVED`

IMPLEMENTATION READINESS DECISION:

`READY FOR CONTROLLED CORRECTION-PACKAGE DESIGN`

but:

`NOT READY FOR UNREVIEWED LICENSING MUTATION`

---

## 52. Formal Review Decision

REVIEW DECISION:

`PASS WITH REQUIRED CONTROLLED FOLLOW-UP`

The evidence is sufficient to confirm that the repository requires:

`LAYERED_ARTIFACT_LEVEL_LICENSING`

with:

`HISTORICAL_RIGHTS_PRESERVATION`

`THIRD_PARTY_RIGHTS_SEPARATION`

`CONTRIBUTOR_RIGHTS_TRACEABILITY`

`TRADEMARK_AND_COPYRIGHT_SEPARATION`

`PROTECTED_CORE_BOUNDARY_CONTROL`

and:

`HUMAN_REVIEW_REQUIRED`.

The review does not support:

`ONE UNIVERSAL REPOSITORY LICENCE`

as the sole representation of all current and historical artifact rights.

The review also does not support immediate mass modification of licensing
files.

The correct next development activity is a controlled correction-package
design based on the mapping in this document.

---

## 53. Architectural Continuity Statement

This mapping remains consistent with the current LEO architectural direction.

It preserves:

- human review required;
- no autonomous enforcement;
- no fraud verdicts;
- no autonomous legal verdicts;
- no production mutation without explicit authorization;
- evidence lineage;
- provenance preservation;
- institutional memory;
- historical archive continuity;
- separation of evidence from reviewed knowledge;
- reversible audit trails;
- controlled public evaluation.

It also preserves the distinction among:

`LEO ARCHITECTURE`

`LEO IMPLEMENTATION`

`FUNDACJA BBS INSTITUTIONAL ROLE`

`INTELLECTUAL PROPERTY`

`LICENSING`

`TRADEMARKS`

`THIRD-PARTY RIGHTS`

`CONTRIBUTOR RIGHTS`

and:

`PUBLICATION STATUS`.

No licensing decision in this document changes LEO governance authority.

No copyright licence grants autonomous institutional authority.

No source-code access grants authority to make official LEO decisions.

---

## 54. Public Evaluation Continuity Statement

The mapping supports the strategic track:

`LEO PUBLIC VISIBILITY & PUBLIC EVALUATION READINESS`

because it makes the public package more defensible for:

- external technical review;
- academic review;
- institutional evaluation;
- foundation cooperation;
- AI governance review;
- future conference presentation;
- reproducibility assessment;
- public GitHub inspection.

The objective is not maximum disclosure.

The objective is:

`MAXIMUM JUSTIFIABLE INSPECTABILITY WITH CONTROLLED RIGHTS BOUNDARIES`.

---

## 55. Explicitly Unauthorized Actions

This document does not authorize:

- editing root `LICENSE`;
- deleting root `LICENSE`;
- replacing Apache License 2.0;
- editing `licensing/LICENSE`;
- deleting AGPL evidence;
- deleting BBS-PL historical evidence;
- deleting embedded BBS-PL declarations;
- rewriting historical licence documents;
- declaring historical grants terminated;
- universal relicensing;
- retroactive proprietary classification;
- publishing protected core implementation;
- changing contributor rights;
- creating a CLA without separate review;
- modifying `TRADEMARK_POLICY.md`;
- modifying `CONTRIBUTING.md`;
- modifying `legal/copyright.html`;
- modifying demo code licences;
- modifying public documentation licences;
- creating third-party notice files;
- staging changes;
- committing changes;
- pushing licensing changes to GitHub;
- altering Git history;
- deleting archive evidence.

Each such action requires a separate human-approved controlled step.

---

## 56. Human Review Record

DOCUMENT:

`ARTIFACT_TO_LICENSE_MAPPING_DRAFT_v1.0.md`

DOCUMENT ROLE:

Controlled artifact-level rights and licensing mapping draft.

LEGAL STATUS:

`NOT LEGAL ADVICE`

LICENCE-GRANT STATUS:

`NO LICENCE GRANT`

OWNERSHIP-DETERMINATION STATUS:

`NO FINAL OWNERSHIP DETERMINATION`

INFRINGEMENT-DETERMINATION STATUS:

`NONE`

RELICENSING STATUS:

`NOT AUTHORIZED`

PRODUCTION AUTHORITY:

`NONE`

PUBLICATION MUTATION AUTHORITY:

`NONE`

HUMAN REVIEW REQUIRED:

`YES`

PROFESSIONAL LEGAL REVIEW:

`REQUIRED FOR LEGALLY CONSEQUENTIAL RIGHTS DECISIONS`

---

## 57. Review Outcome by Major Artifact Class

| Artifact Class | Mapping State | Immediate Mutation |
| --- | --- | --- |
| Root Apache licence | Current evidence confirmed; scope review required | NO |
| Historical BBS-PL | Historical full text confirmed | NO |
| Historical AGPL | Historical evidence confirmed | NO |
| Historical CC BY-NC-SA strategy | Confirmed historical strategy | NO |
| Public documentation | Explicit licence class required | NO |
| Public demo source | Explicit licence class required | NO |
| Public demo tests | Explicit licence + pytest separation required | NO |
| Demo data | Provenance classification required | NO |
| Generated outputs | Lineage-aware classification required | NO |
| Screenshots | Content-level rights review required | NO |
| Institutional materials | Provenance-specific rights mapping required | NO |
| Contributor material | Contribution model required | NO |
| Third-party dependencies | Partial inventory; pytest confirmed | NO |
| Controlled integration technology | Artifact-specific licence required | NO |
| Protected core | Formal boundary inventory required | NO |
| Historical archive | Preserve source-and-time-specific rights | NO |
| Trademark policy | Licensing-scope correction recommended | NO |
| Copyright notice | Ownership clarification recommended | NO |

---

## 58. Proposed Controlled Correction Order

If human approval is granted after review of this mapping, the recommended
correction sequence is:

### Phase A — Rights Infrastructure

1. create third-party rights inventory;
2. define public documentation licence class;
3. define public demo code licence class;
4. define public demo test-code licence class;
5. define protected-core artifact classification structure;
6. define contributor rights model.

No existing current-facing public document should be changed before these
foundation decisions are made.

---

### Phase B — Current-Facing Policy Corrections

After Phase A approval:

1. review and correct `TRADEMARK_POLICY.md`;
2. review and correct `CONTRIBUTING.md`;
3. review and clarify `legal/copyright.html`;
4. add approved third-party rights reference;
5. add approved artifact-level licence references to public code and
   documentation where required.

---

### Phase C — Embedded Historical Licence Resolution

After historical-rights review:

1. classify the five current BBS-PL server artifacts;
2. determine whether current declaration remains valid;
3. preserve historical provenance;
4. update current-facing representation only if separately approved.

---

### Phase D — Public Evaluation Consistency Review

After approved corrections:

recheck:

- `README.md`;
- `PROJECT_STATUS.md`;
- `PUBLIC_DEMO_CATALOG.md`;
- `index.html`;
- public demo documentation;
- licensing directory;
- copyright notice;
- trademark policy;
- contribution policy;
- third-party rights inventory.

Objective:

`NO CURRENT-FACING LICENSING CONTRADICTIONS`

---

### Phase E — Controlled GitHub Publication

Only after:

- rights mapping approved;
- correction package reviewed;
- tracked diff reviewed;
- final continuity review passed;
- human approval granted.

Then:

- stage exact approved set;
- verify exact staged scope;
- commit logical package;
- inspect commit;
- perform publication push only after separate explicit authorization;
- verify remote state from a fresh clone or equivalent independent checkout.

---

## 59. Next Authorized Phase

The next recommended phase is:

`ARTIFACT_TO_LICENSE_MAPPING_DRAFT_HUMAN_REVIEW`

This phase must initially remain:

`READ ONLY`

The immediate objective is to verify:

1. that all mapped artifact classes are materially correct;
2. that historical licensing evidence is represented accurately;
3. that no ownership statement exceeds available evidence;
4. that no current licence scope is overstated;
5. that third-party rights remain distinct;
6. that contributor rights remain unresolved where appropriate;
7. that protected-core classification remains prospective and non-retroactive;
8. that the correction package contains all known current-facing issues;
9. that no required correction has been omitted;
10. that no unnecessary correction has been introduced.

Only after this human review may the first correction artifact be authorized.

---

## 60. First Candidate Action After Human Approval

If this mapping draft passes human review, the recommended first mutation is
not a change to `LICENSE`.

The recommended first rights-infrastructure artifact is:

`THIRD_PARTY_RIGHTS_INVENTORY_v1.0.md`

or an equivalent controlled third-party rights record.

Reason:

- it adds missing rights clarity without changing existing grants;
- it preserves existing licences;
- it separates third-party material from LEO ownership;
- it creates infrastructure required before final public licensing cleanup;
- it is lower risk than immediate relicensing;
- it supports later corrections to `README`, policies, and demo documentation.

This recommendation does not itself authorize file creation.

---

## 61. Final Status Declaration

DOCUMENT:

`LEO ARTIFACT-TO-LICENSE MAPPING DRAFT v1.0`

REPOSITORY:

`BBS-Open-System-publication-working`

STRATEGIC TRACK:

`LEO PUBLIC VISIBILITY & PUBLIC EVALUATION READINESS`

REVIEW BASIS:

`REPOSITORY EVIDENCE + GIT PROVENANCE + ARCHIVE PROVENANCE + CANONICAL HASH-VERIFIED EVIDENCE`

RECOMMENDED LICENSING ARCHITECTURE:

`LAYERED_ARTIFACT_LEVEL_LICENSING`

HISTORICAL RIGHTS:

`PRESERVE`

ROOT APACHE LICENCE:

`CURRENT EVIDENCE CONFIRMED / UNIVERSAL SCOPE NOT ASSUMED`

HISTORICAL BBS-PL:

`FULL TEXT AND TRANSITION PROVENANCE CONFIRMED`

HISTORICAL AGPL:

`CONFIRMED`

HISTORICAL CC BY-NC-SA STRATEGY:

`CONFIRMED`

PUBLIC DOCUMENTATION LICENCE:

`FINAL CLASS NOT YET SELECTED`

PUBLIC DEMO CODE LICENCE:

`FINAL CLASS NOT YET SELECTED`

PUBLIC TEST CODE LICENCE:

`FINAL CLASS NOT YET SELECTED`

THIRD-PARTY RIGHTS:

`PARTIAL INVENTORY / pytest CONFIRMED`

PROTECTED CORE:

`PROSPECTIVE PROTECTED / PROPRIETARY TREATMENT SUBJECT TO ARTIFACT-LEVEL RIGHTS REVIEW`

CONTRIBUTOR RIGHTS MODEL:

`FOLLOW-UP REQUIRED`

DEMO DATA RIGHTS:

`FOLLOW-UP REQUIRED`

TRADEMARK / COPYRIGHT SEPARATION:

`REQUIRED`

HUMAN REVIEW:

`REQUIRED`

LEGAL REVIEW:

`REQUIRED WHERE LEGALLY CONSEQUENTIAL`

AUTONOMOUS RELICENSING:

`NOT AUTHORIZED`

AUTONOMOUS ENFORCEMENT:

`NOT AUTHORIZED`

PRODUCTION MUTATION:

`NOT AUTHORIZED`

PUBLICATION MUTATION:

`NOT AUTHORIZED`

GITHUB PUSH:

`NOT AUTHORIZED BY THIS DOCUMENT`

CURRENT REVIEW DECISION:

`PASS WITH REQUIRED CONTROLLED FOLLOW-UP`

NEXT AUTHORIZED PHASE:

`ARTIFACT_TO_LICENSE_MAPPING_DRAFT_HUMAN_REVIEW`

---

END OF DOCUMENT
