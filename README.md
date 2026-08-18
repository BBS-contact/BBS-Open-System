# LEO — Human-Controlled Institutional Integrity System

Developed by **Fundacja BBS — Better Balance System**
Jurisdiction: Poland (European Union)
Legal form: Registered non-profit research foundation

LEO is a human-controlled institutional integrity, provenance, evidence review, process characterization, anomaly analysis, and reviewed knowledge system.

The project is under active architectural and engineering development and controlled public evaluation preparation.

**Human review is required.**

LEO does not autonomously enforce institutional outcomes, issue authoritative fraud or legal verdicts, mutate production systems, or treat machine-generated interpretation as self-validating institutional truth.

---

# Overview

LEO is designed to support institutions and human reviewers working with complex evidence, processes, anomalies, and institutional knowledge.

Its architecture emphasizes:

* source-evidence preservation;
* provenance and evidence lineage;
* evidence-derived characteristics;
* controlled signal eligibility;
* deterministic and stochastic process signals;
* Process Mode proposals;
* anomaly analysis;
* reviewed anomaly memory;
* Reviewed / Institutional Knowledge;
* reviewer support;
* explicit human authority boundaries;
* reproducible and controlled runtime evidence.

LEO is not designed as an autonomous institutional authority.

Its analytical outputs are intended to support review rather than replace the people or institutions responsible for authoritative decisions.

The current architecture deliberately distinguishes evidence from knowledge, analytical signals from decisions, and technical capability from institutional authority.

---

# Core Architectural Model

The current canonical LEO interpretation pipeline is:

```text
SOURCE EVIDENCE
    ->
EVIDENCE-DERIVED CHARACTERISTICS
    ->
SIGNAL ELIGIBILITY
    ->
DETERMINISTIC / STOCHASTIC SIGNAL COUNTS
    ->
PROCESS MODE PROPOSAL
    ->
HUMAN REVIEW
```

This sequence is controlled.

Source evidence does not automatically become institutional truth.

Evidence-derived characteristics are reviewable interpretations tied to evidence and provenance.

Signal eligibility determines whether a supported characteristic may contribute positively to a deterministic or stochastic process signal.

Signal counts are analytical inputs.

Process Mode is a system proposal.

Authoritative institutional action remains subject to human review and separate authorization.

---

# Evidence, Provenance and Evidence Lineage

Evidence lineage is a foundational LEO requirement.

The architecture is intended to preserve traceability across relationships such as:

```text
SOURCE MATERIAL
    ->
EVIDENCE
    ->
EVIDENCE-DERIVED CHARACTERISTIC
    ->
CHARACTERISTIC STATE
    ->
SIGNAL ELIGIBILITY
    ->
SIGNAL CONTRIBUTION
    ->
PROCESS MODE PROPOSAL
    ->
HUMAN REVIEW
```

Downstream analytical information should remain traceable to the evidence from which it originated.

LEO therefore does not intentionally collapse source evidence, derived interpretation, analytical output, reviewed knowledge, and human decisions into one undifferentiated machine conclusion.

Evidence states must also preserve uncertainty.

The current evidence-derived characteristic model distinguishes:

* `SUPPORTED`;
* `NOT_SUPPORTED`;
* `NOT_OBSERVED`;
* `UNKNOWN`;
* `CONFLICTING`.

Only signal-eligible `SUPPORTED` characteristics may contribute positive deterministic or stochastic signals.

`NOT_SUPPORTED`, `NOT_OBSERVED`, `UNKNOWN`, and `CONFLICTING` remain distinct states.

They must not automatically create a positive signal or an opposite signal.

Absence of support is therefore not automatically treated as evidence of the opposite proposition.

---

# Process Mode

LEO uses Process Mode to characterize the operational nature of a reviewed process before downstream anomaly interpretation.

The canonical Process Mode states are:

* `DETERMINISTIC_PROCESS`
* `STOCHASTIC_PROCESS`
* `MIXED_PROCESS`
* `UNKNOWN_REQUIRES_REVIEW`

A deterministic process is associated with characteristics such as stable rules, procedural control, outcome predictability, and repeatability.

A stochastic process may involve characteristics such as human discretion, behavioral variability, and response uncertainty.

A mixed process contains meaningful deterministic and stochastic characteristics.

`UNKNOWN_REQUIRES_REVIEW` preserves uncertainty where available evidence does not support an adequate process-mode proposal.

Process Mode does not determine whether conduct is fraudulent, lawful, compliant, legitimate, correct, or incorrect.

It provides structured context for subsequent human review and anomaly interpretation.

---

# Evidence-Derived Characteristics and Signal Eligibility

LEO separates evidence interpretation from signal generation.

Examples of deterministic-signal characteristics include:

* rule stability;
* procedural control;
* outcome predictability;
* repeatability.

Examples of stochastic-signal characteristics include:

* human discretion;
* behavioral variability;
* response uncertainty.

Not every evidence-derived characteristic is automatically a process signal.

A characteristic must satisfy the applicable signal-eligibility rules before it can contribute positively to deterministic or stochastic signal counts.

This architectural separation is intended to reduce overconfident interpretation of incomplete, conflicting, unsupported, or otherwise ambiguous evidence.

The controlled relationship is:

```text
EVIDENCE
    ->
EVIDENCE-DERIVED CHARACTERISTIC
    ->
CHARACTERISTIC STATE
    ->
SIGNAL ELIGIBILITY
    ->
SIGNAL CONTRIBUTION
```

rather than:

```text
EVIDENCE
    ->
AUTOMATIC CONCLUSION
```

---

# Human Review and Institutional Authority

Human review is a mandatory architectural boundary.

LEO may assist reviewers by:

* organizing evidence;
* preserving provenance;
* presenting evidence lineage;
* deriving reviewable characteristics;
* applying defined signal-eligibility rules;
* calculating deterministic and stochastic signal counts;
* proposing Process Mode;
* structuring anomaly evidence;
* presenting reviewed anomaly context;
* retrieving relevant Reviewed / Institutional Knowledge;
* preserving review and correction history;
* supporting controlled comparison against reviewed precedents.

These capabilities do not transfer institutional authority to the system.

LEO does not autonomously convert analytical output into sanctions, restrictions, approvals, rejections, punishments, fraud findings, legal findings, or production-changing actions.

The governing separation is:

```text
ANALYSIS
    ->
PROPOSAL / REVIEW SUPPORT
    ->
HUMAN REVIEW
    ->
AUTHORIZATION
    ->
INSTITUTIONAL ACTION
```

Technical capability and institutional authority are different concepts.

---

# Governance Boundaries

The current LEO architecture operates under explicit governance boundaries.

## No Autonomous Enforcement

LEO is not authorized to autonomously enforce institutional outcomes.

Analytical findings, anomaly records, Process Mode proposals, or knowledge retrieval must not automatically become sanctions, restrictions, approvals, rejections, suspensions, or other consequential institutional actions.

## No Autonomous Learning of Institutional Truth

LEO does not treat raw documents or unreviewed machine output as self-validating institutional knowledge.

The governing principle is:

```text
Documents are evidence.
Human-confirmed classifications are knowledge.
```

Reviewed knowledge is accumulated through controlled review with preserved provenance and correction history.

## No Fraud Verdict Authority

An anomaly, inconsistency, unusual pattern, missing record, contradictory evidence, or elevated review condition does not independently establish fraud.

LEO does not issue authoritative fraud verdicts.

## No Legal Verdict Authority

LEO does not independently determine legal liability, regulatory violation, legal guilt, or other authoritative legal conclusions.

Appropriately authorized human and institutional review remains required.

## No Production Mutation

A functioning runtime, completed demonstration, passing test suite, frozen baseline, or public evaluation artifact does not independently authorize production mutation.

Production deployment and production-changing actions require separate explicit authorization.

## No Unsupported Regulatory Claims

Governance controls, provenance mechanisms, human review, traceability, or audit-oriented architecture do not by themselves establish regulatory compliance.

This repository should not be interpreted as asserting independently verified GDPR, EU AI Act, or other regulatory compliance unless such a claim is separately supported by appropriate reviewed legal and technical evidence.

---

# Anomaly Analysis and Anomaly Library

LEO treats anomalies as review objects rather than automatic accusations.

An anomaly may arise from many causes, including:

* legitimate procedural variation;
* incomplete information;
* data-quality problems;
* inconsistent documentation;
* process deviation;
* exceptional circumstances;
* human error;
* system error;
* conflicting evidence;
* unexplained behavior requiring additional review.

An anomaly is therefore not synonymous with fraud, wrongdoing, illegality, or institutional failure.

The Anomaly Library is intended to preserve reviewed anomaly knowledge together with relevant evidence, provenance, Process Mode context, reviewer interpretation, correction history, and review outcomes.

Its intended relationship is:

```text
REVIEWED ANOMALY
    ->
PRESERVED EVIDENCE LINEAGE
    ->
HUMAN INTERPRETATION
    ->
REVIEW OUTCOME
    ->
INSTITUTIONAL MEMORY
    ->
FUTURE REVIEWER SUPPORT
```

It is not intended to implement:

```text
DETECTED ANOMALY
    ->
AUTOMATIC ACCUSATION
    ->
AUTOMATIC ENFORCEMENT
```

Historical anomaly interpretations should remain traceable when later evidence changes their meaning.

Corrections should preserve prior state, supporting evidence, review context, and correction history rather than silently rewriting institutional memory.

---

# Reviewed / Institutional Knowledge

LEO distinguishes evidence from Reviewed / Institutional Knowledge.

A document, record, transaction, report, dataset, message, or external source may constitute evidence.

It does not automatically become institutional knowledge merely because the system ingested or processed it.

Reviewed knowledge is intended to emerge through a controlled progression:

```text
SOURCE EVIDENCE
    ->
REVIEWABLE INTERPRETATION
    ->
HUMAN REVIEW
    ->
CONFIRMED / CORRECTED / REJECTED RESULT
    ->
PRESERVED REVIEW RECORD
    ->
REVIEWED INSTITUTIONAL KNOWLEDGE
```

Reviewed knowledge should preserve enough provenance to understand:

* which evidence supported it;
* which evidence-derived characteristics were relevant;
* which Process Mode context applied;
* what review authority confirmed or corrected it;
* whether uncertainty remained;
* whether later correction occurred;
* which previous interpretation it superseded;
* which reviewed anomalies or precedents were relevant;
* whether the record remains active, superseded, disputed, or under review.

This model is intended to allow institutional memory to evolve without losing its evidentiary history.

---

# Reviewer Support

LEO is designed to support human reviewers working with evidence, process context, anomalies, and reviewed institutional knowledge.

Reviewer-facing information may include:

* structured source evidence;
* provenance references;
* evidence lineage;
* evidence-derived characteristics;
* characteristic states;
* signal eligibility;
* deterministic and stochastic signal counts;
* Process Mode proposals;
* anomaly context;
* reviewed anomaly precedents;
* relevant Reviewed / Institutional Knowledge;
* unresolved evidence conflicts;
* missing or unobserved evidence;
* historical review context;
* correction lineage;
* reproducible runtime output where applicable.

A reviewer should be able to distinguish among:

```text id="5q3w21"
SOURCE FACT
DERIVED CHARACTERISTIC
SYSTEM-GENERATED SIGNAL
SYSTEM PROPOSAL
REVIEWED KNOWLEDGE
HUMAN DECISION
```

These categories should not be collapsed into a single machine-generated conclusion.

Where available evidence does not support an adequate interpretation, uncertainty should remain visible.

`UNKNOWN_REQUIRES_REVIEW` exists specifically to preserve an unresolved state instead of forcing every reviewed process into a confident classification.

---

# Current Development State

LEO remains under active architectural and engineering development.

The project has progressed substantially beyond its earlier public description and now includes a broader governance-centered architecture involving:

* evidence and provenance handling;
* evidence-derived characteristics;
* signal eligibility;
* Process Mode;
* anomaly analysis;
* reviewed anomaly memory;
* Reviewed / Institutional Knowledge;
* human-review support;
* controlled runtime baselines;
* public demonstrations;
* public evaluation infrastructure;
* architectural continuity;
* institutional and engineering memory preservation.

The project should not currently be characterized solely through an older phase or pilot-readiness label.

Earlier phase terminology remains part of the project's historical record where it appears in preserved artifacts.

The current public status is better described as:

```text id="wxrl0a"
ACTIVE ARCHITECTURAL AND ENGINEERING DEVELOPMENT
+
CONTROLLED PUBLIC EVALUATION PREPARATION
```

This status does not mean that every architectural layer has the same implementation maturity.

Some capabilities exist as controlled runtime baselines.

Some exist as reviewed architectural specifications or contracts.

Some are demonstrated through public evaluation artifacts.

Some remain under active development.

These categories should remain distinguishable.

For the more detailed current-state declaration, see:

### [LEO Project Status](./PROJECT_STATUS.md)

---

# Architecture, Runtime and Historical Evidence

LEO's repository contains materials from different stages of system development.

These should not be treated as though they all represent the same architectural period or implementation maturity.

Public evaluators should distinguish among:

## Current Governing Architecture

Architecture and governance materials defining the current evidence model, Process Mode, anomaly interpretation, reviewed knowledge, provenance requirements, human-review boundaries, and related architectural contracts.

## Current Runtime Evidence

Implemented and preserved runtime behavior within explicitly defined scopes.

## Public Evaluation Artifacts

Demonstrations, guides, documentation, outputs, and related materials organized to make selected LEO capabilities externally inspectable.

## Historical / Legacy Evidence

Earlier runtime components, terminology, design assumptions, demonstrations, and development phases retained as part of LEO's engineering provenance and institutional memory.

Historical evidence remains relevant.

It does not automatically override the current governing architecture.

Where current and historical terminology differ, the repository should make that distinction explicit rather than silently rewriting or deleting historical evidence.

---

# Controlled Runtime Baselines

LEO contains multiple runtime components, demonstrations, tests, and completed implementation baselines.

These are engineering evidence within their documented scope.

A completed runtime baseline does not automatically establish complete-system production readiness.

A runtime may also be frozen for reproducibility and change control without being authorized for production deployment.

Public evaluation should therefore distinguish:

* implemented behavior;
* tested behavior;
* demonstrated behavior;
* architectural requirements;
* frozen historical baselines;
* planned functionality;
* production-authorized functionality.

The terms are not interchangeable.

Where runtime evidence is provided, the intended relationship is generally:

```text id="gssmw9"
INPUT
    ->
PROCESSING
    ->
OUTPUT
    ->
VALIDATION
    ->
REVIEW
```

This allows evaluators to distinguish demonstrated behavior from broader architectural intent.

---

# Historical Test Evidence

Historical test results remain useful engineering and reproducibility evidence when they remain tied to their original scope.

A previously recorded result of:

```text id="pqdsom"
2451 passed in 56.87s
```

belongs to a historical Institutional Approval combined runtime baseline.

It is not presented here as the current global LEO test count.

A current global test-count claim would require a new appropriately scoped validation establishing that fact.

Historical test evidence should therefore remain associated with:

* the runtime baseline that produced it;
* the test scope that was executed;
* the relevant repository state where known;
* the context in which the result was recorded.

This preserves useful engineering evidence without converting a historical scoped result into an unsupported current repository-wide metric.

---

# Public Evaluation

LEO is being prepared for controlled public evaluation.

Public evaluation readiness means that an external evaluator should increasingly be able to determine:

* what LEO is;
* what LEO is not;
* which architectural principles govern it;
* which capabilities are implemented;
* which capabilities are architecturally defined;
* which materials are historical;
* which demonstrations are reproducible;
* which claims are supported by evidence;
* how provenance is preserved;
* how evidence lineage can be inspected;
* where human review occurs;
* where institutional authority remains external to the system;
* which areas remain under development;
* which questions remain unresolved.

Public evaluation is not equivalent to production authorization.

The following distinctions apply:

```text id="ns6uvv"
PUBLICLY EVALUABLE
!=
PRODUCTION AUTHORIZED
```

and:

```text id="mr4m4b"
RUNTIME COMPLETE
!=
AUTONOMOUS AUTHORITY
```

A public repository, completed demonstration, passing scoped tests, frozen runtime baseline, or successful internal architectural review does not independently authorize deployment into production systems.

---

# Public Demonstration Portfolio

The public demonstration portfolio provides inspectable examples of selected LEO runtime capabilities.

The demonstrations do not represent autonomous institutional authority and should be evaluated within their documented scopes.

The current public demonstration portfolio is documented in:

### [LEO Public Demo Catalog](./PUBLIC_DEMO_CATALOG.md)

The portfolio currently includes three principal public demonstration tracks.

## 1. Institutional Approval Review

### [LEO Institutional Approval Review Demo](./demos/institutional_approval_review/README.md)

This embedded public demonstration presents a local, human-controlled evidence-review workflow for institutional approval chains.

The demonstration includes:

* structured input-quality validation;
* approval-workflow analysis;
* evidence-backed review findings;
* human reviewer actions;
* local review-package export;
* zero-autonomy safety boundaries.

The demonstration should be interpreted as scoped runtime evidence rather than as proof of complete LEO production readiness.

## 2. Procurement / Accounting Review

### [LEO Procurement / Accounting Review Demo](https://github.com/BBS-contact/leo-procurement-accounting-demo)

This public evaluation demonstration presents evidence-linked procurement and accounting review signals, source-trust warnings, reviewer questions, and local export-package generation.

Public demonstration page:

### [Open Procurement / Accounting Public Demo](https://bbs-contact.github.io/leo-procurement-accounting-demo/)

The demonstration supports human review.

Its analytical findings and review signals do not constitute autonomous fraud determinations, legal conclusions, or institutional enforcement actions.

## 3. Grant Expense Review

### [LEO Grant Expense Review Demo](https://github.com/BBS-contact/leo-grant-expense-review-demo)

This public evaluation demonstration presents a human-controlled grant-expense review workflow involving evidence generation, documentation-completeness review, budget-line review, reviewer-dashboard use, and review-package export.

Its outputs remain reviewer-support artifacts.

They do not independently authorize institutional action.

---

# Demonstration Governance Boundary

All public LEO demonstrations remain human-review-oriented.

They do not independently authorize LEO to:

* approve;
* reject;
* block;
* punish;
* sanction;
* issue authoritative fraud determinations;
* issue authoritative legal conclusions;
* autonomously enforce institutional outcomes;
* mutate production records;
* replace institutional authority.

A demonstration proves only what is actually exercised and supported by evidence within its documented scope.

---

# Historical Prototype Demonstration

The repository also preserves an earlier technical demonstration of the LEO investigative pipeline:

### [LEO Prototype Demonstration](./demonstration/LEO_PROTOTYPE_DEMONSTRATION.md)

This artifact is important historical runtime evidence.

It includes earlier pipeline concepts and runtime outputs associated with areas such as:

* anomaly detection;
* graph analysis;
* pattern detection;
* cluster analysis;
* investigation-report generation;
* risk escalation;
* institutional alert creation.

These capabilities and terms should be interpreted in their historical runtime context.

In particular, historical `risk escalation` and `institutional alert` mechanisms do not define the current governing architecture as an autonomous escalation or enforcement system.

Earlier runtime components associated with case handling, escalation, alerting, and automatic triggering remain part of LEO's engineering provenance where preserved in the repository.

They should not be silently deleted or rewritten merely because the architecture has evolved.

The current architecture instead governs their interpretation through explicit human-review and institutional-authority boundaries.

The historical relationship is therefore:

```text id="ck26nn"
LEGACY / HISTORICAL RUNTIME EVIDENCE
!=
CURRENT PUBLIC ARCHITECTURAL AUTHORITY
```

This distinction preserves engineering history while preventing earlier implementation terminology from misrepresenting the current LEO model.

---

# Historical Preservation and Institutional Memory

LEO treats historical evidence as part of institutional and engineering memory.

Architectural evolution should not create the appearance that previous states never existed.

Where appropriate, the project should use:

* explicit supersession;
* status labeling;
* provenance references;
* correction history;
* archived evidence;
* review records;

rather than silent historical deletion.

This applies both to institutional knowledge processed by LEO and to the engineering history of LEO itself.

The governing continuity principle is:

```text id="f6nby1"
PRESERVE HISTORY
    +
IDENTIFY CURRENT AUTHORITY
    +
PRESERVE PROVENANCE
    +
MAKE SUPERSESSION EXPLICIT
    +
REQUIRE HUMAN REVIEW
```

Preserving historical states allows future reviewers to understand what the system previously did, how the architecture evolved, and which current rules supersede earlier approaches.

---

# Repository Structure

This repository contains public-facing elements of the LEO research, architecture, runtime-demonstration, governance, and evaluation infrastructure.

Principal public areas include:

```text
/docs
    institutional and research documentation

/demonstration
    preserved prototype demonstration material

/demos
    embedded public runtime demonstrations

/licensing
    licensing-related repository artifacts

/architecture
    public architecture descriptions

/PROJECT_STATUS.md
    current public project status and evaluation-readiness position

/PUBLIC_DEMO_CATALOG.md
    public demonstration catalog
```

The presence of an artifact in the public repository does not by itself establish that the artifact represents the current governing architecture.

Repository materials may represent:

* current governing architecture;
* current runtime evidence;
* public evaluation artifacts;
* historical or legacy evidence;
* licensing or institutional documentation.

Evaluators should consider the status and scope of an artifact when interpreting it.

Public institutional documents are located primarily in the `/docs` directory.

For the current project-status declaration, see:

### [LEO Project Status](./PROJECT_STATUS.md)

For public demonstration navigation, see:

### [LEO Public Demo Catalog](./PUBLIC_DEMO_CATALOG.md)

---

# Regulatory Context and Boundary

LEO is developed in Poland within the European Union.

Its architecture is designed with attention to issues relevant to responsible institutional technology, including:

* human oversight;
* provenance;
* evidence lineage;
* traceability;
* controlled institutional authority;
* reviewability;
* correction history;
* data and evidence governance;
* risk-aware system design.

European and Polish legal and regulatory frameworks may be relevant to LEO's development, evaluation, institutional use, or future deployment.

Relevant areas may include, depending on the specific use case and deployment context:

* GDPR;
* the EU Artificial Intelligence Act;
* applicable data-governance requirements;
* applicable Polish law;
* applicable foundation, accounting, contractual, employment, administrative, sector-specific, or other legal requirements.

Reference to these frameworks does not constitute a claim that LEO, the repository, a demonstration, a runtime baseline, or a future deployment has been independently determined to comply with every applicable legal or regulatory requirement.

Regulatory applicability and compliance depend on context, processing activities, institutional roles, deployment conditions, data categories, contractual relationships, and other facts requiring appropriate review.

Accordingly:

```text
REGULATORY AWARENESS
!=
VERIFIED REGULATORY COMPLIANCE
```

Any public claim of GDPR, EU AI Act, or other regulatory compliance should be supported by separate appropriate legal, technical, organizational, and evidentiary review.

---

# Licensing and Intellectual Property

This repository contains licensing-related artifacts and historical licensing statements.

Existing repository materials describe a licensing structure involving concepts such as:

* a Public Knowledge Layer;
* an Institutional Integration Layer;
* a Core Execution Layer;
* Fundacja BBS intellectual-property interests;
* historical licensing associated with earlier releases.

These materials are preserved as part of the current repository state and project history.

However, this README does not independently certify that all licensing-related artifacts, historical statements, current repository contents, third-party dependencies, contribution conditions, intellectual-property claims, and public-facing licensing descriptions have already been reconciled into a final publication-ready licensing position.

Before final publication readiness and broader institutional, corporate, foundation, developer, or EU/institutional cooperation, LEO requires a dedicated:

```text
LICENSE / IP / THIRD-PARTY LICENSING CONSISTENCY REVIEW
```

That review should examine, based on repository evidence:

* repository-level license artifacts;
* public-facing licensing statements;
* historical license declarations;
* licensing-layer descriptions;
* third-party software and dependencies;
* third-party documentation or other incorporated materials where applicable;
* redistribution conditions;
* attribution requirements;
* contribution expectations;
* ownership and intellectual-property statements;
* compatibility among applicable licenses;
* the relationship between public artifacts and protected implementation components;
* whether current licensing language accurately reflects the material actually published.

The dedicated review must preserve historical licensing evidence rather than silently rewriting it.

This README does not pre-judge the outcome of that review.

Until the review is completed, the presence of a licensing statement or licensing file should not be interpreted beyond the scope actually supported by that artifact and its applicable context.

For existing licensing-related repository materials, see:

### [Licensing Directory](./licensing/)

---

# Institutional Context

LEO is developed by:

**Fundacja BBS — Better Balance System**
Poland (European Union)

The project is being developed within a controlled institutional, architectural, engineering, and evaluation framework.

The Foundation's work around LEO includes exploration and development related to:

* institutional integrity infrastructure;
* evidence traceability;
* provenance;
* human-controlled analytical systems;
* process characterization;
* anomaly analysis;
* reviewed institutional knowledge;
* responsible digital governance;
* public evaluation and reproducibility.

Institutional context does not change the core authority boundary of the system.

LEO remains a reviewer-support architecture rather than an autonomous institutional authority.

---

# Claim Discipline

Public LEO documentation follows an evidence-based claim discipline.

Public descriptions should distinguish among:

## Implemented

Functionality that exists in implementation.

## Tested

Functionality supported by appropriately scoped test evidence.

## Demonstrated

Functionality exercised by an inspectable demonstration.

## Architecturally Defined

Behavior or requirements established by reviewed architecture but not necessarily fully implemented.

## Historical

Evidence preserved from an earlier system or repository state.

## Planned

Functionality or work that remains future activity.

These categories should not be substituted for one another merely to simplify public messaging.

A public statement should not exceed the evidence available to support it.

Historical test results should remain tied to their original scope.

Historical runtime functionality should remain identified as historical where it no longer represents current governing architecture.

Architectural requirements should not be presented as implemented functionality unless implementation evidence supports that statement.

Public demonstrations should not be presented as evidence for capabilities outside their demonstrated scope.

---

# Current Public Status

The current LEO public status is:

**ACTIVE ARCHITECTURAL AND ENGINEERING DEVELOPMENT**

**CONTROLLED PUBLIC EVALUATION PREPARATION**

**HUMAN REVIEW REQUIRED**

LEO is being developed as a human-controlled institutional integrity, provenance, evidence review, process characterization, anomaly analysis, and reviewed knowledge system.

The current architecture preserves distinctions among:

```text
SOURCE EVIDENCE
EVIDENCE-DERIVED CHARACTERISTICS
SIGNAL ELIGIBILITY
ANALYTICAL SIGNALS
PROCESS MODE PROPOSALS
ANOMALY CONTEXT
REVIEWED / INSTITUTIONAL KNOWLEDGE
HUMAN DECISIONS
```

These distinctions are governance boundaries as well as analytical distinctions.

LEO does not claim autonomous enforcement authority.

LEO does not claim autonomous learning authority over institutional truth.

LEO does not issue authoritative fraud verdicts.

LEO does not independently issue authoritative legal verdicts.

LEO is not authorized by this README to mutate production systems.

No current global LEO test count is asserted here without current appropriately scoped validation.

No GDPR, EU AI Act, or other regulatory compliance claim is asserted here without separate appropriate evidence and review.

Production deployment requires separate explicit authorization.

---

# Public Evaluation Sequence

Current public-repository alignment and publication readiness proceed through controlled review.

The intended sequence is:

```text
PROJECT_STATUS.md
    ->
README.md
    ->
PUBLIC_DEMO_CATALOG.md
    ->
index.html
    ->
CROSS-DOCUMENT ARCHITECTURAL CONTINUITY / CONSISTENCY REVIEW
    ->
LICENSE / IP / THIRD-PARTY LICENSING CONSISTENCY REVIEW
    ->
FINAL PUBLICATION-READINESS REVIEW
    ->
EXPLICIT HUMAN APPROVAL
    ->
PUBLIC REPOSITORY UPDATE
    ->
FRESH-CLONE / POST-PUSH VERIFICATION
```

Completion of one step does not authorize skipping subsequent review gates.

In particular:

* documentation alignment does not resolve licensing consistency;
* licensing review does not itself authorize production deployment;
* public evaluation does not establish autonomous institutional authority;
* successful demonstrations do not establish complete-system production readiness;
* passing scoped tests do not establish an unsupported global test status;
* completion of technical review does not replace explicit human approval.

---

# Evaluation Navigation

A public evaluator can begin with:

1. this `README.md` for the high-level architecture, governance boundaries, demonstrations, and repository orientation;
2. [`PROJECT_STATUS.md`](./PROJECT_STATUS.md) for the detailed current project-status and evaluation-readiness position;
3. [`PUBLIC_DEMO_CATALOG.md`](./PUBLIC_DEMO_CATALOG.md) for the public demonstration portfolio;
4. the individual demonstration documentation for scoped runtime evidence;
5. architecture, governance, provenance, and institutional documentation relevant to the capability being evaluated.

Historical prototype material should be interpreted as historical evidence where the current documentation identifies it as such.

Where two artifacts appear to conflict, evaluators should consider whether they belong to different architectural periods, runtime scopes, or evidence categories before treating the difference as a current architectural contradiction.

---

# Architectural Continuity

LEO's current public positioning does not require deletion or concealment of earlier engineering history.

Legacy runtime components, previous terminology, historical demonstrations, earlier test baselines, architectural changes, and prior development states remain relevant to project provenance.

The governing continuity principle is:

```text
PRESERVE HISTORY
    +
IDENTIFY CURRENT AUTHORITY
    +
PRESERVE PROVENANCE
    +
MAKE SUPERSESSION EXPLICIT
    +
REQUIRE HUMAN REVIEW
```

Current architecture may supersede earlier public positioning without erasing the evidence that the earlier state existed.

This enables external evaluators and future developers to understand not only what LEO currently represents, but how and why its architecture evolved.

---

# Current Governance Boundaries

For clarity, the current public LEO position maintains the following boundaries:

* human review required;
* no autonomous enforcement;
* no autonomous institutional authority;
* no autonomous learning of institutional truth from raw evidence;
* no authoritative fraud verdicts;
* no authoritative legal verdicts;
* no automatic conversion of anomaly detection into accusation;
* no production mutation without separate explicit authorization;
* provenance and evidence lineage must be preserved;
* historical evidence should remain traceable;
* uncertainty should remain visible where evidence does not support a stronger conclusion;
* public claims should remain proportionate to evidence;
* regulatory compliance should not be claimed without appropriate supporting review;
* production readiness should not be inferred solely from completed or frozen runtime baselines.

---

# Contact

**Fundacja BBS — Better Balance System**
Poland (European Union)

Institutional, research, evaluation, collaboration, licensing, or regulatory inquiries should be directed to the Foundation through its official channels.

---

# Repository Position

This repository provides public-facing evidence and documentation for the continuing development and evaluation of LEO.

It should be interpreted as an evolving public evaluation environment rather than as evidence that every LEO architectural layer is complete, production-deployed, or autonomously authorized.

The repository is intended to support increasingly rigorous external evaluation while preserving:

* architectural continuity;
* engineering provenance;
* evidence lineage;
* historical runtime evidence;
* explicit governance boundaries;
* human authority;
* reproducibility where applicable;
* institutional memory.

For the detailed current project-status declaration:

### [LEO Project Status](./PROJECT_STATUS.md)

For public demonstration navigation:

### [LEO Public Demo Catalog](./PUBLIC_DEMO_CATALOG.md)

---

**LEO — Human-Controlled Institutional Integrity, Provenance, Evidence Review and Anomaly Analysis System**

**Status: Active architectural and engineering development / Controlled public evaluation preparation**

**Human review required.**
