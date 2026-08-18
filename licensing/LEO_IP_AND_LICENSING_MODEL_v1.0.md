# LEO IP AND LICENSING MODEL v1.0

**Document Status:** Architectural and Licensing Governance Draft
**Version:** 1.0
**Project:** LEO
**Original Author / Developer / Rights Holder:** Pavlo Martseniuk
**Institutional Context:** Fundacja BBS — Better Balance System
**Document Function:** Canonical architectural basis for future artifact-level licensing alignment
**Legal Status:** Subject to professional legal review where legal validity, enforceability, statutory interpretation, contractual authority, or jurisdiction-specific effects are concerned

---

## 1. Purpose

This document defines the architectural model by which intellectual property, licensing, publication, collaboration, protected implementation, provenance, and institutional use are to be distinguished within LEO.

Its purpose is not merely to select a single repository licence.

LEO contains, or may contain over time, materially different classes of artifacts with different functions, disclosure requirements, security implications, collaboration purposes, provenance requirements, and permissible uses. A single undifferentiated repository-wide licensing statement is therefore insufficient as the long-term governance model.

This document establishes a structured basis for determining:

* who is identified as the original author and original rights holder of LEO;
* how ownership is distinguished from licences and permissions granted to other parties;
* how Fundacja BBS — Better Balance System participates in LEO without being represented as the original author or original IP owner;
* how public knowledge and evaluation materials are distinguished from controlled integration materials and protected core technology;
* how individual artifacts must be assigned an explicit licensing status;
* how public availability differs from transfer of ownership;
* how controlled collaboration may occur without falsely representing restricted material as open source;
* how proprietary and security-sensitive components remain protected;
* how commercial-use permissions are governed;
* how institutional collaborations are authorized and documented;
* how contributor rights and provenance are preserved;
* how third-party code, dependencies, datasets, evidence, documentation, and other external materials are identified and governed;
* how trademarks, project identity, branding, forks, derivatives, and rebranding are handled;
* how historical licensing evidence is preserved;
* how future licensing changes are versioned without silently rewriting historical grants or provenance;
* how licensing decisions remain compatible with LEO's human-controlled governance architecture;
* and how the existing repository licensing artifacts should later be reviewed and aligned through explicit, separately authorized changes.

The model is intended to protect two objectives simultaneously.

First, LEO should remain capable of public-interest visibility, independent evaluation, research, education, citation, institutional scrutiny, and legitimate collaboration.

Second, public visibility must not be treated as an implicit surrender of intellectual property, security-sensitive implementation, governance-critical technology, project identity, or the right to control uses that have not been expressly authorized.

These objectives are complementary rather than contradictory.

Transparency can be intentionally provided at one architectural layer while implementation rights remain controlled at another.

---

## 2. Status and Legal-Review Boundary

This document is an architectural and licensing-governance specification.

It records the intended LEO IP and licensing model and establishes the framework that future repository licensing artifacts should follow.

It is not a substitute for professional legal advice.

In particular, this document must not be interpreted as independently establishing:

* the legal validity of a historical agreement;
* the legal effectiveness of an assignment or licence;
* the existence of an exclusive licence;
* the enforceability of a restriction in a particular jurisdiction;
* the legal authority of Fundacja BBS to enter into a particular transaction with its founder or governing officer;
* the correct corporate representation procedure for such a transaction;
* the legal consequences of historical Apache, AGPL, Creative Commons, proprietary, institutional, or other licensing statements;
* the ability to revoke rights that may already have been validly granted;
* regulatory compliance;
* or a definitive interpretation of Polish, European Union, or other applicable law.

Where the validity or effect of a licensing arrangement depends on law rather than architecture, repository evidence, or an explicit human governance decision, the matter must be escalated to qualified legal review.

This boundary is mandatory.

LEO documentation must not convert an unresolved legal question into an asserted legal fact merely for the purpose of making repository documentation appear internally consistent.

### 2.1 No Unsupported Regulatory Compliance Claims

This model does not establish or certify compliance with:

* the General Data Protection Regulation;
* the European Union Artificial Intelligence Act;
* any other European Union regulatory regime;
* Polish statutory requirements;
* sector-specific regulatory obligations;
* cybersecurity certification requirements;
* procurement requirements;
* or any other legal or regulatory framework.

LEO architecture may contain governance controls, provenance mechanisms, human-review requirements, evidence-lineage mechanisms, security boundaries, and design properties that are relevant to regulatory analysis.

Those properties are not equivalent to verified legal compliance.

Any future public claim of compliance must be supported by the appropriate evidence and review process.

### 2.2 Architectural Decisions Versus Legal Conclusions

For purposes of this document, an architectural decision may define what LEO intends to do prospectively.

For example, the project may decide that:

* a particular class of future artifacts should be publicly readable;
* a protected runtime component should not be publicly released;
* controlled integration code requires explicit authorization;
* every published artifact must carry an artifact-level licensing classification;
* contributor provenance must be recorded before integration;
* or historical licensing evidence must be retained.

Such decisions can be established as project governance.

They must nevertheless be distinguished from legal conclusions about rights that may already exist because of prior publication, prior licences, contracts, statutory rules, contributor rights, third-party licences, or other historical circumstances.

Where those two domains intersect, the historical and legal position must be reviewed rather than assumed.

---

## 3. Author and Original Rights Holder

The canonical ownership principle for LEO is:

**Pavlo Martseniuk is identified as the Author, Developer, and Original Rights Holder of LEO, subject to any rights of third parties that may exist in specific third-party materials, contributions, dependencies, datasets, or other incorporated artifacts.**

This statement establishes the intended authorship and original-rights baseline for LEO governance.

It must not be expanded into a claim that every byte, dependency, dataset, quotation, externally supplied contribution, or third-party artifact associated with LEO is owned by Pavlo Martseniuk.

Third-party rights must remain identifiable and must be governed separately.

### 3.1 Original Ownership Is Distinct from Institutional Operation

Fundacja BBS — Better Balance System may participate in the institutional operation, publication, evaluation, development support, collaboration, demonstration, administration, or deployment-related governance of LEO only within rights and authority validly available to it.

Institutional participation does not by itself transfer original authorship.

Institutional publication does not by itself transfer original ownership.

Repository hosting does not by itself transfer original ownership.

Project administration does not by itself transfer original ownership.

Foundation governance activity does not by itself make the Foundation the original author of LEO.

Accordingly, repository documentation must not represent Fundacja BBS as the original owner of LEO merely because the Foundation operates, supports, publishes, evaluates, demonstrates, or institutionally uses the project.

### 3.2 Third-Party Rights Remain Distinct

The ownership baseline defined above must coexist with the rights of other parties.

Possible third-party rights include, without limitation:

* open-source software copyrights;
* dependency licences;
* contributor copyrights;
* documentation copyrights;
* dataset rights;
* database rights;
* Creative Commons materials;
* externally supplied evidence;
* trademarks;
* patent rights;
* contractual restrictions;
* confidentiality obligations;
* public-sector information rules;
* and other legally protected interests.

The LEO ownership model must therefore preserve artifact-level provenance.

No general LEO ownership statement may be used to erase or obscure third-party attribution, licence conditions, or provenance.

---

## 4. Ownership and Licensing Are Different Legal and Governance Concepts

Ownership and licensing must remain explicitly separated throughout LEO documentation.

Ownership identifies the underlying rights holder or rights holders.

A licence defines permissions granted by a rights holder, or by another party legally authorized to grant them.

Publication is not automatically an ownership transfer.

Source availability is not automatically an ownership transfer.

Public access is not automatically a grant of unrestricted implementation rights.

A licence grant is not automatically an assignment of copyright.

An institutional licence is not automatically an ownership transfer.

A repository being publicly accessible does not, by itself, establish that every artifact within it is open source.

Likewise, describing one layer or artifact as proprietary does not retroactively eliminate rights that may previously have been granted under a valid public licence.

These distinctions are foundational to the LEO licensing architecture.

### 4.1 Rights Must Be Granted Deliberately

Permissions should be granted through an identifiable licensing mechanism appropriate to the artifact.

The intended model therefore rejects reliance on ambiguous assumptions such as:

* "it is on GitHub, therefore anyone may use it for anything";
* "the repository contains an Apache licence, therefore every artifact is Apache-licensed";
* "a licensing directory contains AGPL text, therefore every integration component is AGPL";
* "documentation is publicly readable, therefore ownership has been transferred";
* "the Foundation publishes the project, therefore the Foundation owns it";
* or "the core is proprietary, therefore earlier public grants automatically cease to exist."

Instead, future licensing alignment must make the applicable permission and restriction discoverable at the appropriate artifact or artifact-class level.

### 4.2 No Implied Expansion of Rights

A licence applying to one artifact, directory, layer, release, or identified class must not automatically be interpreted by project documentation as applying to unrelated artifacts.

For example:

* a public documentation licence must not automatically license protected source code;
* a controlled source licence must not automatically grant rights to security-sensitive core technology;
* a licence covering a specific integration package must not automatically govern all LEO runtime components;
* and a proprietary notice for protected implementation must not be used to claim proprietary ownership over third-party open-source dependencies.

Licensing scope must be explicit enough to preserve these boundaries.

---

## 5. Role of Fundacja BBS — Better Balance System

Fundacja BBS — Better Balance System is to be represented as an institutional participant in the LEO ecosystem rather than as the original author or original owner of LEO.

Its precise rights must derive from validly granted authority.

Depending on the final legally reviewed arrangement, such authority may include some combination of:

* institutional use;
* project administration;
* public-interest publication;
* evaluation activities;
* research cooperation;
* demonstrations;
* pilot coordination;
* institutional integration;
* grant or public-interest activities;
* representation within explicitly authorized limits;
* collaboration management;
* or other specified functions.

The existence and scope of those permissions must not be inferred beyond the evidence available.

### 5.1 No Unverified Exclusive-Licensee Claim

The repository must not state as a verified current legal fact that Fundacja BBS is the exclusive licensee of LEO unless that status is separately established through legally valid documentation and appropriate legal review.

Historical documents using terminology such as **Exclusive Institutional Licensee** are evidence of historical documentation state.

They are not, by terminology alone, proof that a legally effective exclusive licence exists.

Until the relevant agreement and applicable legal requirements are reviewed, the safer architectural representation is:

**Fundacja BBS is an institutional licensee and/or operator only to the extent of rights validly granted to it.**

This formulation is deliberately limited.

It does not determine the legal validity, exclusivity, duration, or complete scope of any historical agreement.

### 5.2 Foundation Agreement Requires Separate Legal Review

A historical agreement concerning licensing of LEO to Fundacja BBS has been identified as a matter requiring separate review.

The project governance position is not to presume that agreement valid or invalid.

Questions concerning transactions between Pavlo Martseniuk and Fundacja BBS — including questions arising from governance roles, representation, conflicts of interest, authorization, corporate procedure, or other requirements under applicable Polish law — are legal questions.

They must not be resolved through repository documentation alone.

Until reviewed, repository alignment must avoid relying on that historical agreement as conclusive proof of:

* exclusivity;
* ownership transfer;
* sublicensing authority;
* commercial authority;
* representation authority;
* or any other unresolved legal effect.

### 5.3 Foundation Operation Does Not Erase Provenance

Institutional use by Fundacja BBS must preserve the provenance of LEO.

The Foundation's role must not obscure:

* original authorship;
* original rights ownership;
* contributor provenance;
* third-party rights;
* historical licensing states;
* release history;
* repository history;
* evidence lineage;
* or later changes in licensing policy.

This principle is part of LEO's broader institutional-memory architecture.

---

## 6. Three-Layer IP and Licensing Architecture

LEO adopts a three-layer architectural model for prospective licensing governance:

1. **Layer I — Public Knowledge & Evaluation**
2. **Layer II — Controlled Collaboration & Integration**
3. **Layer III — Protected Core Technology**

The layers describe different disclosure and permission domains.

They are not merely repository directories.

They are not automatically licence names.

They are not substitutes for artifact-level licensing.

They are governance classifications used to determine what kind of access, publication, licensing, security treatment, and human authorization an artifact requires.

An artifact's layer classification must therefore be distinguished from the specific legal instrument eventually selected for that artifact.

### 6.1 Why a Layered Model Is Required

LEO has competing but legitimate requirements.

It must be possible for external evaluators to understand important architectural principles, inspect appropriate evidence, assess public demonstrations, cite public material, understand governance boundaries, and evaluate the project's claims.

At the same time, not every implementation detail should necessarily be publicly reusable.

Some components may:

* expose security-sensitive behavior;
* implement governance-critical controls;
* contain protected algorithms;
* enable circumvention if disclosed without appropriate safeguards;
* represent technology intended for controlled institutional collaboration;
* require negotiated commercial terms;
* contain third-party restrictions;
* or require access controls for other legitimate reasons.

A binary model of either **everything open** or **everything closed** is therefore insufficient.

The three-layer architecture provides a controlled middle structure.

### 6.2 Layers Do Not Override Artifact-Level Rights

Layer classification alone does not create a legal licence.

For example:

**Layer I** does not automatically mean CC BY-NC-SA 4.0.

**Layer II** does not automatically mean AGPLv3.

**Layer III** does not mean that third-party components located near protected code lose their original licences.

Each artifact or defined artifact class must ultimately have a licensing determination consistent with:

* ownership;
* provenance;
* intended use;
* disclosure requirements;
* third-party obligations;
* historical grants;
* security classification;
* collaboration model;
* and legal-review requirements.

### 6.3 Layer Classification Must Be Reviewable

Classification into a licensing layer must be subject to human review.

No automated LEO runtime component may autonomously decide that an artifact:

* becomes public;
* changes licence;
* becomes proprietary;
* is approved for commercial use;
* may be distributed;
* may be sublicensed;
* may be disclosed despite a security boundary;
* or has had historical licensing rights revoked.

Automation may assist with evidence collection, classification proposals, inconsistency detection, provenance review, or documentation checks.

Final licensing and publication authority remains human-controlled.

---

## 7. Layer I — Public Knowledge & Evaluation

**Layer I — Public Knowledge & Evaluation** exists to support legitimate public understanding and scrutiny of LEO.

Its intended purposes include:

* public understanding;
* independent evaluation;
* research;
* education;
* citation;
* architectural transparency;
* governance transparency;
* reproducibility where appropriate;
* public-interest discussion;
* and societal benefit.

Layer I is the principal domain through which LEO can be publicly visible without requiring that all implementation technology be released under unrestricted terms.

### 7.1 Typical Layer I Artifact Classes

Subject to artifact-level review, Layer I may include:

* public architectural explanations;
* public evaluation guides;
* public demo documentation;
* public governance explanations;
* non-sensitive specifications;
* public research materials;
* citation information;
* public provenance explanations;
* evidence-lineage documentation;
* selected schemas intended for evaluation;
* selected examples;
* educational materials;
* public project-status documentation;
* evaluation checklists;
* public repository maps;
* public methodology descriptions;
* and other materials intentionally designated for public knowledge or evaluation.

This list is illustrative rather than self-executing.

An artifact does not become Layer I merely because it resembles an item on this list.

The artifact must be classified deliberately.

### 7.2 Public Availability Does Not Transfer Ownership

Layer I publication must preserve the distinction between visibility and ownership.

Making an artifact publicly accessible does not mean:

* ownership has been abandoned;
* copyright has been transferred;
* attribution requirements disappear;
* trademarks become unrestricted;
* all derivative uses are permitted;
* all commercial uses are permitted;
* protected implementation is included in the grant;
* or other LEO layers become subject to the same licence.

The applicable licence must state the actual rights granted.

### 7.3 Exact Layer I Licence Must Be Selected Explicitly

This model does not automatically designate CC BY-NC-SA 4.0, Apache-2.0, AGPLv3, or any other licence as the universal Layer I licence.

Different Layer I artifact classes may require different licensing instruments.

For example, documentation, source code, data, schemas, images, research material, and evaluation outputs may have materially different licensing requirements.

Selection must consider:

* artifact type;
* intended public use;
* desired derivative-use permissions;
* commercial-use policy;
* attribution requirements;
* compatibility with third-party materials;
* provenance;
* existing historical grants;
* and legal review where necessary.

Accordingly, Layer I defines a governance domain.

It does not itself substitute for the artifact-level licence.

### 7.4 Public Evaluation Must Remain Credible

Licensing controls must not be used to create a misleading appearance of transparency.

If LEO makes a public claim that a capability is independently evaluable, the publicly available material should be sufficient for the scope of evaluation actually claimed.

Where evaluation is necessarily limited because protected implementation is withheld, that limitation should be disclosed.

The project should distinguish between:

* architectural transparency;
* behavioral evaluation;
* reproducible public demonstrations;
* source-level inspection;
* controlled source review;
* and access to protected implementation.

These are different levels of visibility.

Public documentation must not imply that an evaluator has access to a level of evidence that has not actually been provided.

### 7.5 Public-Interest Purpose Does Not Eliminate Licensing Boundaries

LEO's societal or public-interest objectives do not require abandonment of IP governance.

Public-interest publication can coexist with:

* retained copyright;
* attribution;
* controlled commercial use;
* trademark protection;
* protected security-sensitive technology;
* negotiated institutional permissions;
* and controlled collaboration.

The appropriate balance must be made explicit rather than assumed.

---

## 8. Layer I Boundary Decision

Layer I establishes the public knowledge and evaluation domain of LEO.

It does not determine the licensing status of controlled integration code or protected core technology.

Those domains require separate treatment because their access, reuse, commercial, security, and institutional implications differ materially from public knowledge and evaluation artifacts.

---

## 9. Layer II — Controlled Collaboration & Integration

**Layer II — Controlled Collaboration & Integration** exists to support legitimate technical, institutional, research, evaluation, pilot, and commercial collaboration where public Layer I access is insufficient but unrestricted public release is not appropriate.

Layer II occupies the controlled space between publicly available knowledge and protected core technology.

It may include selected source code, APIs, interfaces, integration components, reference implementations, pilot implementations, evaluation implementations, technical specifications, test materials, interoperability components, or other artifacts intentionally made available to approved collaborators.

The defining characteristic of Layer II is not secrecy.

The defining characteristic is **controlled authorization**.

Access, use, modification, evaluation, integration, redistribution, deployment, or commercial exploitation may be permitted under defined terms, but those permissions must not be inferred merely from repository visibility or technical accessibility.

### 9.1 Layer II Is Not Automatically Open Source

Layer II must not be described as open source merely because source code is available to an approved collaborator or because selected code is visible in a repository.

Where a licence imposes restrictions incompatible with the applicable definition of open source — including authorization requirements, field-of-use restrictions, commercial restrictions, redistribution restrictions, or other non-open conditions — public documentation must not use the term **open source** for that material.

LEO documentation must distinguish between:

* publicly viewable source;
* source available for evaluation;
* source available to approved collaborators;
* source available under a negotiated institutional licence;
* source available under a commercial agreement;
* genuinely open-source code;
* and proprietary source.

These categories are not interchangeable.

### 9.2 AGPL Is Not the Automatic Layer II Default

Historical LEO licensing material has associated the Institutional Integration Layer with the GNU Affero General Public License version 3.

That historical association must be preserved as licensing provenance.

It does not establish AGPLv3 as the automatic prospective licence for every Layer II artifact.

AGPL may remain appropriate for specific artifacts where:

* the rights holder deliberately selects it;
* the artifact can lawfully be licensed under it;
* third-party compatibility has been reviewed;
* the consequences of modification and network interaction have been considered;
* the intended collaboration model is compatible with its terms;
* and the decision is documented at artifact level.

Other Layer II artifacts may require:

* a controlled source licence;
* an evaluation licence;
* an institutional licence;
* a research collaboration agreement;
* a pilot agreement;
* a commercial licence;
* a dual-licensing arrangement;
* or another legally reviewed instrument.

The appropriate mechanism must follow the intended rights and restrictions rather than forcing all controlled collaboration into a historically selected licence.

### 9.3 Typical Layer II Artifact Classes

Subject to explicit classification and review, Layer II may include:

* selected integration APIs;
* integration adapters;
* interoperability components;
* evaluation implementations;
* research implementations;
* institutional pilot code;
* selected reference implementations;
* controlled SDKs;
* controlled test harnesses;
* selected schemas not intended for unrestricted reuse;
* integration documentation containing non-public operational detail;
* partner-specific implementation materials;
* deployment evaluation materials;
* selected runtime components approved for controlled inspection;
* and other collaboration artifacts whose use requires authorization.

This list is illustrative.

It does not automatically classify any existing artifact.

Existing artifacts must be reviewed individually or through a formally defined artifact class before Layer II status is assigned.

### 9.4 Controlled Source Access

Controlled source access may be used where legitimate evaluation or collaboration requires source-level inspection but unrestricted publication would create unacceptable IP, security, commercial, contractual, or governance exposure.

Controlled source access should define, as applicable:

* who may access the material;
* what material is included;
* the purpose of access;
* whether copying is permitted;
* whether modification is permitted;
* whether local execution is permitted;
* whether deployment is permitted;
* whether redistribution is permitted;
* whether derivative works are permitted;
* whether publication of findings is permitted;
* confidentiality requirements;
* security requirements;
* retention requirements;
* termination conditions;
* and the applicable licence or agreement.

Access controls must not substitute for legal clarity.

Likewise, a legal licence must not substitute for appropriate technical access controls where protected material requires them.

### 9.5 Institutional Collaboration

LEO should support collaboration with legitimate external actors, potentially including:

* researchers;
* universities;
* independent evaluators;
* developers;
* foundations;
* non-governmental organizations;
* public institutions;
* municipalities;
* public bodies;
* auditors;
* regulated institutions;
* commercial partners;
* and other approved organizations.

Such collaboration does not require that all collaborators receive identical rights.

The rights granted should correspond to the collaboration purpose.

For example, an independent evaluator may require inspection rights without deployment rights.

A research partner may require experimental modification rights without commercial distribution rights.

A public institution conducting a pilot may require controlled operational rights within a defined environment.

A commercial integration partner may require separately negotiated implementation and deployment rights.

The licensing architecture must permit these distinctions without changing original ownership.

### 9.6 Commercial Use Within Layer II

Commercial use must be expressly addressed rather than assumed.

The fact that an artifact is available for research, evaluation, or institutional collaboration does not automatically authorize:

* commercial deployment;
* commercial SaaS operation;
* resale;
* sublicensing;
* white-label deployment;
* incorporation into a commercial proprietary product;
* paid redistribution;
* commercial hosting;
* or monetization of protected LEO technology.

Where commercial rights are intended, they must be granted explicitly.

The grant should identify the relevant artifact scope and applicable conditions.

Where commercial rights are not granted, documentation should state that limitation accurately without representing the material as open source if the restrictions would make that characterization misleading.

### 9.7 Layer II Must Not Become an Accidental Path to Layer III

Layer II collaboration must not create an uncontrolled path to protected Layer III technology.

Before a Layer II artifact is shared, the project should review whether it:

* embeds protected algorithms;
* exposes security-sensitive implementation;
* contains credentials or secrets;
* exposes internal security controls;
* reveals protected governance mechanisms;
* includes proprietary components not authorized for disclosure;
* includes third-party material that cannot be redistributed;
* contains sensitive operational data;
* or creates an indirect technical route to material outside the authorized scope.

Where such exposure exists, the artifact should be separated, redacted where legally and technically appropriate, redesigned, or retained within Layer III.

Redaction or separation must preserve provenance.

Historical originals must not be silently rewritten or destroyed merely to create a publication-safe derivative.

---

## 10. Layer III — Protected Core Technology

**Layer III — Protected Core Technology** contains LEO technology that is not subject to a general public implementation-rights grant.

The prospective default for genuinely Layer III material is:

**PROPRIETARY / ALL RIGHTS RESERVED**, subject to third-party rights and any specific existing rights that must be preserved.

Layer III exists to protect implementation whose unrestricted disclosure, reuse, modification, redistribution, commercialization, or operational replication is not authorized.

### 10.1 Typical Layer III Categories

Subject to explicit classification, Layer III may include:

* security-sensitive code;
* governance-critical runtime;
* protected algorithms;
* internal security mechanisms;
* protected implementation;
* non-public operational controls;
* security-sensitive detection mechanisms;
* protected integration logic;
* internal administrative tooling;
* non-public deployment mechanisms;
* sensitive configuration;
* protected orchestration logic;
* and other technology specifically classified as protected core material.

This list is architectural rather than dispositive.

An artifact must not be declared proprietary merely because it is technically important.

Ownership, historical licensing, contributor rights, third-party rights, and previous public grants must first be considered.

### 10.2 No Public Grant of Layer III Implementation Rights by Default

Classification as Layer III means that the project does not prospectively intend to provide a general public grant to:

* reproduce protected implementation;
* modify it;
* distribute it;
* deploy it;
* sublicense it;
* commercialize it;
* offer it as a service;
* create commercial derivatives from it;
* or incorporate it into another product.

Any such permission requires explicit authorization from the party legally entitled to grant it.

This prospective policy does not itself extinguish rights that may already exist under valid historical licensing.

### 10.3 Security-Sensitive Disclosure

Protection of Layer III is not solely an economic IP concern.

Some material may require restricted disclosure because publication could:

* weaken security controls;
* expose attack surfaces;
* facilitate circumvention;
* reveal sensitive operational assumptions;
* enable manipulation of review mechanisms;
* compromise institutional safeguards;
* expose confidential integrations;
* or create other concrete security risks.

Security-sensitive classification must nevertheless be used narrowly and reviewably.

It must not become a generic justification for concealing information merely because that information is inconvenient, critical, or potentially embarrassing.

A security classification should have an identifiable rationale.

Where possible, LEO should separate:

* the public architectural principle;
* the evaluable behavior;
* the security-sensitive implementation;
* and the protected operational detail.

This permits meaningful evaluation while preserving legitimate security boundaries.

### 10.4 Protected Core Does Not Mean Autonomous Enforcement

The term **Protected Core Technology** must not be interpreted as authorizing autonomous institutional enforcement.

LEO's current governance boundaries remain applicable regardless of licensing layer.

Protected runtime capability does not create institutional authority.

In particular, Layer III classification does not authorize LEO to:

* autonomously enforce institutional decisions;
* autonomously punish or sanction a person or organization;
* issue fraud verdicts;
* issue binding legal verdicts;
* autonomously mutate production systems;
* bypass required human review;
* or convert an anomaly, signal, confidence value, or process-mode proposal into an enforcement action.

Licensing architecture governs rights and access.

It does not expand LEO's decision authority.

### 10.5 Historical Runtime Components

Historical runtime components may contain names or behaviors that reflect earlier architectural stages.

Examples previously identified within LEO history include components such as:

* `RiskEscalationEngine`;
* `CaseEscalationEngine`;
* `InstitutionalAlertEngine`;
* `CaseEngine`;
* and `AutomaticCaseTrigger`.

Such components are part of historical/runtime evidence.

Their existence must not automatically define current LEO public positioning.

Likewise, licensing alignment must not silently delete, rename, rewrite, or otherwise alter historical runtime evidence merely to make it conform superficially to current terminology.

If a historical component requires later architectural review, deprecation, isolation, documentation, or migration, that must occur through a separately authorized engineering process preserving provenance.

### 10.6 Protected Core and Third-Party Components

Layer III protection cannot override rights granted by third parties.

If protected LEO code uses or contains third-party components, each third-party component remains subject to its applicable rights and obligations.

The project must not:

* label third-party open-source code as exclusively proprietary LEO property;
* remove required copyright notices;
* remove required licence notices;
* impose incompatible restrictions on third-party material;
* or conceal dependency provenance.

Protected LEO implementation and third-party licensed components must therefore remain distinguishable.

---

## 11. Artifact-Level Licensing

The three-layer architecture is insufficient without artifact-level licensing discipline.

Every material artifact intended for publication, controlled distribution, institutional sharing, or protected retention should have a discoverable licensing status.

The status may be assigned individually or through a clearly defined artifact class.

### 11.1 Artifact-Level Licensing Record

Where appropriate, an artifact-level licensing record should identify:

* artifact name or identifier;
* repository path or other location;
* artifact type;
* layer classification;
* original rights holder;
* relevant contributors;
* third-party components or embedded material;
* selected licence or legal instrument;
* version of that licence or instrument;
* permitted uses;
* restricted uses where applicable;
* attribution requirements;
* redistribution status;
* modification status;
* commercial-use status;
* sublicensing status where relevant;
* security classification where relevant;
* historical licensing state;
* supersession status;
* legal-review status;
* human approver;
* approval date;
* and provenance reference.

Not every public artifact must carry all of this information directly in its body.

The information may be maintained through a canonical mapping mechanism where that mechanism is clear, durable, reviewable, and publicly discoverable when public discovery is required.

### 11.2 Artifact-to-License Mapping Requirement

Before future licensing alignment is considered complete, LEO should establish an explicit artifact-to-license mapping.

That mapping should prevent situations in which a reader encounters multiple repository-level licensing statements but cannot determine which one applies to a particular artifact.

The mapping must be capable of representing at least:

* Layer I public artifacts;
* Layer II controlled artifacts;
* Layer III protected artifacts;
* third-party artifacts;
* mixed or composite artifacts;
* historically licensed artifacts;
* and artifacts requiring legal review.

Where classification is unresolved, the mapping should record the uncertainty rather than inventing a definitive licence.

An appropriate unresolved state may be represented conceptually as:

**LICENSING_STATUS_REQUIRES_REVIEW**

or equivalent reviewed terminology.

The final machine-readable or documentation representation may be decided separately.

### 11.3 Composite Artifacts

Some artifacts may contain material governed by more than one rights regime.

Examples may include:

* documentation containing third-party images;
* source packages containing dependencies;
* evaluation bundles containing public documentation and controlled code;
* datasets combining internally generated and externally licensed records;
* or reports quoting external evidence.

Such artifacts must not be forced into a false single-ownership model.

Where necessary, licensing documentation should identify component-specific rights.

### 11.4 Ambiguity Must Be Preserved Until Resolved

Where the applicable licence is uncertain, LEO must not automatically select whichever licence appears most permissive, most restrictive, or most convenient.

Ambiguity is itself a review state.

The appropriate response is to:

1. identify the artifact;
2. preserve the artifact and its historical state;
3. identify available licensing evidence;
4. identify conflicting claims;
5. identify relevant ownership and third-party issues;
6. record the unresolved status;
7. obtain human review;
8. obtain legal review where required;
9. document the resulting decision;
10. preserve the decision's provenance.

This approach is consistent with LEO's broader evidence-governance architecture.

---

## 12. Public Availability Versus Ownership and Permission

LEO must maintain a clear distinction between four concepts:

1. **visibility** — whether an artifact can be seen;
2. **access** — whether a party can obtain or inspect it;
3. **permission** — what that party is legally authorized to do with it;
4. **ownership** — who holds the underlying rights.

These concepts may overlap, but they are not equivalent.

### 12.1 Public Repository Visibility

An artifact located in a publicly accessible repository may be visible and technically retrievable.

That technical fact does not, by itself, define the complete legal permission set.

The applicable licence and historical licensing context remain relevant.

Conversely, if a valid open-source licence applies to an artifact, later moving that artifact to a private repository does not by itself erase rights already granted under the applicable licence.

Repository visibility and licensing history must therefore be tracked separately.

### 12.2 Controlled Repository Visibility

A private or access-controlled repository may contain material licensed to specific parties.

Private visibility does not necessarily mean no licence exists.

The rights of an authorized collaborator may derive from:

* a software licence;
* institutional agreement;
* research agreement;
* pilot agreement;
* evaluation agreement;
* commercial agreement;
* confidentiality arrangement;
* or another valid authorization.

The repository access mechanism should support, not replace, that authorization model.

### 12.3 Publication Does Not Create Foundation Ownership

Where Fundacja BBS publishes a LEO artifact within an authorized institutional role, the act of publication must not be documented as transferring original LEO ownership to the Foundation unless a legally effective rights transfer actually exists.

Attribution and copyright notices should reflect the reviewed ownership and licensing structure.

### 12.4 Withdrawal From Publication

If a future decision is made to stop publicly distributing an artifact, the project may be able to cease future distribution under some circumstances.

That operational decision must not be represented as automatically revoking permissions already validly granted to recipients.

The consequences depend on the applicable licence, agreement, and law.

Where historical public licensing is involved, professional legal review may be required before making claims about revocation or continuing rights.

---

## 13. Commercial Use Boundaries

LEO's licensing model must make commercial-use boundaries explicit.

The project has a legitimate interest in preventing unauthorized appropriation, fragmentation, rebranding, or commercialization of protected technology.

That objective must be pursued through valid IP, licensing, contractual, trademark, repository, access-control, provenance, and security mechanisms rather than through unsupported claims that copying can be made technically impossible.

### 13.1 No Automatic Commercial Permission Across LEO

No single commercial-use assumption applies to all LEO artifacts.

Commercial rights depend on the artifact and its applicable licence.

Possible states include:

* commercial use permitted by an applicable public licence;
* commercial use permitted subject to licence conditions;
* commercial use requiring explicit authorization;
* commercial use governed by a negotiated agreement;
* commercial use prohibited under a valid applicable agreement;
* or commercial status requiring review.

Historical grants must be considered before applying a new prospective commercial policy.

### 13.2 Public-Interest Access and Commercial Rights Are Separate

An artifact may be made available for:

* research;
* education;
* public evaluation;
* citation;
* institutional scrutiny;
* or non-commercial experimentation

without necessarily granting commercial deployment rights.

However, any restriction must be expressed through an appropriate legal instrument.

Project documentation must not describe restricted material as open source when the restriction is incompatible with that description.

### 13.3 Commercial Partnerships

LEO may support legitimate commercial partnerships where they are compatible with project governance and explicitly authorized.

A commercial agreement may address matters including:

* implementation scope;
* deployment scope;
* permitted organizations;
* permitted environments;
* fees;
* support;
* maintenance;
* source access;
* modification rights;
* derivative works;
* confidentiality;
* security;
* attribution;
* branding;
* sublicensing;
* termination;
* data responsibilities;
* audit rights;
* and IP ownership.

The existence of a commercial partnership must not automatically transfer ownership of the underlying LEO technology.

Any transfer or assignment of rights would require a separate, explicit, legally valid instrument.

### 13.4 Anti-Appropriation Objective

The strategic objective of the LEO licensing architecture includes reducing the risk that another actor can take protected LEO technology and present it as an independently owned, unrestricted, or rebranded product contrary to the rights actually granted.

Relevant protections may include:

* copyright;
* explicit licence scope;
* proprietary boundaries;
* controlled repository access;
* trademark protection;
* contributor provenance;
* institutional agreements;
* commercial agreements;
* security controls;
* release provenance;
* historical repository evidence;
* and enforcement of valid legal rights by authorized human or institutional actors.

No document should claim that these measures make unauthorized copying technically impossible.

Licensing controls establish rights, obligations, and remedies.

They do not eliminate the physical possibility of copying digital information.

---

## 14. Institutional Collaboration Boundaries

Institutional collaboration must preserve LEO's governance architecture.

A licence or collaboration agreement may grant technical rights.

It must not be interpreted as granting LEO itself autonomous institutional authority.

### 14.1 Human-Controlled Institutional Use

Institutional use of LEO must preserve the applicable human-review requirements.

A collaborating institution must not infer from access to LEO technology that LEO is authorized to make binding institutional decisions autonomously.

Where LEO produces:

* evidence-derived characteristics;
* signals;
* anomaly indications;
* confidence information;
* process-mode proposals;
* review recommendations;
* or other analytical outputs,

those outputs remain subject to the governance model applicable to the capability.

Licensing does not convert analytical output into institutional verdict authority.

### 14.2 No Fraud or Legal Verdict Authority

No Layer I, Layer II, or Layer III licensing arrangement changes the LEO boundary that the system does not possess autonomous authority to issue fraud or legal verdicts.

An institution may have its own legally established authority and processes.

Those institutional powers must not be confused with LEO's technical capability.

### 14.3 No Production Mutation Merely From Technical Capability

Possession of code capable of changing a production system does not constitute authorization to perform that change.

Production mutation requires separate operational authority and human-controlled governance.

A licence to inspect, use, modify, or integrate software must not be interpreted as automatically authorizing LEO itself to mutate production environments autonomously.

### 14.4 Institutional Responsibility

Organizations using LEO remain responsible for their own:

* legal authority;
* operational decisions;
* human-review procedures;
* access controls;
* data governance;
* regulatory obligations;
* security controls;
* and institutional actions.

LEO licensing documentation must not imply that use of the system transfers those responsibilities to the software.

---

## 15. Contributor IP and Provenance

Contributor governance is necessary to protect both LEO and its contributors.

The project must be able to establish the provenance of contributions and determine whether it has the rights necessary to use, modify, publish, distribute, protect, or license them as intended.

### 15.1 Contribution Does Not Automatically Erase Contributor Rights

A contribution to LEO does not automatically transfer all contributor rights merely because it is submitted to a repository.

The legal effect depends on the applicable contribution terms, licence, agreement, assignment, or other valid mechanism.

The project should not assume ownership where no valid ownership transfer exists.

### 15.2 Contributor Provenance Requirements

For material contributions, LEO should preserve sufficient provenance to determine:

* contributor identity or accountable contributor record;
* contribution date;
* contribution scope;
* source of the contributed material;
* applicable licence or contribution terms;
* whether third-party material is included;
* whether the contributor asserts authority to contribute it;
* review status;
* integration decision;
* and relevant commit or artifact history.

The precise implementation of this record may vary by contribution type.

### 15.3 Contributor Agreements

Before broad external contribution is encouraged, LEO should determine whether its intended licensing architecture requires:

* a Developer Certificate of Origin;
* a Contributor Licence Agreement;
* a copyright assignment mechanism;
* project-specific contribution terms;
* or another reviewed provenance and rights mechanism.

No particular mechanism is selected by this document.

The appropriate mechanism requires separate governance and legal review.

### 15.4 No Rights Laundering Through Contribution

LEO must not accept a contribution as if it were clean project-owned material when there is reason to believe it contains unauthorized third-party content.

Where provenance is uncertain, the contribution should remain unresolved until reviewed.

This principle applies to:

* source code;
* documentation;
* datasets;
* images;
* models;
* generated artifacts;
* research material;
* schemas;
* and other protected content.

### 15.5 AI-Assisted Contributions

Where AI-assisted or machine-generated material is contributed, provenance should record that fact where relevant to rights assessment, reproducibility, institutional accountability, or later review.

AI assistance must not be treated as proof that:

* the output is free of third-party rights;
* the output can be exclusively owned;
* the output is legally safe to redistribute;
* or the contributor has automatically obtained all necessary rights.

Material questions should be reviewed under the applicable legal and project policy.

---

## 16. Part 1B Boundary Decision

Part 1B establishes the controlled collaboration, protected core, artifact-level licensing, commercial-use, institutional-collaboration, and contributor-provenance foundations of the LEO IP and Licensing Model.

The next part must continue the same document by addressing external rights and identity boundaries, beginning with:

**17. Third-Party Dependencies and Third-Party Licences**

It must then continue into datasets and external evidence, trademarks and branding, forks and derivatives, security-sensitive disclosure, publication/repository boundaries, and the historical licensing model without redefining Sections 1–16.

---

## 17. Third-Party Dependencies and Third-Party Licences

LEO's ownership and licensing architecture must distinguish original LEO intellectual property from third-party software, libraries, frameworks, documentation, datasets, standards, media, research materials, and other externally sourced artifacts.

No LEO ownership or proprietary classification may erase rights belonging to third parties.

Likewise, the presence of third-party open-source material within a LEO environment does not automatically place original LEO technology under the same licence unless the applicable licence legally requires that result.

Third-party licensing must therefore be handled through explicit provenance and compatibility review rather than assumptions based solely on repository location.

### 17.1 Dependency Identification

Before an artifact is publicly released, distributed to a collaborator, incorporated into a controlled integration package, or classified as protected core technology, relevant third-party dependencies should be identified.

The review should consider, as applicable:

* software libraries;
* frameworks;
* command-line tools;
* runtime dependencies;
* development dependencies;
* build tools;
* vendored source code;
* copied code fragments;
* generated code;
* schemas;
* standards-derived material;
* documentation;
* fonts;
* icons;
* images;
* templates;
* datasets;
* test fixtures;
* example data;
* external models;
* APIs;
* externally hosted services;
* and other incorporated or redistributed material.

The absence of a common package manifest must not be interpreted as proof that no third-party dependencies exist.

Dependency identification is an evidence task.

Where evidence is incomplete, the correct state is unresolved review rather than an unsupported declaration of independence from third-party material.

### 17.2 Third-Party Licence Record

Where a third-party component is used or redistributed, LEO should preserve sufficient information to identify:

* component name;
* component version where known;
* source or origin;
* upstream rights holder where identifiable;
* applicable licence;
* licence version where relevant;
* required copyright notices;
* required attribution;
* source-availability obligations where applicable;
* modification notice requirements;
* redistribution requirements;
* compatibility considerations;
* location within LEO;
* and the evidence supporting the classification.

Where multiple licences or licensing options exist, the option actually relied upon should be recorded where necessary.

### 17.3 Licence Compatibility

Before LEO redistributes or combines third-party material with original LEO artifacts, the applicable licensing conditions should be reviewed for compatibility with the intended distribution model.

Compatibility review may need to consider:

* copyleft obligations;
* network-use provisions;
* attribution requirements;
* notice requirements;
* source-disclosure requirements;
* patent provisions;
* trademark restrictions;
* commercial-use permissions;
* modification conditions;
* redistribution conditions;
* sublicensing restrictions;
* licence-version compatibility;
* and other applicable terms.

A compatibility decision must not be inferred solely from the names of licences.

Where legal interpretation is material, professional legal review is required.

### 17.4 Third-Party Open Source Within Protected LEO Systems

A protected or proprietary LEO package may depend on legitimately licensed open-source components.

Those components must retain their required notices and licensing treatment.

LEO must not represent those third-party components as exclusively owned proprietary LEO technology.

Conversely, the presence of an open-source dependency does not automatically establish that every original LEO component in the surrounding system is governed by the dependency's licence.

The actual legal interaction depends on:

* the applicable licence;
* the nature of integration;
* distribution;
* linking or other technical relationships where legally relevant;
* modifications;
* network interaction where relevant;
* and other facts.

Those questions must be reviewed rather than resolved by architectural assertion alone.

### 17.5 No Unverified Dependency-Clean Claim

LEO public documentation must not state that the project is free of third-party licensing obligations unless a sufficiently complete review supports that claim.

Likewise, an earlier repository search that did not identify common dependency manifests establishes only what was found in that search.

It does not establish that the entire LEO project contains no external dependencies.

### 17.6 Future Dependency Governance

As LEO moves toward broader public evaluation or institutional collaboration, a more formal dependency governance mechanism may be established.

Possible future mechanisms include:

* software bill of materials generation;
* dependency inventories;
* licence scanning;
* provenance manifests;
* third-party notice generation;
* release-specific dependency snapshots;
* or other reviewed controls.

This document does not authorize a specific implementation.

Any automated mechanism must remain reviewable and must not silently alter licensing classifications or repository contents.

---

## 18. Datasets and External Evidence

LEO's evidence architecture makes the treatment of datasets and external evidence particularly important.

Documents, records, datasets, reports, images, external publications, public records, institutional materials, user-supplied information, and other source material may function as evidence within LEO without becoming LEO-owned intellectual property.

The fact that LEO processes, indexes, references, analyzes, classifies, or preserves evidence does not by itself transfer ownership of that evidence.

### 18.1 Evidence Is Not Automatically Project-Owned Content

Source evidence may be governed by:

* copyright;
* database rights;
* contractual restrictions;
* confidentiality;
* privacy requirements;
* public-sector information rules;
* terms of access;
* research-use restrictions;
* institutional policies;
* evidentiary obligations;
* or other legal constraints.

Accordingly, LEO must distinguish:

* possession of evidence;
* access to evidence;
* analytical use of evidence;
* preservation of evidence;
* publication of evidence;
* redistribution of evidence;
* and ownership of evidence.

These are separate questions.

### 18.2 Evidence Provenance

Where external evidence materially contributes to a LEO review, classification, evaluation, or public claim, its provenance should be preserved to the extent legally and operationally appropriate.

Relevant provenance may include:

* source identifier;
* source organization or origin;
* acquisition date;
* acquisition mechanism;
* original location;
* version or snapshot where available;
* licence or access terms;
* transformation history;
* integrity information;
* review history;
* derived-artifact relationships;
* and restrictions affecting further use.

This provenance supports both licensing governance and LEO's broader evidence-lineage architecture.

### 18.3 Derived Analysis Does Not Erase Source Rights

A LEO-generated analysis derived from external evidence may contain original analytical material while still depending on protected or restricted source evidence.

The existence of an original analysis does not automatically grant permission to republish the complete underlying evidence.

Public evaluation artifacts should therefore distinguish between:

* source evidence;
* quotations or extracts;
* transformed evidence;
* metadata;
* analytical output;
* evidence-derived characteristics;
* signals;
* classifications;
* and human-reviewed conclusions.

Each category may have different rights and disclosure constraints.

### 18.4 Datasets

Before a dataset is included in a public or controlled LEO artifact, the project should determine, where relevant:

* who created or compiled it;
* where it originated;
* applicable licence or access conditions;
* whether redistribution is permitted;
* whether modification is permitted;
* whether attribution is required;
* whether database rights may apply;
* whether personal or confidential information is present;
* whether contractual restrictions apply;
* and whether publication is consistent with the intended evaluation purpose.

This document does not establish that any particular dataset is legally publishable.

### 18.5 Synthetic and Demonstration Data

Synthetic or demonstration data may reduce some external-rights risks but must not automatically be described as free of legal or provenance concerns.

Where synthetic data is derived from protected source material, generated using restricted inputs, or designed to reproduce identifiable records, additional review may still be required.

Public demo documentation should accurately distinguish synthetic, transformed, anonymized, pseudonymized, sampled, and real-world evidence where those distinctions matter.

### 18.6 Evidence Preservation and Licensing

Where historical evidence must be preserved for institutional memory, preservation does not automatically authorize public redistribution.

LEO may need to retain evidence internally while restricting its public availability.

The architecture must therefore distinguish:

**preservation authority** from **publication authority**.

This distinction is essential to maintaining evidence lineage without turning archival preservation into an unsupported public licensing claim.

---

## 19. Trademarks, Project Identity, and Branding

Copyright licensing and trademark governance must remain distinct.

A licence permitting use, modification, or redistribution of an artifact does not automatically grant unrestricted rights to use the names, marks, logos, institutional identities, or branding associated with LEO or Fundacja BBS.

### 19.1 LEO Identity

The LEO project identity should remain distinguishable from permission to use particular source code or documentation.

Where legally available and appropriately protected, trademark or branding rules may govern use of:

* the LEO name;
* LEO logos;
* project marks;
* certification-like statements;
* official project branding;
* official repository presentation;
* Fundacja BBS identity;
* and other identifiers.

The exact legally protected status of any mark must not be overstated without appropriate evidence.

### 19.2 No Automatic Trademark Grant

An artifact licence should not be interpreted as granting a trademark licence unless it expressly does so or applicable law requires another result.

A party may therefore possess rights to modify or redistribute a licensed artifact while remaining restricted from falsely presenting a derivative as:

* the official LEO project;
* an official Fundacja BBS release;
* an endorsed implementation;
* a certified implementation;
* or an authorized institutional deployment.

The precise restrictions must be legally supportable and appropriately documented.

### 19.3 Accurate Attribution Versus False Endorsement

Trademark policy must distinguish legitimate attribution from false endorsement.

A third party should not be prohibited from accurately identifying the origin of material where such identification is legally permitted or required.

At the same time, accurate attribution must not be transformed into a false claim that the third party's product, fork, service, or deployment is officially endorsed.

### 19.4 Foundation and LEO Branding Are Distinct

Fundacja BBS institutional branding and LEO project branding should not be treated as automatically identical.

Where different rights holders, policies, or institutional permissions apply, those distinctions should be preserved.

Future alignment of `TRADEMARK_POLICY.md` should reflect the final reviewed relationship between:

* LEO ownership;
* LEO project identity;
* Foundation institutional operation;
* permitted attribution;
* derivative identification;
* and false-endorsement prevention.

---

## 20. Forks, Derivatives, Redistribution, and Rebranding

LEO's licensing architecture must distinguish the technical possibility of creating a fork or derivative from the legal permission to do so.

The applicable rights depend on the licence governing the relevant artifact.

### 20.1 Publicly Licensed Artifacts

Where a valid public licence grants rights to modify, fork, or redistribute an artifact, LEO governance must recognize those granted rights.

Project policy must not falsely claim that a later licensing strategy can retroactively erase valid rights already granted.

Applicable attribution, notice, copyleft, share-alike, or other conditions may continue to apply according to the relevant licence.

### 20.2 Controlled Artifacts

Layer II artifacts may permit derivatives only within explicitly defined collaboration terms.

Depending on the governing instrument, derivative rights may be:

* permitted;
* permitted for evaluation only;
* permitted for internal institutional use;
* permitted for research;
* subject to approval;
* subject to commercial terms;
* restricted from redistribution;
* or otherwise defined.

These rights must be stated rather than inferred.

### 20.3 Protected Core Artifacts

Layer III artifacts carry no prospective general public permission to create or distribute derivatives unless such permission is explicitly granted.

This prospective boundary remains subject to any historical rights that may already apply.

### 20.4 Rebranding

The project has a legitimate interest in preventing misleading rebranding of protected technology as an independently originated or officially endorsed system.

That objective should be pursued through valid mechanisms such as:

* copyright;
* licence conditions;
* attribution;
* trademark policy;
* provenance records;
* contractual terms;
* and accurate public documentation.

The licensing model must not claim a broader legal power than the applicable rights actually provide.

### 20.5 Anti-Fragmentation Objective

LEO's strategic anti-fragmentation objective is to preserve architectural, governance, and provenance continuity while enabling legitimate public evaluation and collaboration.

Fragmentation risks may include:

* removal of provenance;
* misleading claims of original authorship;
* incompatible unofficial variants presented as official LEO;
* loss of governance boundaries;
* removal of human-review requirements from derivative institutional representations;
* appropriation of protected implementation;
* and confusion between historical and current architecture.

Not every form of technical divergence can or should be prohibited.

Where an applicable licence legally permits forks or derivatives, the project must respect those permissions.

The appropriate response to permitted divergence may instead include:

* clear official-project identification;
* trademark boundaries;
* provenance requirements;
* versioning;
* compatibility declarations;
* and transparent distinction between official and independent derivatives.

### 20.6 No Unsupported Anti-Copying Guarantee

No LEO licensing document should claim that the project can guarantee that corporations, investors, institutions, individuals, or other actors will never copy protected material.

Digital material can be copied in violation of rights or agreements.

The project can instead establish layered protection through:

* ownership evidence;
* copyright;
* explicit licence scope;
* proprietary boundaries;
* repository boundaries;
* access controls;
* trademarks;
* contributor provenance;
* institutional agreements;
* commercial agreements;
* security controls;
* and historical provenance.

The objective is defensible governance and enforceable rights where available, not an impossible technical guarantee.

---

## 21. Security-Sensitive Disclosure Governance

Security-sensitive disclosure requires a governance model distinct from ordinary proprietary classification.

An artifact may be restricted because of security risk even where commercial sensitivity is limited.

Likewise, commercially valuable information is not automatically security-sensitive.

The two classifications should not be conflated.

### 21.1 Security Review Questions

Before public or controlled disclosure of potentially sensitive implementation, reviewers should consider whether disclosure could materially:

* expose credentials or secrets;
* reveal exploitable vulnerabilities;
* disclose security architecture in a manner that enables circumvention;
* expose internal access-control mechanisms;
* reveal protected administrative interfaces;
* disclose sensitive institutional integration details;
* facilitate manipulation of evidence-review processes;
* expose private operational data;
* compromise integrity controls;
* or otherwise create a concrete security risk.

The presence of such a risk does not automatically determine the final licensing instrument.

It establishes a reason for security review.

### 21.2 Minimum Necessary Restriction

Security restrictions should be proportionate to the identified risk.

Where meaningful public evaluation can be supported without exposing sensitive implementation, the project should consider publishing:

* architectural descriptions;
* interfaces;
* behavioral specifications;
* test evidence;
* controlled demonstrations;
* sanitized examples;
* non-sensitive schemas;
* or other evaluation artifacts.

This supports transparency while preserving legitimate security boundaries.

### 21.3 Security Classification Requires Human Review

LEO must not autonomously classify information as permanently secret or authorize its disclosure.

Automated tooling may identify possible secrets, sensitive patterns, dependency risks, or disclosure concerns.

Final classification and publication decisions remain human-controlled.

### 21.4 Vulnerability and Security Research

Future LEO governance may require a coordinated vulnerability disclosure or security research policy.

Such a policy should distinguish good-faith security research from unauthorized exploitation and should define appropriate reporting channels and handling procedures.

This document does not establish those procedures.

They require a separate reviewed artifact if and when authorized.

---

## 22. Publication and Repository Boundaries

Repository structure is an important implementation mechanism for the licensing model, but repository location alone must not become the licensing authority.

LEO may use different repositories or repository areas for:

* canonical historical material;
* runtime development;
* public evaluation packages;
* publication staging;
* controlled collaboration;
* protected implementation;
* archives;
* and verification clones.

These operational categories should remain consistent with the relevant licensing and disclosure classifications.

### 22.1 Publication Repository

A public repository should contain only artifacts that have been intentionally approved for public disclosure.

Before publication, review should establish:

* disclosure authorization;
* licensing status;
* third-party compatibility;
* provenance;
* security suitability;
* artifact-level licence mapping;
* and consistency with public positioning.

The fact that a file exists in a publication working copy does not itself constitute final publication approval.

### 22.2 Publication Working Copies

A publication working copy is a preparation environment.

It may contain proposed documentation changes that have not yet been:

* staged;
* committed;
* pushed;
* legally reviewed;
* or finally approved for publication.

Accordingly, local preparation must not be represented as completed public release.

### 22.3 Controlled Collaboration Repositories

Repositories used for Layer II collaboration should apply access controls appropriate to the collaboration.

Repository membership alone should not be relied upon as the complete statement of rights.

The applicable licence or agreement must remain identifiable.

### 22.4 Protected Repositories

Layer III implementation should be kept within repository and access boundaries appropriate to its classification.

Public documentation should avoid linking directly to protected material in ways that undermine those boundaries.

Where metadata about protected artifacts is publicly necessary for architectural transparency, the disclosed metadata should not unintentionally expose sensitive implementation.

### 22.5 Verification Clones and Derived Working Copies

Fresh clones, post-push verification repositories, staging copies, test copies, and other derived repository instances must not automatically be treated as independent licensing authorities.

Their role is operational or evidentiary.

Canonical licensing decisions should be traceable to the appropriate reviewed source and release state.

### 22.6 Archive as Institutional Memory

Historical repositories and archived artifacts form part of LEO's institutional memory.

Archive preservation is therefore not merely storage.

It supports:

* provenance;
* release reconstruction;
* licensing-history reconstruction;
* authorship evidence;
* contributor evidence;
* historical architecture;
* evaluation reproducibility;
* and correction history.

Archived material must not be silently altered to make historical licensing appear identical to current policy.

---

## 23. Historical Licensing Evidence

LEO currently has historical licensing evidence involving multiple licensing models and statements.

Known public-repository evidence includes, among other artifacts:

* a root `LICENSE` containing Apache License 2.0;
* a `licensing/LICENSE` containing GNU Affero General Public License version 3;
* historical licensing strategy material assigning different licensing approaches to architectural layers;
* institutional licensing material;
* proprietary core notices;
* Creative Commons-related historical strategy language;
* repository-wide source-code licensing statements;
* citation metadata referring users to the licensing directory;
* governance language concerning protected intellectual property;
* and legal/copyright material describing institutional and founder relationships.

These artifacts must be treated as historical licensing evidence.

The purpose of the new model is not to pretend those states never existed.

### 23.1 Historical Apache Evidence

The presence of Apache License 2.0 at repository root is legally and historically significant.

The project must not simply replace the file and then claim that Apache licensing never applied.

Before alignment, the actual scope and effect of the historical Apache licensing state require review.

Relevant questions may include:

* which artifacts were distributed while the root Apache licence was present;
* what repository documentation stated at the time;
* whether particular source files contained separate notices;
* whether recipients reasonably received rights under Apache-2.0;
* whether other conflicting notices affected interpretation;
* and what rights, if any, continue for historical recipients and versions.

These are not resolved by this architectural document.

### 23.2 Historical AGPL Evidence

The presence of AGPLv3 in `licensing/LICENSE` and historical identification of an Institutional Integration Layer as AGPL-licensed must likewise be preserved.

The new strategic decision not to use AGPL automatically for all future Layer II material does not mean that historical AGPL grants can be treated as nonexistent.

The scope and effect of those grants require evidence-based and, where material, legal review.

### 23.3 Historical Creative Commons Evidence

Historical licensing strategy material associated the Public Knowledge Layer with CC BY-NC-SA 4.0.

The current architecture does not automatically adopt that licence for every future Layer I artifact.

However, where historical artifacts were actually distributed under Creative Commons terms, those historical grants must be preserved and respected according to their applicable legal effect.

### 23.4 Historical Institutional Licence Evidence

`BBS_INSTITUTIONAL_LICENSE_v1.0.md` forms part of LEO's licensing history.

Its existence is evidence of an attempted or documented institutional licensing model.

It must not automatically be treated as proof that every term is legally effective or that the Foundation possesses a legally verified exclusive licence.

Its legal status, relationship to other licensing statements, and relationship to any underlying agreement require separate review.

### 23.5 Historical Proprietary Notice Evidence

`CORE_RUNTIME_PROPRIETARY_NOTICE_v1.0.md` is evidence of an intention to distinguish protected core technology from publicly licensed material.

Its historical existence should be preserved.

However, the notice cannot by itself retroactively convert third-party or previously licensed material into proprietary material.

Any problematic historical terminology or absolute legal assertions within the notice should be addressed later through explicit versioning or supersession rather than silent rewriting.

### 23.6 Conflicting Historical Evidence Must Remain Visible to Review

Where historical artifacts conflict, the conflict itself is evidence.

The appropriate response is not to select one historical document and erase the others.

The review process should determine:

* what each artifact stated;
* when it applied;
* what material it purported to cover;
* how it interacted with other notices;
* what was publicly distributed;
* what rights may have been granted;
* and what remains unresolved.

This evidence can then support a legally reviewed migration strategy.

---

## 24. No Silent Retroactive Relicensing

LEO adopts a strict governance principle against silent retroactive relicensing.

A new licensing policy may govern future releases or future grants where legally permitted.

It must not falsely rewrite the licensing history of artifacts already distributed.

### 24.1 Prospective Policy Versus Historical Grant

The project must distinguish:

**prospective licensing policy**

from:

**historical licensing grant**.

A prospective decision can state how future versions are intended to be licensed.

It cannot, merely by being written into a new document, extinguish rights that recipients may already possess under valid earlier licences.

### 24.2 No Historical Erasure

Alignment must not create statements such as:

* "LEO has always been proprietary" where historical public licensing evidence exists;
* "LEO has never been Apache-licensed" where Apache licensing evidence exists;
* "Layer II has never been AGPL" where historical AGPL positioning exists;
* or equivalent claims that erase documented history.

Where earlier policy is superseded, documentation should say that it was superseded prospectively and preserve the historical record.

### 24.3 Existing Copies and Historical Versions

Rights associated with already distributed copies may differ from rights applicable to future versions.

The legal consequences depend on the applicable licence and facts.

The project must therefore avoid claims that changing the licence of a future release automatically changes the licence of all historical copies.

### 24.4 Relicensing Authority

Before relicensing an artifact, LEO must establish that the party making the decision has the necessary rights to do so.

This is particularly important where an artifact contains:

* multiple contributors;
* third-party code;
* previously licensed components;
* jointly authored material;
* externally sourced content;
* or material governed by agreements limiting relicensing.

Where authority is unclear, relicensing must stop at a review gate.

---

## 25. Supersession, Versioning, and Licensing History

The preferred alignment mechanism is explicit versioning and supersession rather than silent replacement of historical meaning.

### 25.1 Canonical Current Policy

Once reviewed and formally adopted, this document is intended to become the canonical architectural basis for current and future LEO licensing alignment.

That status does not automatically amend every existing licence or agreement.

Individual artifacts still require separately approved alignment.

### 25.2 Supersession Statements

Where an existing strategy or policy document is replaced, the new or revised artifact should identify, where appropriate:

* the superseded document;
* superseded version;
* effective date;
* scope of supersession;
* whether supersession is prospective;
* historical status;
* and any unresolved legal questions.

The superseded artifact should remain recoverable as historical evidence.

### 25.3 Version History

Material licensing-policy changes should be versioned.

A version history should permit future reviewers to determine:

* what changed;
* when;
* why;
* under whose approval;
* what artifacts were affected;
* and whether the change applied prospectively or addressed an existing inconsistency.

### 25.4 No False Clean History

LEO must not create a sanitized licensing history that suggests the project always had a perfectly consistent licensing architecture.

The actual history includes evolving architectural and licensing decisions.

Preserving that evolution strengthens provenance.

It permits future evaluators to distinguish:

* historical design;
* correction;
* supersession;
* current policy;
* and unresolved legal issues.

---

## 26. Evidence Lineage and Institutional Memory

Licensing governance must integrate with LEO's broader evidence-lineage and institutional-memory principles.

Licensing decisions are institutional decisions supported by evidence.

They should therefore remain reconstructable.

### 26.1 Licensing Evidence Lineage

A material licensing decision should be capable of tracing, where relevant:

**SOURCE LICENSING EVIDENCE
-> OWNERSHIP / RIGHTS ANALYSIS
-> ARTIFACT CLASSIFICATION
-> THIRD-PARTY REVIEW
-> LICENSING OPTIONS
-> LEGAL REVIEW WHERE REQUIRED
-> HUMAN LICENSING DECISION
-> ARTIFACT-LEVEL LICENCE MAPPING
-> PUBLICATION / ACCESS DECISION
-> VERSIONED HISTORICAL RECORD**

This lineage is conceptually compatible with LEO's broader provenance architecture while remaining a distinct licensing-governance workflow.

### 26.2 Historical Evidence Must Be Preserved

Historical licences, notices, agreements, repository states, commits, publication records, and policy documents may become relevant to later rights analysis.

They should therefore not be silently destroyed merely because current policy changes.

Where a historical artifact must be removed from an active public route for a legitimate reason, its archival and provenance status should be determined separately.

### 26.3 Corrections Must Preserve Correction History

If an earlier licensing statement is determined to be incorrect, misleading, stale, or legally unsafe, the project should correct the active representation.

The correction should not falsely imply that the earlier representation never existed.

Where material, the correction record should identify:

* the previous state;
* the identified issue;
* the reviewed correction;
* effective scope;
* and the relationship to historical rights.

### 26.4 Archive Is Part of LEO Memory

LEO's archive must be treated as part of institutional memory.

This applies to licensing history as well as technical history.

Future LEO governance should be able to answer not only:

**What is the current licence?**

but also:

**What licensing state existed for this artifact at the relevant historical time, and what evidence supports that answer?**

That capability is essential for credible provenance.

---

## 27. Part 2A Boundary Decision

Part 2A establishes the external-rights, dataset, trademark, derivative, security-disclosure, repository-boundary, historical-licensing, supersession, and institutional-memory foundations of the LEO IP and Licensing Model.

The next part must continue the same document with compatibility between this licensing architecture and current LEO governance and Process Mode architecture.

It must then define:

* human-review requirements;
* no-autonomous-enforcement boundaries;
* no fraud or legal verdict authority;
* no production mutation from licensing decisions;
* the licensing decision workflow;
* artifact-to-license decision governance;
* ambiguity handling;
* legal-review gates;
* the unresolved Foundation agreement issue;
* and explicit non-goals.

---

## 28. Compatibility with Current LEO Architecture and Process Mode Governance

The LEO IP and licensing model must remain compatible with the current LEO architectural baseline.

Licensing governance must not revive obsolete architectural claims or introduce terminology that contradicts the current system model.

The current canonical Process Mode architecture is:

**SOURCE EVIDENCE
-> EVIDENCE-DERIVED CHARACTERISTICS
-> SIGNAL ELIGIBILITY
-> DETERMINISTIC / STOCHASTIC SIGNAL COUNTS
-> PROCESS MODE PROPOSAL
-> HUMAN REVIEW**

The canonical Process Mode states are:

* `DETERMINISTIC_PROCESS`
* `STOCHASTIC_PROCESS`
* `MIXED_PROCESS`
* `UNKNOWN_REQUIRES_REVIEW`

These states describe the character of a process under review.

They do not define licensing categories.

They do not determine ownership.

They do not determine whether an artifact is public, controlled, or proprietary.

They do not create legal authority.

### 28.1 Licensing Layers and Process Modes Are Orthogonal

The three licensing layers:

* Layer I — Public Knowledge & Evaluation;
* Layer II — Controlled Collaboration & Integration;
* Layer III — Protected Core Technology;

must remain conceptually separate from Process Mode classification.

A deterministic process may be implemented by:

* publicly documented architecture;
* controlled integration code;
* protected core technology;
* or a combination of all three.

A stochastic process may likewise be represented across multiple licensing layers.

A mixed process does not imply mixed licensing.

An unknown process mode does not imply unresolved ownership.

These systems answer different questions.

Process Mode asks:

**What is the character of the process being reviewed?**

Licensing governance asks:

**Who owns or controls rights in an artifact, what permissions exist, and under what conditions may it be accessed, used, modified, distributed, or published?**

No automated mapping between these domains should be introduced.

### 28.2 Historical Deterministic-System Wording Is Stale

Historical licensing material has used wording equivalent to:

**"LEO is a deterministic institutional system architecture."**

That statement is no longer compatible with the current Process Mode architecture.

LEO now explicitly recognizes deterministic, stochastic, mixed, and unknown-requires-review process modes.

Future licensing and public documentation should therefore avoid using the historical deterministic-system statement as a general description of LEO.

The historical statement should remain preserved as provenance within the relevant superseded artifact.

It should not be silently removed from historical evidence.

### 28.3 Evidence-Derived Characteristics and Licensing Decisions

Evidence-derived characteristics used by the Process Mode Classifier are not licensing evidence by default.

Likewise, licensing evidence is not automatically evidence for process-mode classification.

The two may intersect in specific cases, but any such relationship must be explicit.

For example, a document describing a contractual licensing restriction may be relevant to:

* licensing analysis;
* provenance;
* repository publication decisions;
* or institutional authority.

It does not automatically generate a deterministic or stochastic process signal.

### 28.4 No Licensing Decision From Signal Counts

Deterministic or stochastic signal counts must never be used automatically to:

* choose a licence;
* declare an artifact proprietary;
* approve public release;
* approve controlled disclosure;
* approve commercial use;
* revoke existing rights;
* or determine ownership.

Signal-count logic exists for process characterization.

Licensing decisions require a separate evidence and review chain.

---

## 29. Human Review Requirement

Human review is mandatory for material licensing decisions.

This principle applies across all three licensing layers.

LEO tooling may assist in:

* discovering licensing files;
* identifying conflicting notices;
* detecting missing licence metadata;
* identifying third-party components;
* comparing repository states;
* producing proposed artifact classifications;
* highlighting possible incompatibilities;
* checking provenance completeness;
* identifying historical licensing evidence;
* and preparing review reports.

Those capabilities are advisory.

They do not constitute final licensing authority.

### 29.1 Human Licensing Authority

A material licensing decision should identify an accountable human decision-maker or legally authorized institutional decision process.

Depending on the decision, review may involve:

* the original rights holder;
* an authorized institutional representative;
* project governance;
* a contributor;
* a third-party rights holder;
* legal counsel;
* security review;
* or another appropriately authorized reviewer.

LEO must not invent authorization where it is not established.

### 29.2 No Autonomous Licence Assignment

LEO must not autonomously change an artifact from:

* public to controlled;
* controlled to proprietary;
* proprietary to public;
* one public licence to another;
* or one institutional licensing state to another.

Automated classification may propose a status.

The proposal must remain explicitly distinguishable from the human-approved status.

### 29.3 No Autonomous Acceptance of Legal Conclusions

LEO tooling must not automatically convert statements such as:

* "this appears to be Apache-licensed";
* "this may be proprietary";
* "this agreement may be invalid";
* "this contributor may not own the material";
* or "this licence may conflict with another";

into binding legal conclusions.

Such findings are review inputs.

Where legal interpretation is material, human legal review is required.

---

## 30. No Autonomous Enforcement

The licensing model must remain consistent with LEO's prohibition on autonomous enforcement.

A licensing violation, suspected violation, licence inconsistency, provenance anomaly, or unauthorized-use indicator may be identified for review.

It must not automatically result in an enforcement action by LEO.

### 30.1 Permitted Advisory Functions

LEO may support human reviewers by:

* flagging suspected licence inconsistencies;
* identifying missing attribution;
* detecting possible unauthorized repository exposure;
* identifying unreviewed derivatives;
* identifying provenance gaps;
* generating evidence reports;
* proposing escalation for human consideration;
* and preserving evidence lineage.

### 30.2 Prohibited Autonomous Actions

Without separate explicit human authority, LEO must not:

* send legal demands;
* issue takedown notices;
* revoke repository access;
* delete repositories;
* remove files;
* disable user accounts;
* block partners;
* alter licences;
* modify production access rights;
* destroy evidence;
* publish accusations;
* or impose sanctions.

Technical capability does not equal institutional authority.

### 30.3 Enforcement Belongs to Authorized Humans and Institutions

Where actual enforcement of IP rights or contractual terms becomes necessary, the decision must be made by the legally authorized rights holder or institution, with appropriate legal review.

LEO may support evidence preparation.

LEO does not become the rights-enforcement authority.

---

## 31. No Fraud or Legal Verdict Authority

Licensing or provenance analysis may reveal unusual, conflicting, incomplete, or suspicious patterns.

Those patterns must not be automatically converted into accusations of fraud, theft, infringement, bad faith, or other legal wrongdoing.

### 31.1 Evidence Review Versus Verdict

LEO may describe evidence-supported facts such as:

* two files contain conflicting licence statements;
* attribution is missing;
* a repository state differs from the approved mapping;
* a historical licence is present;
* a contributor's provenance record is incomplete;
* or an artifact was distributed under a particular documented state.

LEO should not transform those facts into an unsupported legal verdict.

### 31.2 Legal Characterization Requires Legal Authority

Terms such as:

* copyright infringement;
* breach of contract;
* fraud;
* misappropriation;
* unlawful distribution;
* or invalid agreement

may carry specific legal consequences.

Where those conclusions matter, qualified legal review is required.

The architectural record may state that an issue **requires legal review**.

That is not equivalent to declaring the legal outcome.

---

## 32. No Production Mutation From Licensing Analysis

Licensing analysis must not autonomously modify production systems.

This restriction applies even where LEO identifies:

* a missing licence;
* a contradictory notice;
* a possible proprietary leak;
* an unapproved dependency;
* or a possible access-control issue.

### 32.1 Production Mutation Requires Separate Authority

Any change to:

* production repositories;
* production deployments;
* access-control systems;
* publication endpoints;
* package registries;
* public websites;
* partner environments;
* or institutional infrastructure

requires separate operational authorization.

Licensing review may inform such a decision.

It does not execute it.

### 32.2 Repository Mutation Is a Separate Human-Controlled Step

Likewise, a reviewed licensing recommendation must not automatically trigger:

* file deletion;
* file rewriting;
* `git reset`;
* `git clean`;
* staging;
* commit;
* push;
* branch rewriting;
* tag rewriting;
* history rewriting;
* or repository archival.

Each mutation requires explicit human authorization appropriate to the context.

---

## 33. Licensing Decision Workflow

LEO should use a controlled licensing decision workflow for material artifact decisions.

The workflow should preserve evidence, uncertainty, human authority, and historical continuity.

### 33.1 Step 1 — Identify the Artifact

The artifact must be identified precisely enough to avoid ambiguity.

Relevant identifiers may include:

* path;
* repository;
* commit;
* release;
* version;
* checksum;
* artifact identifier;
* or another stable reference.

### 33.2 Step 2 — Establish Provenance

Available provenance should be collected.

This may include:

* original author;
* contributors;
* creation history;
* source repository;
* external source;
* acquisition history;
* prior licensing statements;
* release history;
* and relevant agreements.

### 33.3 Step 3 — Identify Existing Rights Evidence

The review should identify any applicable:

* licence text;
* notice;
* copyright statement;
* contributor terms;
* institutional agreement;
* third-party licence;
* public repository state;
* release metadata;
* historical strategy;
* or other evidence relevant to rights.

### 33.4 Step 4 — Identify Conflicts and Uncertainty

Conflicting evidence must be recorded rather than normalized away.

Examples include:

* root licence versus directory licence;
* repository-wide statement versus proprietary notice;
* institutional agreement versus public licence;
* contributor claim versus repository attribution;
* or current strategy versus historical release state.

### 33.5 Step 5 — Assign Preliminary Layer Classification

A reviewer may propose:

* Layer I;
* Layer II;
* Layer III;
* composite/mixed rights status;
* third-party governed;
* or unresolved.

This classification remains provisional until approved.

### 33.6 Step 6 — Evaluate Third-Party Obligations

Where external material exists, review should determine whether the intended licensing action is compatible with applicable third-party rights.

### 33.7 Step 7 — Evaluate Security and Publication Risk

The review should determine whether:

* public disclosure is appropriate;
* controlled access is required;
* security-sensitive information exists;
* or a protected boundary must be preserved.

### 33.8 Step 8 — Determine Legal-Review Requirement

If the decision depends on unresolved legal interpretation, the artifact must enter a legal-review gate.

### 33.9 Step 9 — Human Decision

An authorized human reviewer makes the licensing decision.

The decision should identify:

* approved layer;
* approved licence or agreement;
* applicable scope;
* restrictions;
* legal-review status;
* and any conditions.

### 33.10 Step 10 — Record Artifact-to-License Mapping

The approved result should be entered into the canonical licensing mapping.

### 33.11 Step 11 — Implement Separately

Only after approval should separately authorized implementation occur.

Implementation may include:

* adding licence metadata;
* updating notices;
* modifying publication documentation;
* creating access controls;
* or preparing a release.

Implementation must not be conflated with the decision itself.

### 33.12 Step 12 — Verify

After implementation, verification should confirm that:

* the approved licensing state is represented correctly;
* unrelated artifacts were not modified;
* historical evidence remains preserved;
* provenance remains intact;
* and repository/publication state matches the approved decision.

---

## 34. Artifact-to-License Decision Governance

The artifact-to-license mapping should become the operational bridge between the architectural model and concrete repository artifacts.

### 34.1 Mapping Must Be Authoritative but Reviewable

The mapping should identify the current approved status while preserving links to underlying evidence.

It must not become an opaque registry that hides historical complexity.

### 34.2 Suggested Decision States

A future mapping may require states such as:

* `APPROVED_PUBLIC`
* `APPROVED_CONTROLLED`
* `APPROVED_PROPRIETARY`
* `THIRD_PARTY_LICENSED`
* `COMPOSITE_RIGHTS`
* `LEGAL_REVIEW_REQUIRED`
* `LICENSING_REVIEW_REQUIRED`
* `HISTORICAL_SUPERSEDED`
* `DO_NOT_PUBLISH_PENDING_REVIEW`

These names are illustrative only.

They are not authorized canonical schema values by this document.

A separate implementation decision is required before machine-readable states are adopted.

### 34.3 Mapping Must Not Rewrite History

A current mapping may state that a current version is proprietary while preserving evidence that an earlier version was distributed under another licence.

The mapping should therefore support temporal or version-specific status where necessary.

### 34.4 Composite Rights Must Be Representable

The mapping must not force an artifact into a single licence where different components are governed differently.

A composite state should permit reference to:

* original LEO rights;
* third-party rights;
* dataset rights;
* documentation rights;
* and other relevant permissions.

---

## 35. Ambiguity Handling

Ambiguity must be handled conservatively but not destructively.

When licensing status is unclear, LEO must preserve the artifact and the evidence while preventing unsupported conclusions.

### 35.1 Uncertainty Is a Valid State

An unresolved licensing question may remain unresolved.

The project should prefer an explicit review state over a false definitive answer.

### 35.2 No Automatic Most-Restrictive Rule

LEO must not assume that ambiguity always means proprietary.

Doing so could wrongly disregard valid public rights.

### 35.3 No Automatic Most-Permissive Rule

LEO must not assume that ambiguity means unrestricted reuse.

Doing so could violate the rights of original or third-party rights holders.

### 35.4 Evidence Conflict

Where evidence conflicts, the review should record:

* the competing statements;
* the artifact versions involved;
* dates where available;
* repository locations;
* release context;
* and the unresolved legal or factual question.

### 35.5 Publication During Ambiguity

Where a licensing ambiguity materially affects the legality or safety of publication, new publication should normally pause until human review resolves the issue.

This is a prospective publication-control principle.

It does not authorize withdrawal of previously granted rights.

---

## 36. Legal-Review Gates

Legal review is required where an architectural or technical decision cannot safely resolve the legal question.

### 36.1 Mandatory Legal-Review Categories

Professional legal review should be treated as required where material issues involve:

* validity of historical agreements;
* exclusivity;
* assignment of copyright;
* authority of Fundacja BBS to contract with its founder or governing officer;
* sublicensing rights;
* termination rights;
* revocation of historical licences;
* contributor ownership disputes;
* compatibility of conflicting licences;
* interpretation of copyleft obligations;
* commercial restrictions;
* enforceability of anti-rebranding provisions;
* trademark rights;
* patent implications;
* regulatory claims;
* cross-border licensing questions;
* or other legally consequential uncertainty.

### 36.2 Legal Review Must Be Evidence-Based

Legal counsel should receive the relevant evidence rather than a simplified project narrative.

The review package may need to include:

* historical licence files;
* commit history;
* publication dates;
* repository snapshots;
* contributor information;
* agreements;
* notices;
* public statements;
* and artifact-specific provenance.

### 36.3 Legal Advice Must Not Be Fabricated Into Repository Documentation

Until legal advice exists, project documents should state that the matter requires legal review.

They must not invent conclusions in order to remove ambiguity from public-facing text.

---

## 37. Foundation Agreement Issue

The historical licensing relationship between Pavlo Martseniuk and Fundacja BBS requires dedicated legal review.

This issue must remain explicitly separated from the broader architectural decision that Pavlo Martseniuk is to be represented as the Author, Developer, and Original Rights Holder of LEO.

### 37.1 Known Governance Position

The current governance position is:

* Pavlo Martseniuk is identified as the original LEO author/developer/rights holder;
* Fundacja BBS is not to be represented as original owner merely because it operates or publishes LEO;
* Fundacja BBS may act only within rights validly granted to it;
* no current claim of legally verified exclusivity should be made without further review.

### 37.2 Historical Agreement Is Evidence, Not Final Legal Conclusion

The existence of an older agreement is relevant evidence.

The project must not presume:

* that it is valid;
* that it is invalid;
* that it created exclusivity;
* that it created sublicensing rights;
* that it transferred ownership;
* or that it is unenforceable.

Those questions depend on the document, facts, corporate authority, applicable Polish law, and professional legal analysis.

### 37.3 Founder / Institutional Representation Issue

Where the same individual is associated with the Foundation's governance and is also the counterparty or rights holder, questions may arise concerning:

* representation;
* authority;
* conflict-of-interest procedure;
* governing-body approval;
* or other statutory requirements.

This document does not determine the legal solution.

Repository documentation must not invent one.

### 37.4 Future Agreement Alignment

If legal review determines that a new or revised agreement is required, that agreement should clearly address:

* rights granted;
* exclusivity or non-exclusivity;
* duration;
* territory;
* fields of use;
* publication authority;
* institutional operation;
* sublicensing;
* commercial use;
* modification;
* distribution;
* termination;
* post-termination rights;
* attribution;
* trademark use;
* protected core access;
* and historical rights.

Any new agreement should be reviewed separately from this architectural model.

---

## 38. Explicit Non-Goals

This document intentionally does not attempt to resolve every legal, commercial, security, or operational issue associated with LEO.

### 38.1 No Automatic Licence Selection for Every Artifact

This document does not assign a final licence to every existing LEO artifact.

### 38.2 No Retroactive Legal Determination

It does not determine the legal effect of historical Apache, AGPL, Creative Commons, institutional, or proprietary licensing states.

### 38.3 No Foundation Ownership Claim

It does not represent Fundacja BBS as original owner of LEO.

### 38.4 No Verified Exclusive-Licensee Claim

It does not establish Fundacja BBS as a legally verified exclusive licensee.

### 38.5 No Open-Source Claim for All LEO

It does not state that all LEO code or artifacts are open source.

### 38.6 No Repository-Wide Apache Claim

It does not state that all repository source code is currently or historically governed exclusively by Apache License 2.0.

### 38.7 No Automatic AGPL Layer II Rule

It does not designate AGPLv3 as the mandatory licence for all Layer II artifacts.

### 38.8 No Automatic Creative Commons Layer I Rule

It does not designate CC BY-NC-SA 4.0 as the mandatory licence for all Layer I artifacts.

### 38.9 No Regulatory Certification

It does not certify GDPR, EU AI Act, or other regulatory compliance.

### 38.10 No Autonomous Licensing Enforcement

It does not authorize LEO to autonomously enforce licences or impose sanctions.

### 38.11 No Fraud or Legal Verdict Authority

It does not give LEO authority to determine fraud, infringement, contract breach, or other legal liability.

### 38.12 No Production Mutation Authority

It does not authorize automatic repository or production mutation.

### 38.13 No Historical Evidence Deletion

It does not authorize deletion, rewriting, or concealment of historical licensing evidence.

### 38.14 No Guarantee Against Unauthorized Copying

It does not claim that licensing or technical controls can make unauthorized copying impossible.

### 38.15 No Immediate Mutation of Existing Licensing Files

This document does not itself authorize changes to:

* root `LICENSE`;
* `licensing/LICENSE`;
* `licensing/NOTICE`;
* `licensing/LICENSE_STRATEGY_v1.0.md`;
* `licensing/BBS_INSTITUTIONAL_LICENSE_v1.0.md`;
* `licensing/CORE_RUNTIME_PROPRIETARY_NOTICE_v1.0.md`;
* `TRADEMARK_POLICY.md`;
* `GOVERNANCE.md`;
* `CONTRIBUTING.md`;
* `CITATION.cff`;
* `legal/copyright.html`;
* or other public documentation.

Each future change requires separate review and approval.

---

## 39. Part 2B Boundary Decision

Part 2B establishes compatibility between licensing governance and current LEO architecture, mandatory human review, non-enforcement boundaries, non-verdict boundaries, production-mutation restrictions, licensing workflow, artifact-to-license governance, ambiguity handling, legal-review gates, the unresolved Foundation agreement issue, and explicit non-goals.

The remaining part must complete the document by defining:

* the migration and alignment plan for existing licensing artifacts;
* sequencing and control of future changes;
* publication-readiness implications;
* architectural risks;
* legal and operational risks;
* implementation readiness;
* formal review decision;
* Architectural Continuity Statement;
* and the Next Authorized Phase.

---

## 40. Migration and Alignment Plan for Existing Licensing Artifacts

The adoption of this architectural model does not itself modify existing licensing artifacts.

Migration must occur through a controlled, evidence-preserving alignment process.

The current licensing environment contains multiple historical and potentially conflicting statements. These include repository-level licences, layer-specific licence statements, institutional licensing documents, proprietary notices, trademark language, governance language, citation metadata, copyright statements, and public documentation.

The purpose of migration is to establish a coherent current licensing architecture without erasing the evidence of how the repository was historically represented.

### 40.1 Migration Principles

All future alignment work should follow these principles:

1. preserve historical evidence;
2. distinguish current policy from historical policy;
3. avoid silent retroactive relicensing;
4. avoid unsupported ownership or exclusivity claims;
5. establish artifact-level licensing scope;
6. identify third-party rights before changing licensing representations;
7. use explicit supersession where a strategy document is replaced;
8. require legal review where legal effect cannot be determined architecturally;
9. require human approval before repository mutation;
10. verify every implemented change against the approved decision.

### 40.2 Current Artifacts Requiring Future Alignment Review

The following existing public-repository artifacts have been identified as requiring later alignment review:

* root `LICENSE`;
* `licensing/LICENSE`;
* `licensing/NOTICE`;
* `licensing/LICENSE_STRATEGY_v1.0.md`;
* `licensing/BBS_INSTITUTIONAL_LICENSE_v1.0.md`;
* `licensing/CORE_RUNTIME_PROPRIETARY_NOTICE_v1.0.md`;
* `TRADEMARK_POLICY.md`;
* `GOVERNANCE.md`;
* `CONTRIBUTING.md`;
* `CITATION.cff`;
* `legal/copyright.html`;
* and relevant public-facing documentation that describes ownership, licensing, project status, collaboration rights, or protected technology.

This list identifies review scope.

It does not authorize modification.

### 40.3 Root `LICENSE`

The root `LICENSE` currently contains Apache License 2.0.

Future alignment must not simply replace it without first determining:

* the scope historically associated with the root licence;
* which artifacts were distributed while it was present;
* whether public documentation represented the repository as Apache-licensed;
* whether specific files or directories contained conflicting or narrower terms;
* and what continuing rights may exist for historical versions.

Potential future options may include:

* retaining Apache licensing for specifically mapped artifacts;
* introducing a repository-level licensing index rather than a single universal licence;
* relocating historical licence evidence while preserving discoverability;
* or another legally reviewed approach.

No option is selected here.

### 40.4 `licensing/LICENSE`

The existing AGPLv3 licence in `licensing/LICENSE` must be reviewed against:

* historical Layer II positioning;
* actual artifacts that were intended to fall under that licence;
* public distribution history;
* current controlled-collaboration strategy;
* and any continuing historical rights.

The future controlled-collaboration model must not imply that all Layer II material is automatically AGPL.

At the same time, migration must not erase historical AGPL evidence or valid grants.

### 40.5 `licensing/NOTICE`

The current notice identifying the LEO Institutional Integration Layer and associating it with AGPLv3 requires alignment with the revised Layer II model.

Future treatment should distinguish:

* historical statement;
* current policy;
* applicable artifacts;
* and effective scope.

If superseded, the supersession must be explicit.

### 40.6 `LICENSE_STRATEGY_v1.0.md`

The historical strategy document requires substantial review because its three-layer model uses licensing assignments that are no longer accepted as automatic defaults.

In particular:

* Layer I must not automatically mean CC BY-NC-SA 4.0;
* Layer II must not automatically mean AGPLv3;
* Layer III protection must remain subject to actual ownership and historical rights;
* historical deterministic-system wording must be corrected prospectively;
* and the relationship between repository-level Apache licensing and the three-layer strategy must be resolved.

The preferred future approach is not silent overwrite.

A reviewed successor or explicit supersession mechanism should preserve the historical version.

### 40.7 `BBS_INSTITUTIONAL_LICENSE_v1.0.md`

This artifact requires legal review before it can be treated as part of a canonical current licensing framework.

Review should address, among other matters:

* who granted the rights;
* to whom;
* whether the agreement or licence is validly executed;
* whether exclusivity exists;
* whether sublicensing is permitted;
* whether commercial use is permitted;
* termination provisions;
* destruction obligations;
* post-termination rights;
* relationship to historical public licences;
* and the institutional authority of Fundacja BBS.

No legal conclusion is made here.

### 40.8 `CORE_RUNTIME_PROPRIETARY_NOTICE_v1.0.md`

This notice should later be reviewed for compatibility with:

* Layer III terminology;
* current LEO governance boundaries;
* current Process Mode architecture;
* historical public licensing;
* third-party components;
* and current terminology concerning enforcement-related capabilities.

Any stale or legally absolute wording should be revised only through an explicit versioned process.

### 40.9 `TRADEMARK_POLICY.md`

The trademark policy requires review because repository-wide Apache wording is inconsistent with the layered model.

Future alignment should separate:

* copyright licence;
* trademark use;
* official project identity;
* Foundation identity;
* derivative attribution;
* false endorsement;
* and permitted nominative use.

### 40.10 `GOVERNANCE.md`

Statements that imply Fundacja BBS owns protected core IP require review against the intended ownership model.

Future governance language should distinguish:

* original LEO ownership;
* Foundation institutional role;
* validly granted institutional rights;
* operational authority;
* and unresolved legal questions.

### 40.11 `CONTRIBUTING.md`

Contribution policy should later be reviewed for:

* contributor provenance;
* contributor authority;
* third-party material;
* contribution licensing;
* potential CLA/DCO requirements;
* AI-assisted contributions;
* and compatibility with the three-layer architecture.

### 40.12 `CITATION.cff`

Citation metadata should provide a clear licensing discovery path.

A generic reference to the licensing directory may remain insufficient if the repository contains multiple materially different licensing regimes.

Future alignment should make current licensing discovery understandable without erasing historical information.

### 40.13 `legal/copyright.html`

The legal copyright page requires review because it contains statements concerning:

* Foundation-owned website content;
* founder ownership of LEO;
* Foundation licensing;
* and potentially conflicting exclusivity language elsewhere in the repository.

Future alignment must preserve distinctions between:

* website content;
* LEO technology;
* Foundation-created material;
* founder-created material;
* third-party material;
* and valid institutional licences.

---

## 41. Controlled Migration Sequence

Migration should occur in a deliberate order.

A recommended sequence is:

### Phase 1 — Canonical Model Review

Review this document as the architectural basis.

Confirm:

* ownership baseline;
* Foundation role;
* three-layer model;
* historical licensing treatment;
* legal-review boundaries;
* governance compatibility;
* and non-goals.

No existing licensing artifact should be changed before this checkpoint is accepted.

### Phase 2 — Artifact Inventory and Mapping

Create or approve a controlled artifact-to-license inventory.

The inventory should classify existing artifacts by:

* ownership;
* provenance;
* licensing history;
* intended layer;
* third-party content;
* legal-review requirements;
* and publication status.

This phase should remain evidence-based.

### Phase 3 — Legal Review of High-Risk Questions

Obtain professional legal review for issues that cannot be safely resolved through repository evidence alone.

Priority questions include:

* historical Foundation agreement;
* exclusivity;
* founder/Foundation contracting mechanism;
* historical Apache and AGPL effect;
* institutional sublicensing;
* commercial restrictions;
* and any proposed relicensing of historically distributed artifacts.

### Phase 4 — Current Policy Design

Based on evidence and legal review, define:

* current repository licensing entry point;
* artifact-level licence mapping;
* Layer I licence choices by artifact class;
* Layer II licensing mechanisms;
* Layer III proprietary notices;
* trademark boundaries;
* contributor terms;
* and third-party notice requirements.

### Phase 5 — Individual Artifact Alignment

Modify individual licensing artifacts one controlled item at a time.

Each modification should:

* identify the reason;
* preserve historical provenance;
* state supersession where relevant;
* avoid unrelated changes;
* receive human approval;
* and be verified after editing.

### Phase 6 — Public Documentation Alignment

Once licensing artifacts are coherent, review public documentation for consistency.

Public-facing documents should accurately describe:

* ownership;
* licensing layers;
* open-source status where applicable;
* controlled collaboration;
* protected core technology;
* Foundation role;
* and evaluation boundaries.

### Phase 7 — Final Publication-Readiness Review

Before publication, perform a final cross-document review covering:

* licensing consistency;
* ownership consistency;
* provenance;
* third-party obligations;
* security disclosure;
* governance boundaries;
* Process Mode compatibility;
* public claims;
* and repository state.

### Phase 8 — Explicit Human Publication Approval

No push or publication should occur merely because the documentation review passes.

Publication requires explicit human approval.

### Phase 9 — Publication

Only the specifically approved changes should be:

* staged;
* reviewed;
* committed;
* pushed;
* or otherwise published.

### Phase 10 — Post-Publication Verification

After publication, perform verification against the public repository.

Verification should confirm:

* expected commit state;
* expected files;
* licensing discovery path;
* links;
* public rendering;
* absence of unintended changes;
* and consistency with the approved publication state.

---

## 42. Publication-Readiness Implications

The current licensing inconsistency is a material public-evaluation-readiness issue.

LEO may have strong technical and governance documentation while still presenting an unclear rights model to:

* evaluators;
* researchers;
* institutions;
* contributors;
* commercial partners;
* and public users.

That ambiguity can undermine confidence even when the underlying project governance is sound.

### 42.1 Publication Readiness Requires Licensing Discoverability

A public evaluator should be able to determine, without guessing:

* what is publicly licensed;
* what is controlled;
* what is proprietary;
* what is third-party material;
* who is identified as the original rights holder;
* what role Fundacja BBS has;
* and where unresolved legal questions remain.

### 42.2 Public Claims Must Match Legal and Licensing Reality

Public documentation must not create a stronger claim than the evidence supports.

Examples of claims that require particular caution include:

* "open source";
* "Apache licensed";
* "AGPL licensed";
* "exclusive licensee";
* "owned by Fundacja BBS";
* "fully compliant";
* "commercial use prohibited";
* or "all rights reserved".

Each such statement must have a defined artifact scope and supporting rights basis.

### 42.3 Licensing Readiness Is Separate From Runtime Readiness

A completed or frozen runtime baseline does not establish licensing readiness.

Likewise, a coherent licensing model does not establish production readiness.

These are separate review dimensions.

---

## 43. Architectural Risks Assessment

The following risks are currently material to the LEO licensing architecture.

### 43.1 Conflicting Repository-Level Licensing Signals

**Risk:** HIGH

The coexistence of root Apache licensing, AGPL material, proprietary notices, institutional terms, and other strategy statements can cause users to misunderstand applicable rights.

**Required response:** artifact-level mapping and explicit current licensing entry point.

### 43.2 Historical Grant Mischaracterization

**Risk:** HIGH

A migration process that treats historical public licences as if they never existed could create legal and provenance problems.

**Required response:** preserve historical evidence and distinguish prospective policy from historical grants.

### 43.3 Foundation Ownership / Exclusivity Misstatement

**Risk:** HIGH

Representing Fundacja BBS as original owner or legally verified exclusive licensee without sufficient evidence could misstate the intended ownership model and unresolved legal position.

**Required response:** use limited, evidence-based institutional-role language pending legal review.

### 43.4 Founder / Foundation Contracting Validity

**Risk:** HIGH — LEGAL REVIEW REQUIRED

The validity and appropriate mechanism for a licensing arrangement between Pavlo Martseniuk and Fundacja BBS cannot be established by this document.

**Required response:** professional Polish-law review.

### 43.5 Third-Party Licensing Gaps

**Risk:** MEDIUM TO HIGH, DEPENDING ON ARTIFACT

Incomplete dependency or external-material provenance may create redistribution risk.

**Required response:** controlled third-party inventory and compatibility review before affected publication.

### 43.6 False Open-Source Characterization

**Risk:** HIGH

Calling restricted Layer II material open source where authorization or commercial restrictions apply could be misleading.

**Required response:** use precise terminology distinguishing public source, controlled source, open source, and proprietary source.

### 43.7 Security-Sensitive Disclosure

**Risk:** HIGH FOR AFFECTED ARTIFACTS

Publication of protected implementation may expose security-sensitive mechanisms.

**Required response:** security review and minimum-necessary disclosure.

### 43.8 Over-Restriction of Historically Licensed Material

**Risk:** HIGH

A new proprietary classification may be incorrectly applied to material that remains subject to valid public rights.

**Required response:** version-specific rights analysis and legal review where necessary.

### 43.9 Licensing / Governance Architecture Drift

**Risk:** MEDIUM

Future licensing documents could revert to stale deterministic-system wording or imply enforcement authority inconsistent with current LEO governance.

**Required response:** architectural continuity review before adoption.

### 43.10 Provenance Loss During Cleanup

**Risk:** HIGH

Deleting or rewriting historical licensing artifacts during alignment could destroy evidence required for future rights analysis.

**Required response:** no silent deletion; use versioning, supersession, and archival preservation.

### 43.11 Commercial Ambiguity

**Risk:** MEDIUM TO HIGH

Unclear commercial-use permissions may discourage legitimate partners or permit unsupported assumptions.

**Required response:** explicit artifact-level commercial status.

### 43.12 Contributor Rights Ambiguity

**Risk:** MEDIUM, INCREASING WITH EXTERNAL CONTRIBUTIONS

Without contributor-rights governance, future relicensing or distribution may become difficult.

**Required response:** establish a reviewed contribution mechanism before significant external contribution expansion.

---

## 44. Implementation Readiness Assessment

### 44.1 Architectural Readiness

**Assessment: READY FOR CONTROLLED REVIEW**

The architectural licensing model is sufficiently defined to serve as a basis for the next evidence and legal-review phase.

It establishes:

* ownership versus licensing distinction;
* Foundation role boundary;
* three-layer architecture;
* public versus controlled versus protected access;
* artifact-level licensing requirement;
* historical licensing preservation;
* human review;
* legal-review gates;
* and migration controls.

### 44.2 Legal Readiness

**Assessment: NOT YET READY FOR FINAL LEGAL ADOPTION**

Material legal questions remain unresolved.

These include:

* historical Foundation agreement validity;
* exclusivity;
* founder/Foundation representation;
* historical public licence effects;
* sublicensing;
* relicensing authority;
* and potentially third-party rights.

Professional legal review remains necessary.

### 44.3 Repository Migration Readiness

**Assessment: NOT YET AUTHORIZED**

This document does not authorize modification of existing licensing files.

The next phase should establish and review the artifact-level mapping and legal questions before repository-wide alignment begins.

### 44.4 Public Publication Readiness

**Assessment: NOT YET COMPLETE**

The public repository should not be considered licensing-aligned until:

* current licensing entry points are coherent;
* artifact scope is discoverable;
* ownership language is consistent;
* Foundation language is legally safe;
* historical rights are preserved;
* and final publication-readiness review passes.

### 44.5 Automation Readiness

**Assessment: ADVISORY TOOLING ONLY**

Future tooling may assist with:

* licence discovery;
* provenance checks;
* dependency inventories;
* conflicting-statement detection;
* mapping validation;
* and release verification.

No autonomous licensing mutation or enforcement is authorized.

---

## 45. Formal Review Decision

### Decision

**PASS AS ARCHITECTURAL BASIS WITH MANDATORY LEGAL AND ARTIFACT-LEVEL REVIEW BEFORE IMPLEMENTATION**

### 45.1 Rationale

The model resolves the principal architectural problem identified in the current public repository:

LEO cannot be coherently governed through a single undifferentiated repository-wide licensing assumption while simultaneously maintaining public evaluation material, controlled collaboration, protected core technology, historical public licensing evidence, institutional use, third-party rights, and human-controlled governance.

The three-layer model provides a coherent prospective architecture while preserving artifact-level licensing as the actual rights-control mechanism.

The model also explicitly avoids unsupported conclusions concerning:

* Foundation ownership;
* exclusivity;
* historical agreement validity;
* regulatory compliance;
* automatic AGPL application;
* automatic Creative Commons application;
* repository-wide Apache application;
* retroactive revocation;
* or legal authority.

### 45.2 Conditions of the Decision

This PASS is conditional on the following:

1. this document is treated as architectural governance, not legal advice;
2. existing licensing artifacts remain unchanged until separately approved;
3. historical licensing evidence is preserved;
4. legal-review gates are respected;
5. artifact-level mapping precedes broad relicensing or publication claims;
6. no historical rights are silently erased;
7. no Foundation exclusivity claim is made without legal evidence;
8. no unsupported regulatory-compliance claim is introduced;
9. human review remains mandatory;
10. no autonomous enforcement or production mutation is authorized.

---

## 46. Architectural Continuity Statement

This licensing model is compatible with the current LEO architectural direction.

It preserves the core governance principles that:

* source evidence must remain traceable;
* provenance must be preserved;
* institutional memory must retain historical states;
* human review is mandatory for consequential decisions;
* analytical capability does not create institutional authority;
* anomaly detection does not create a fraud verdict;
* technical analysis does not create a legal verdict;
* process-mode proposals remain subject to human review;
* no autonomous enforcement is authorized;
* no autonomous production mutation is authorized;
* and historical evidence must not be silently destroyed to simplify a current narrative.

The licensing model also remains compatible with the current Process Mode architecture:

**SOURCE EVIDENCE
-> EVIDENCE-DERIVED CHARACTERISTICS
-> SIGNAL ELIGIBILITY
-> DETERMINISTIC / STOCHASTIC SIGNAL COUNTS
-> PROCESS MODE PROPOSAL
-> HUMAN REVIEW**

The four current Process Mode states remain unchanged:

* `DETERMINISTIC_PROCESS`
* `STOCHASTIC_PROCESS`
* `MIXED_PROCESS`
* `UNKNOWN_REQUIRES_REVIEW`

Nothing in this licensing model modifies that runtime architecture.

Nothing in the Process Mode architecture automatically determines licensing status.

The licensing architecture and Process Mode architecture remain separate but governance-compatible layers.

---

## 47. Current Canonical Licensing Architecture Summary

The intended prospective model is:

### LEO Original Rights Holder

**Pavlo Martseniuk**
Author / Developer / Original Rights Holder

subject to identifiable third-party rights and contribution-specific rights.

### Fundacja BBS — Better Balance System

Institutional licensee and/or operator only within rights validly granted to it.

No current legally verified exclusivity claim is established by this document.

### Layer I — Public Knowledge & Evaluation

Purpose:

* public understanding;
* evaluation;
* research;
* education;
* citation;
* architectural transparency;
* and societal benefit.

Exact licences must be assigned explicitly by artifact or artifact class.

### Layer II — Controlled Collaboration & Integration

Purpose:

* research collaboration;
* evaluation;
* institutional pilots;
* technical integration;
* approved development;
* and authorized commercial collaboration where applicable.

Layer II is not automatically open source.

Layer II is not automatically AGPL.

Rights must be explicitly defined.

### Layer III — Protected Core Technology

Purpose:

* protection of security-sensitive code;
* governance-critical runtime;
* protected algorithms;
* internal security mechanisms;
* and other protected implementation.

Prospective default:

**PROPRIETARY / ALL RIGHTS RESERVED**

subject to historical grants, third-party rights, and artifact-specific review.

### Historical Licensing

Apache, AGPL, Creative Commons, institutional, proprietary, and other historical licensing evidence must be preserved.

No silent retroactive relicensing.

### Governance

Human review required.

No autonomous enforcement.

No fraud verdict authority.

No legal verdict authority.

No production mutation merely because technical capability exists.

Provenance and evidence lineage must be preserved.

---

## 48. Next Authorized Phase

The next authorized phase following review of this document is:

**ARTIFACT-LEVEL LICENSING AND RIGHTS MAPPING REVIEW**

This phase should initially be **READ-ONLY**.

Its purpose is to create or review a structured mapping for the existing licensing-related artifacts without modifying them.

The review should establish, for each material artifact:

* current path;
* current licensing statement;
* historical licensing relevance;
* intended future layer;
* known rights holder;
* third-party considerations;
* conflict status;
* legal-review requirement;
* proposed current status;
* and evidence references.

Priority artifacts are:

1. root `LICENSE`;
2. `licensing/LICENSE`;
3. `licensing/NOTICE`;
4. `licensing/LICENSE_STRATEGY_v1.0.md`;
5. `licensing/BBS_INSTITUTIONAL_LICENSE_v1.0.md`;
6. `licensing/CORE_RUNTIME_PROPRIETARY_NOTICE_v1.0.md`;
7. `TRADEMARK_POLICY.md`;
8. `GOVERNANCE.md`;
9. `CONTRIBUTING.md`;
10. `CITATION.cff`;
11. `legal/copyright.html`.

No mutation is authorized merely by entering that phase.

After the mapping review, the project should stop for explicit human approval before any existing licensing artifact is edited.

---

## 49. Final Status Declaration

**Document:** `LEO_IP_AND_LICENSING_MODEL_v1.0.md`

**Architectural Status:** COMPLETE FOR REVIEW

**Legal Status:** REQUIRES PROFESSIONAL LEGAL REVIEW FOR IDENTIFIED LEGAL QUESTIONS

**Existing Licensing Artifact Mutation:** NOT AUTHORIZED

**Repository Staging:** NOT AUTHORIZED

**Commit:** NOT AUTHORIZED

**Push:** NOT AUTHORIZED

**Historical Evidence Preservation:** REQUIRED

**Artifact-Level Licensing Mapping:** REQUIRED NEXT

**Human Review:** REQUIRED

**Autonomous Enforcement:** PROHIBITED

**Fraud Verdict Authority:** NOT GRANTED

**Legal Verdict Authority:** NOT GRANTED

**Autonomous Production Mutation:** NOT GRANTED

**Next Authorized Phase:** ARTIFACT-LEVEL LICENSING AND RIGHTS MAPPING REVIEW — READ-ONLY FIRST

---

**END OF DOCUMENT**
