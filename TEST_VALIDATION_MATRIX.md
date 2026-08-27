# LEO Test Validation Matrix

**Document status:** Living canonical validation and evidence matrix\
**Strategic track:** LEO Public Visibility & Public Evaluation
Readiness\
**Canonical repository root:** `D:\BBS-09-01-2026`\
**Inventory baseline HEAD:** `8b6a6e3df2892e913321b0f06f8b330b686cc56e`\
**Inventory basis:** tracked repository files identified through
`git ls-files`\
**Human review required:** Yes\
**Autonomous enforcement:** No\
**Production mutation authorized by this document:** No\
**Last matrix baseline:** 2026-08-27

------------------------------------------------------------------------

## 1. Purpose

This document is the persistent LEO test validation matrix. Its purpose
is to preserve, in one maintainable evidence artifact, the distinction
between:

1.  test files present in the canonical repository;
2.  test files belonging to the current runtime;
3.  legacy or historical test assets;
4.  publication copies;
5.  auxiliary or other canonical test assets;
6.  test cases collected by a test runner;
7.  tests actually executed;
8.  tests reported as passed in a particular historical or current
    verification run.

The matrix is intended for repeated update as LEO grows. It must not be
recreated from memory for every public evaluation cycle. New test
scopes, verified executions, publication baselines, and discrepancies
are to be appended or updated with explicit evidence and provenance.

This matrix is designed to support technical review by external
evaluators, including European Commission / EU AI Office reviewers,
without overstating what has been verified.

------------------------------------------------------------------------

## 2. Interpretation rule

A **test file count is not a test case count**.

A **collected test case count is not an executed test count**.

An **executed test count is not automatically a passed test count**.

A historical successful run is evidence for the state and revision at
which it was performed; it must not be silently represented as a fresh
execution against a later repository revision.

Accordingly, this document uses separate evidence dimensions:

| Evidence dimension              | Meaning                                                                                                              |
|:--------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| `TRACKED_FILE_INVENTORY`        | Test-bearing files are present and tracked by Git at the stated baseline.                                            |
| `COLLECTION_EVIDENCE`           | A test runner collected test cases at a stated baseline/run.                                                         |
| `EXECUTION_EVIDENCE`            | Tests were actually executed in a stated run.                                                                        |
| `PASS_EVIDENCE`                 | The stated execution completed with passing results.                                                                 |
| `HISTORICAL_EXECUTION_EVIDENCE` | A prior verified execution exists, but it is not represented as a fresh execution of the current baseline.           |
| `PUBLICATION_COPY`              | A test file is part of a release/staging copy and must not be double-counted as an independent canonical test asset. |

------------------------------------------------------------------------

## 3. Evidence baseline used for this matrix

The controlled read-only repository inventory established:

-   `HEAD=8b6a6e3df2892e913321b0f06f8b330b686cc56e`
-   `HEAD_MATCH=True`
-   `TOTAL_TRACKED_TEST_FILES=198`
-   `TRACKED_CHANGES=0`
-   `STAGED_FILES=0`
-   `HEAD_UNCHANGED=True`
-   `READ_ONLY_COMPLETE=True`

The inventory identified test files using tracked paths matching the
repository test-file naming rule:

`(^|/)(test_[^/]+\.py|[^/]+_test\.py)$`

The inventory operation did not itself execute the 198 files and did not
establish that every test case contained in them passes at this
baseline.

------------------------------------------------------------------------

## 4. Repository-wide tracked test-file inventory

### 4.1 Normalized class totals

| Class                                 | Tracked test files | Interpretation                                                                                                           |
|:--------------------------------------|-------------------:|:-------------------------------------------------------------------------------------------------------------------------|
| CURRENT                               |                125 | Current runtime and current demonstration test assets.                                                                   |
| LEGACY_OR_HISTORICAL                  |                 62 | Historical/legacy runtime test assets retained in the repository.                                                        |
| PUBLICATION_COPY                      |                  8 | Test files present in publication/release copies; not independent canonical test assets for aggregate capability claims. |
| OTHER_CANONICAL                       |                  1 | Canonical test outside the principal current runtime grouping.                                                           |
| AUXILIARY                             |                  1 | Auxiliary audit/smoke test asset.                                                                                        |
| UNCLASSIFIED at initial normalization |                  1 | Subsequently identified as the epistemic ingestion test path; retained here to preserve the original inventory result.   |
| **TOTAL**                             |            **198** | Complete tracked test-file inventory at the stated HEAD under the naming rule.                                           |

Check:

`125 + 62 + 8 + 1 + 1 + 1 = 198`

------------------------------------------------------------------------

## 5. Current runtime and demonstration test-file matrix

The current class contains **125 tracked test files**.

| Current scope                                            | Test files | Inventory status            | Current-baseline execution status in this matrix                                                          |
|:---------------------------------------------------------|-----------:|-----------------------------|:----------------------------------------------------------------------------------------------------------|
| `leo/runtime/tests`                                      |         81 | Confirmed tracked inventory | Not inferred from inventory                                                                               |
| `leo/runtime/process_mode`                               |         15 | Confirmed tracked inventory | Separate historical/focused evidence may exist; no blanket fresh-run claim made here                      |
| `leo/runtime/anomaly_library`                            |         12 | Confirmed tracked inventory | Separate historical evidence exists for earlier runtime checkpoints; no blanket fresh-run claim made here |
| `leo/runtime/knowledge_layer`                            |         10 | Confirmed tracked inventory | Separate historical evidence exists for earlier checkpoints; no blanket fresh-run claim made here         |
| `leo/runtime/demos/grant_expense_review`                 |          1 | Confirmed tracked inventory | Not inferred from inventory                                                                               |
| `leo/runtime/demos/institutional_approval_review`        |          4 | Confirmed tracked inventory | Not inferred from inventory                                                                               |
| `leo/runtime/demos/procurement_accounting_anomaly_audit` |          2 | Confirmed tracked inventory | Not inferred from inventory                                                                               |
| **CURRENT TOTAL**                                        |    **125** | **Confirmed**               | **No unsupported aggregate execution claim**                                                              |

Check:

`81 + 15 + 12 + 10 + 1 + 4 + 2 = 125`

### 5.1 Current scope interpretation

The 125-file current inventory is the principal test-file inventory
relevant to the active LEO runtime and demonstrations. It is not
equivalent to 125 individual tests: each Python test file can contain
multiple test functions, methods, parametrized cases, fixtures, or
collection structures.

For public reporting, the recommended wording is therefore:

> At the referenced canonical repository baseline, LEO contains 125
> tracked test files classified as current runtime or current
> demonstration test assets, within a repository-wide inventory of 198
> tracked test files. Test-file inventory is reported separately from
> collected and executed test-case counts.

------------------------------------------------------------------------

## 6. Process Mode test scope

**Tracked test files:** 15\
**Path class:** `CURRENT`\
**Canonical scope:** `leo/runtime/process_mode`

Process Mode is part of the active architectural and runtime track. The
test-file inventory is confirmed at the stated HEAD.

Historical project evidence includes focused and regression executions
from earlier Process Mode implementation checkpoints. Those historical
runs remain useful evidence, but this matrix does not transform them
into a claim that all current Process Mode tests were freshly executed
at HEAD `8b6a6e3d`.

Relevant architectural controls that test interpretation must preserve
include:

-   deterministic, stochastic, mixed, and unknown/review-required
    Process Mode semantics;
-   human review requirement;
-   no autonomous enforcement;
-   evidence-derived characteristic handling;
-   separation of signal-eligible and non-signal characteristics;
-   preservation of distinct unsupported, unobserved, unknown, and
    conflicting evidence states.

**Matrix status:** inventory confirmed; execution evidence must be
linked to specific run/baseline when updated.

------------------------------------------------------------------------

## 7. Anomaly Library test scope

**Tracked test files:** 12\
**Path class:** `CURRENT`\
**Canonical scope:** `leo/runtime/anomaly_library`

Earlier controlled development established successful focused Anomaly
Library runtime verification at earlier checkpoints. Those results form
historical execution evidence. They do not by themselves establish a
fresh pass at the present matrix HEAD.

The Anomaly Library validation model must continue to preserve:

-   evidence lineage;
-   provenance;
-   human review;
-   no autonomous fraud verdict;
-   no autonomous enforcement;
-   distinction between anomaly indication and adjudicative conclusion.

**Matrix status:** inventory confirmed; historical execution evidence
retained; current-baseline blanket pass not asserted.

------------------------------------------------------------------------

## 8. Knowledge Layer test scope

**Tracked test files:** 10\
**Path class:** `CURRENT`\
**Canonical scope:** `leo/runtime/knowledge_layer`

The Knowledge Layer has prior focused validation evidence from its
implementation sequence. The current inventory confirms the presence of
ten tracked test files in this scope.

The validation boundary includes, where applicable:

-   integration records;
-   reference resolution;
-   evidence lineage validation;
-   provenance validation;
-   deterministic read-only validation behavior;
-   prohibition on unauthorized external inference or decision-making.

**Matrix status:** inventory confirmed; historical execution evidence
must remain revision-specific.

------------------------------------------------------------------------

## 9. Core current runtime test scope

**Tracked test files:** 81\
**Path class:** `CURRENT`\
**Canonical scope:** `leo/runtime/tests`

This is the largest current canonical test-file group.

The inventory proves that 81 matching tracked test files exist under
this scope at the matrix baseline. The inventory alone does not
establish the number of collected test cases inside these files and does
not establish a fresh pass result.

This scope should be a primary target of the later controlled
current-baseline collection/execution verification because it materially
affects any repository-wide public test-count claim.

**Matrix status:** inventory confirmed; current test-case collection and
execution evidence pending future authorized verification.

------------------------------------------------------------------------

## 10. Current demonstration test scopes

### 10.1 Grant Expense Review

-   Path: `leo/runtime/demos/grant_expense_review`
-   Tracked test files: **1**
-   Class: `CURRENT`
-   Inventory: confirmed

### 10.2 Institutional Approval Review

-   Path: `leo/runtime/demos/institutional_approval_review`
-   Tracked test files: **4**
-   Class: `CURRENT`
-   Inventory: confirmed

### 10.3 Procurement Accounting Anomaly Audit

-   Path: `leo/runtime/demos/procurement_accounting_anomaly_audit`
-   Tracked test files: **2**
-   Class: `CURRENT`
-   Inventory: confirmed

### 10.4 Demonstration subtotal

`1 + 4 + 2 = 7 current demonstration test files`

These demonstration files are part of the 125-file CURRENT total. They
must not be added again when calculating a current canonical total.

------------------------------------------------------------------------

## 11. Legacy or historical runtime inventory

**Tracked test files:** 62\
**Class:** `LEGACY_OR_HISTORICAL`\
**Scope:** `tests_runtime`

These files remain important evidence of LEO's development history and
should not be deleted or hidden merely because they are not classified
as the current runtime test scope.

The recovered tracked paths are:

|  \# | Historical test file                                   |
|----:|:-------------------------------------------------------|
|   1 | `tests_runtime/manual_test.py`                         |
|   2 | `tests_runtime/test_anchor_recovery.py`                |
|   3 | `tests_runtime/test_anomaly_engine.py`                 |
|   4 | `tests_runtime/test_anomaly_memory.py`                 |
|   5 | `tests_runtime/test_anomaly_pattern_engine.py`         |
|   6 | `tests_runtime/test_archive_manager.py`                |
|   7 | `tests_runtime/test_case_engine.py`                    |
|   8 | `tests_runtime/test_case_escalation_engine.py`         |
|   9 | `tests_runtime/test_case_evidence.py`                  |
|  10 | `tests_runtime/test_case_trigger.py`                   |
|  11 | `tests_runtime/test_consensus_engine.py`               |
|  12 | `tests_runtime/test_consensus_logger.py`               |
|  13 | `tests_runtime/test_contradiction_engine.py`           |
|  14 | `tests_runtime/test_core_handshake.py`                 |
|  15 | `tests_runtime/test_core_identity.py`                  |
|  16 | `tests_runtime/test_core_registry.py`                  |
|  17 | `tests_runtime/test_core_sync_engine.py`               |
|  18 | `tests_runtime/test_corruption_cluster_engine.py`      |
|  19 | `tests_runtime/test_cross_anchor.py`                   |
|  20 | `tests_runtime/test_cross_domain_engine.py`            |
|  21 | `tests_runtime/test_domain_core_registry.py`           |
|  22 | `tests_runtime/test_domain_interaction_engine.py`      |
|  23 | `tests_runtime/test_epistemic_audit_logger.py`         |
|  24 | `tests_runtime/test_epistemic_classifier.py`           |
|  25 | `tests_runtime/test_epistemic_graph.py`                |
|  26 | `tests_runtime/test_epistemic_ingestion.py`            |
|  27 | `tests_runtime/test_evidence_graph_builder.py`         |
|  28 | `tests_runtime/test_fork_detector.py`                  |
|  29 | `tests_runtime/test_graph_influence_engine.py`         |
|  30 | `tests_runtime/test_graph_propagation.py`              |
|  31 | `tests_runtime/test_institution_response_tracker.py`   |
|  32 | `tests_runtime/test_institution_routing_engine.py`     |
|  33 | `tests_runtime/test_institutional_alert_engine.py`     |
|  34 | `tests_runtime/test_investigation_report_generator.py` |
|  35 | `tests_runtime/test_investigation_timeline_engine.py`  |
|  36 | `tests_runtime/test_leo_full_system_pipeline.py`       |
|  37 | `tests_runtime/test_leo_system_chronicle.py`           |
|  38 | `tests_runtime/test_multicore.py`                      |
|  39 | `tests_runtime/test_node_rebuild.py`                   |
|  40 | `tests_runtime/test_octopus_network.py`                |
|  41 | `tests_runtime/test_octopus_network_full.py`           |
|  42 | `tests_runtime/test_pattern_detection.py`              |
|  43 | `tests_runtime/test_pattern_engine.py`                 |
|  44 | `tests_runtime/test_pattern_library.py`                |
|  45 | `tests_runtime/test_reconstruction.py`                 |
|  46 | `tests_runtime/test_recovery_commit.py`                |
|  47 | `tests_runtime/test_recovery_verifier.py`              |
|  48 | `tests_runtime/test_resolution_engine.py`              |
|  49 | `tests_runtime/test_response_engine.py`                |
|  50 | `tests_runtime/test_risk_engine.py`                    |
|  51 | `tests_runtime/test_risk_escalation_engine.py`         |
|  52 | `tests_runtime/test_signal_engine.py`                  |
|  53 | `tests_runtime/test_state_broadcast.py`                |
|  54 | `tests_runtime/test_state_canonizer.py`                |
|  55 | `tests_runtime/test_state_commit.py`                   |
|  56 | `tests_runtime/test_state_consensus.py`                |
|  57 | `tests_runtime/test_state_verifier.py`                 |
|  58 | `tests_runtime/test_systemic_risk_engine.py`           |
|  59 | `tests_runtime/test_temporal_anomaly.py`               |
|  60 | `tests_runtime/test_topology.py`                       |
|  61 | `tests_runtime/test_topology_commit.py`                |
|  62 | `tests_runtime/test_truth_pipeline.py`                 |

### 11.1 Historical classification rule

These 62 files may support historical architecture, regression history,
or capability provenance. They are not to be silently represented as 62
current-runtime test files.

Conversely, their historical classification does not mean that they are
valueless or obsolete. The archive is part of LEO's institutional memory
and provenance chain.

------------------------------------------------------------------------

## 12. Other canonical test asset

**Path:** `leo/tests/integration/test_runtime_v02.py`\
**Tracked test files:** 1\
**Class:** `OTHER_CANONICAL`

This file is canonical but outside the principal `leo/runtime/...`
current grouping used by the normalized inventory.

It remains separately visible to prevent either accidental omission or
accidental inclusion in the 125 CURRENT subtotal.

------------------------------------------------------------------------

## 13. Epistemic ingestion test asset

**Path:** `leo/runtime/epistemic/ingestion_v1/test_ingestion_v1.py`\
**Tracked test files:** 1

The initial normalization placed this path into:

`UNCLASSIFIED|other`

A subsequent recovery step identified its exact canonical location.

For provenance, this matrix preserves both facts:

1.  the initial normalized output classified one file as unclassified;
2.  the file was subsequently identified as the epistemic ingestion
    test.

Future matrix revisions may assign a formal durable class to this scope,
but that reclassification should be explicit rather than silently
rewriting the original inventory evidence.

------------------------------------------------------------------------

## 14. Auxiliary test asset

**Path:** `tools/audit/runtime_smoke_test.py`\
**Tracked test files:** 1\
**Class:** `AUXILIARY`

This is an audit/smoke-test utility and is not included in the 125
CURRENT runtime/demo subtotal.

Its presence is nevertheless part of the complete 198-file tracked
inventory.

------------------------------------------------------------------------

## 15. Publication-copy inventory

Publication copies must be visible for reproducibility and public
evaluation, but must not inflate the canonical test inventory by double
counting copies.

### 15.1 Public MVP release

-   Scope: `leo-public-mvp-release`
-   Tracked test files: **4**
-   Class: `PUBLICATION_COPY`

### 15.2 Repository publication staging

-   Scope: `repository_publication_staging`
-   Tracked test files: **4**
-   Class: `PUBLICATION_COPY`

### 15.3 Publication-copy subtotal

`4 + 4 = 8 publication-copy test files`

These eight files are included in the repository-wide 198 tracked
test-file count because they are tracked matching paths. They are not to
be presented as eight additional independent canonical runtime tests.

------------------------------------------------------------------------

## 16. Canonical inventory reconciliation

The repository-wide count reconciles exactly:

| Component                                  |   Files |
|:-------------------------------------------|--------:|
| Current runtime and demos                  |     125 |
| Legacy/historical runtime                  |      62 |
| Publication copies                         |       8 |
| Other canonical                            |       1 |
| Auxiliary                                  |       1 |
| Initially unclassified epistemic ingestion |       1 |
| **Repository-wide total**                  | **198** |

Arithmetic:

`125 + 62 + 8 + 1 + 1 + 1 = 198`

No missing file is required to reconcile the inventory.

------------------------------------------------------------------------

## 17. Why 198 is not the public "number of tests"

The number 198 describes **tracked test files matching the inventory
naming rule**.

It must not be compared directly with numbers such as `2403` or `2451`
as though all three numbers measured the same thing.

A pytest collection can generate many individual test cases from a
smaller number of files. Parametrization can further increase the number
of collected cases. Therefore:

-   198 may be a file count;
-   2403 may refer to a historical executed/collected test-case count at
    a particular checkpoint;
-   2451 may refer to a later website/public claim or later test-case
    baseline;
-   these values require provenance before they can be reconciled.

The matrix therefore prohibits the statement:

`198 tests vs 2451 tests`

unless "tests" is first defined consistently for both values.

The technically correct comparison is:

`tracked test files` versus `collected test cases` versus
`executed test cases` versus `passed test cases`.

------------------------------------------------------------------------

## 18. The 2403 figure

Project history contains a prior runtime baseline associated with **2403
passed tests** at an earlier checkpoint.

That evidence is historical unless the exact run output, revision,
command, environment, and scope are linked to a current verification
record.

Accordingly:

| Claim                                                                     | Matrix treatment                                                               |
|:--------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| “LEO historically reached a verified 2403-test passing runtime baseline.” | Permissible when linked to the historical evidence/checkpoint.                 |
| “2403 tests pass now at HEAD 8b6a6e3d.”                                   | Not established by the current inventory.                                      |
| “There are 2403 test files.”                                              | False relative to the current tracked-file inventory.                          |
| “2403 and 198 conflict.”                                                  | Not established; they measure different units unless evidence shows otherwise. |

The historical 2403 result should remain part of LEO's evidence history
and should not be discarded merely because the repository has evolved.

------------------------------------------------------------------------

## 19. The 2451 figure

A public/site figure of **2451 tests** has been identified as requiring
reconciliation.

At the present evidence boundary, this matrix does **not** assert what
exact command, revision, scope, or execution produced 2451.

Therefore the status is:

`PUBLIC_CLAIM_REQUIRES_PROVENANCE_RECONCILIATION`

This does not mean that 2451 is necessarily wrong. It means that a
reviewer-facing matrix should not invent its derivation.

Before the public figure is reaffirmed or changed, the later controlled
verification should establish:

1.  the exact source of the 2451 figure;
2.  whether it represents collected, executed, or passed test cases;
3.  the repository revision to which it applies;
4.  included and excluded directories;
5.  whether publication copies were excluded;
6.  whether legacy tests were included;
7.  whether test parametrization affected the count;
8.  whether collection warnings/errors occurred;
9.  the execution exit code if execution was performed.

Until that reconciliation is complete, the inventory and the public
count must remain separately labeled.

------------------------------------------------------------------------

## 20. Collection inventory versus execution

A key evidence boundary is preserved here:

**The recovered inventory proves collection/inventory structure, not
execution of all test cases.**

Where an earlier controlled step performed collection only, the matrix
must say collection was performed. It must not be upgraded to execution
evidence.

Where test execution was not authorized, no inference of execution is
allowed.

This distinction is especially important for external technical review
because it makes the evidence stronger, not weaker: the reviewer can see
precisely what has and has not been established.

------------------------------------------------------------------------

## 21. Historical execution evidence register

The following categories of historical evidence are known from the
controlled LEO development record and should be linked to exact
logs/checkpoints when the evidence register is expanded.

| Area                                   | Historical evidence status                                                                                  | Current matrix interpretation                               |
|:---------------------------------------|:------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------|
| Core runtime earlier stable baseline   | Historical passing evidence exists, including the 2403 figure at an earlier baseline                        | Preserve as historical; do not relabel as fresh current run |
| Process Mode first runtime prototype   | Historical focused passing evidence exists                                                                  | Revision-specific evidence                                  |
| Process Mode projection implementation | Historical focused tests and Process Mode regression were reported passing at the implementation checkpoint | Revision-specific evidence                                  |
| Anomaly Library runtime                | Historical focused runtime suite passing evidence exists                                                    | Revision-specific evidence                                  |
| Knowledge Layer components             | Historical focused validation evidence exists                                                               | Revision-specific evidence                                  |
| Public demonstrations                  | Historical focused demo verification exists for earlier public-evaluation checkpoints                       | Revision-specific evidence                                  |

This register intentionally avoids inventing exact totals where the
current evidence excerpt does not provide enough information to support
them.

------------------------------------------------------------------------

## 22. Validation status vocabulary

Every future matrix row should use one or more of the following
controlled statuses.

### `INVENTORY_CONFIRMED`

The file/path/count is confirmed in the tracked repository inventory.

### `COLLECTED_CURRENT_BASELINE`

A controlled test-runner collection was performed at the matrix/current
baseline and completed with recorded evidence.

### `EXECUTED_CURRENT_BASELINE`

A controlled execution was performed at the current baseline.

### `PASSED_CURRENT_BASELINE`

A controlled execution at the current baseline completed with the stated
passing result.

### `HISTORICAL_PASS_EVIDENCE`

A prior controlled passing result exists for an earlier
revision/checkpoint.

### `PENDING_CURRENT_EXECUTION`

The test asset is known, but no fresh current-baseline execution is
asserted.

### `PUBLICATION_COPY`

The file is a publication/release copy and is not an independent
canonical test asset.

### `REQUIRES_PROVENANCE_RECONCILIATION`

A claim/count exists but its exact derivation must be recovered before
it is used as a current verified claim.

------------------------------------------------------------------------

## 23. Reviewer-facing matrix

| Scope                                       | Class                  | Files | Inventory            | Historical execution evidence        | Fresh current-baseline aggregate pass asserted? |
|:--------------------------------------------|:-----------------------|------:|:---------------------|:-------------------------------------|:------------------------------------------------|
| `leo/runtime/tests`                         | CURRENT                |    81 | Confirmed            | Earlier system-level evidence exists | No                                              |
| `leo/runtime/process_mode`                  | CURRENT                |    15 | Confirmed            | Yes, checkpoint-specific             | No blanket claim                                |
| `leo/runtime/anomaly_library`               | CURRENT                |    12 | Confirmed            | Yes, checkpoint-specific             | No                                              |
| `leo/runtime/knowledge_layer`               | CURRENT                |    10 | Confirmed            | Yes, checkpoint-specific             | No                                              |
| Grant Expense Review demo                   | CURRENT                |     1 | Confirmed            | Historical demo evidence             | No blanket claim                                |
| Institutional Approval Review demo          | CURRENT                |     4 | Confirmed            | Historical demo evidence             | No blanket claim                                |
| Procurement Accounting Anomaly Audit demo   | CURRENT                |     2 | Confirmed            | Historical demo evidence             | No blanket claim                                |
| `tests_runtime`                             | LEGACY_OR_HISTORICAL   |    62 | Confirmed            | Historical role                      | No                                              |
| `leo/tests/integration/test_runtime_v02.py` | OTHER_CANONICAL        |     1 | Confirmed            | Not asserted here                    | No                                              |
| Epistemic ingestion v1                      | Initially UNCLASSIFIED |     1 | Confirmed exact path | Not asserted here                    | No                                              |
| `tools/audit/runtime_smoke_test.py`         | AUXILIARY              |     1 | Confirmed            | Not asserted here                    | No                                              |
| `leo-public-mvp-release`                    | PUBLICATION_COPY       |     4 | Confirmed            | Copy-specific                        | Not counted as independent canonical            |
| `repository_publication_staging`            | PUBLICATION_COPY       |     4 | Confirmed            | Copy-specific                        | Not counted as independent canonical            |

------------------------------------------------------------------------

## 24. Public reporting recommendations

For GitHub and the public site, the strongest defensible presentation is
not a single unexplained test number.

A reviewer should be able to see:

-   the current tracked test-file inventory;
-   the breakdown by subsystem;
-   the distinction between current and historical test assets;
-   the distinction between canonical tests and publication copies;
-   the latest verified collected test-case count;
-   the latest verified executed/passed count;
-   the revision and date associated with every execution count;
-   any pending reconciliation.

Recommended public summary structure:

**Test architecture** - 198 tracked test files repository-wide at the
stated inventory baseline. - 125 classified as current runtime/demo test
files. - 62 retained as legacy/historical runtime test assets. - 8
publication-copy test files, not double-counted as independent canonical
assets. - 3 additional separately classified assets: other canonical,
epistemic ingestion, and auxiliary audit/smoke.

**Execution evidence** - Historical passing baselines are retained with
revision-specific provenance. - A fresh current-baseline aggregate pass
count is published only after controlled execution. - The public 2451
figure remains subject to explicit provenance reconciliation unless its
supporting run is recovered.

------------------------------------------------------------------------

## 25. What must not be claimed

Until supporting evidence is attached, public or reviewer-facing
material must not claim:

-   that all 198 tracked test files were freshly executed at HEAD
    `8b6a6e3d`;
-   that 198 is the number of pytest test cases;
-   that 2451 is currently verified merely because it appears on a
    website;
-   that 2403 and 2451 are directly comparable without matching scope
    and semantics;
-   that publication-copy files are additional independent canonical
    tests;
-   that legacy tests are current runtime tests;
-   that historical successful runs automatically validate later code
    revisions;
-   that passing tests constitute autonomous certification, legal
    compliance, fraud adjudication, or institutional enforcement.

------------------------------------------------------------------------

## 26. Human review and institutional boundary

The test matrix is evidence for technical review. It is not an
autonomous decision instrument.

LEO's governing boundary remains:

-   human review required;
-   no autonomous enforcement;
-   no autonomous fraud verdict;
-   no production mutation without explicit authorization;
-   evidence lineage and provenance preserved;
-   archive and historical evidence retained as institutional memory.

A test result can support a technical assessment. It does not replace
institutional judgment or legal review.

------------------------------------------------------------------------

## 27. Provenance requirements for every future execution

Every future aggregate test run entered into this matrix should record
at least:

| Field                             | Required            |
|:----------------------------------|:--------------------|
| Date/time                         | Yes                 |
| Git full HEAD                     | Yes                 |
| Branch                            | Yes                 |
| Working-tree tracked-change state | Yes                 |
| Staged-file state                 | Yes                 |
| Exact command                     | Yes                 |
| Test runner/version               | Yes                 |
| Python/runtime version            | Yes                 |
| Scope/include paths               | Yes                 |
| Explicit exclusions               | Yes                 |
| Collected count                   | Yes, when available |
| Executed count                    | Yes                 |
| Passed count                      | Yes                 |
| Failed count                      | Yes                 |
| Skipped count                     | Yes                 |
| XFailed/XPassed count             | When applicable     |
| Warnings                          | When applicable     |
| Exit code                         | Yes                 |
| Generated-output side effects     | Yes                 |
| Restoration action, if authorized | When applicable     |
| Log/evidence path                 | Yes                 |
  Human reviewer                      Recommended

This prevents future loss of control over the meaning of a test number.

------------------------------------------------------------------------

## 28. Generated-output side-effect control

A recent controlled test-related workflow demonstrated why execution
provenance must include generated-output handling.

Four tracked JSON demo outputs were observed with changes limited to
`generated_at` timestamps:

-   `leo/runtime/demos/grant_expense_review/output/grant_expense_evidence_report.json`
-   `leo/runtime/demos/grant_expense_review/output/grant_expense_input_quality_report.json`
-   `leo/runtime/demos/procurement_accounting_anomaly_audit/output/demo_evidence_report.json`
-   `leo/runtime/demos/procurement_accounting_anomaly_audit/output/input_quality_report.json`

The controlled classification established:

-   tracked changed files before restore: 4;
-   generated-at changed lines: 8;
-   non-generated-at content changes: 0;
-   timestamp-only classification: pass;
-   exact four-file restore: authorized and performed;
-   restore exit code: 0;
-   tracked changes after restore: 0;
-   staged files after restore: 0;
-   HEAD unchanged;
-   controlled restore: pass.

This is evidence of a test-execution side effect, not evidence that the
generated report contents changed substantively.

Future test runs should record such side effects explicitly.

------------------------------------------------------------------------

## 29. Maintenance protocol

This file is a living matrix.

It should be updated when any of the following occurs:

1.  a new canonical test file is added;
2.  a test file is retired or moved;
3.  a subsystem changes classification;
4.  a new current-baseline collection is performed;
5.  a new controlled test execution is performed;
6.  the public test count changes;
7.  a publication package is refreshed;
8.  historical evidence is recovered;
9.  a discrepancy is resolved;
10. a new LEO subsystem enters the runtime test architecture.

Updates should preserve previous evidence rather than silently replacing
historical states.

------------------------------------------------------------------------

## 30. Update sequence

The preferred controlled update sequence is:

1.  verify expected HEAD;
2.  verify tracked and staged state;
3.  perform read-only test-file inventory;
4.  compare with the previous matrix baseline;
5.  classify additions/removals/moves;
6.  if authorized, perform collection;
7.  inspect collection output;
8.  if separately authorized, perform execution;
9.  inspect execution output;
10. classify generated-output side effects;
11. restore only explicitly authorized generated changes where
    appropriate;
12. verify repository state;
13. update this matrix;
14. review the matrix diff;
15. stage only this matrix;
16. commit only after explicit approval;
17. update public GitHub/site representations only from verified matrix
    facts.

------------------------------------------------------------------------

## 31. Future detailed per-suite expansion

The current matrix establishes the repository-level grouping and
evidence semantics.

The next evidence-enrichment cycle may add a per-file/per-suite register
for the 125 current files containing:

-   exact file path;
-   subsystem;
-   test purpose;
-   test class/category;
-   collected case count;
-   last verified execution revision;
-   last verified pass count;
-   last execution date;
-   evidence/log reference;
-   current status;
-   public relevance.

That enrichment should be generated from repository evidence, not
manually guessed.

The matrix structure is intentionally designed so that this enrichment
can be added without replacing the present document.

------------------------------------------------------------------------

## 32. Commission / AI Office evaluation value

For an external technical evaluator, the matrix demonstrates more than a
raw test count.

It demonstrates that LEO distinguishes:

-   code inventory from execution evidence;
-   current architecture from historical assets;
-   canonical tests from publication copies;
-   collection from execution;
-   execution from passing;
-   current verification from historical verification;
-   technical validation from institutional/legal judgment.

This distinction supports reproducibility and reduces the risk of an
inaccurate public claim.

------------------------------------------------------------------------

## 33. Current evidence conclusion

At canonical repository HEAD:

`8b6a6e3df2892e913321b0f06f8b330b686cc56e`

the controlled repository inventory establishes:

-   **198 tracked test files repository-wide**;
-   **125 CURRENT runtime/demo test files**;
-   **62 LEGACY_OR_HISTORICAL test files**;
-   **8 PUBLICATION_COPY test files**;
-   **1 OTHER_CANONICAL test file**;
-   **1 AUXILIARY test file**;
-   **1 initially unclassified file, subsequently identified as the
    epistemic ingestion v1 test**.

The 125 current files break down as:

-   `leo/runtime/tests`: **81**
-   `leo/runtime/process_mode`: **15**
-   `leo/runtime/anomaly_library`: **12**
-   `leo/runtime/knowledge_layer`: **10**
-   Grant Expense Review demo: **1**
-   Institutional Approval Review demo: **4**
-   Procurement Accounting Anomaly Audit demo: **2**

Total:

`81 + 15 + 12 + 10 + 1 + 4 + 2 = 125`

Repository-wide reconciliation:

`125 + 62 + 8 + 1 + 1 + 1 = 198`

These are **test-file inventory facts**, not a claim that 198 tests or
all test cases were freshly executed.

Historical passing evidence, including the earlier 2403-test baseline,
remains part of LEO's evidence history. The public/site figure of 2451
requires explicit provenance reconciliation before this matrix can
represent it as a current verified execution result.

------------------------------------------------------------------------

## 34. Current matrix status

**TRACKED_TEST_FILE_INVENTORY:** CONFIRMED\
**CURRENT_TEST_FILE_CLASSIFICATION:** CONFIRMED\
**LEGACY/HISTORICAL_FILE_INVENTORY:** CONFIRMED\
**PUBLICATION_COPY_COUNT:** CONFIRMED\
**CURRENT_BASELINE_FULL_COLLECTION:** NOT CLAIMED BY THIS INVENTORY\
**CURRENT_BASELINE_FULL_EXECUTION:** NOT CLAIMED\
**CURRENT_BASELINE_FULL_PASS:** NOT CLAIMED\
**HISTORICAL_EXECUTION_EVIDENCE:** PRESERVED, REVISION-SPECIFIC\
**2403 FIGURE:** HISTORICAL BASELINE; CURRENT RE-EXECUTION NOT INFERRED\
**2451 FIGURE:** REQUIRES PROVENANCE RECONCILIATION\
**HUMAN REVIEW:** REQUIRED\
**AUTONOMOUS ENFORCEMENT:** NOT AUTHORIZED\
**PRODUCTION MUTATION:** NOT AUTHORIZED BY THIS DOCUMENT

------------------------------------------------------------------------

## 35. Next controlled evidence step

The next test-specific step should not restart the inventory.

The inventory is now a stable baseline.

When time and authorization permit, the next controlled technical step
is to recover or perform a **current canonical pytest collection with
explicit scope**, record the exact collected-case count and provenance,
and reconcile it against the historical `2403` and public `2451`
figures.

Only after collection evidence is understood should a repository-wide
execution be authorized.

This preserves the work already completed and prevents repeated
reconstruction of the test landscape.

------------------------------------------------------------------------

## 36. Final declaration

This matrix is the maintained evidence index for LEO test validation.

Its purpose is not to maximize a headline number. Its purpose is to make
every test-related statement traceable to its scope, repository
revision, evidence type, and verification status.

Where evidence is complete, the matrix states the result.

Where only inventory is proven, it states inventory.

Where historical execution evidence exists, it remains historical and
revision-specific.

Where provenance is missing, the matrix records the gap rather than
inventing a conclusion.

That evidence discipline is part of LEO's institutional integrity model.
