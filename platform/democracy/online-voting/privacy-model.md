# Privacy Model — Secret Ballot, Public Integrity

Online voting must preserve two truths at the same time:

1) the system must prove that voting is legitimate,
2) the voter’s choice must remain secret.

This module follows a “system transparency, personal privacy” doctrine.

---

## Core Privacy Rules

- voter identity is never publicly linked to vote choice
- public proofs verify integrity, not private behavior
- observers can validate election results without deanonymizing voters
- any published data must be legally compliant with national and EU privacy standards

---

## Practical Outcomes

The system provides:
- confirmation that a vote was accepted (receipt)
- assurance that counting was not manipulated
- the ability to detect anomalies and fraud
without producing a public list of “who voted for whom”.

---

## Privacy-Preserving Verification (Public Overview)

The design supports:
- verifiable acceptance (a vote is recorded)
- verifiable inclusion (a vote is in the final tally)
- verifiable tally (results match the immutable snapshot)
while keeping:
- identity private,
- vote choice secret.

Detailed cryptographic mechanisms are not published in the public façade and are audit-released only
under controlled conditions.
