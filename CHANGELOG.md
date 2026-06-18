# Changelog

All notable public-facing changes to the LEO (Logical Epistemic Oversight) public repository are documented in this file.

The format follows the spirit of Keep a Changelog and is maintained as a human-readable public release record.

---

## [1.0.1] - 2026-06-18

### Added

- Added `PUBLIC_DEMO_CATALOG.md` as the canonical public navigation entry point for LEO demonstration repositories.
- Added public catalog visibility for three demonstration tracks:
  - Institutional Approval Review
  - Procurement / Accounting Review
  - Grant Expense Review

### Changed

- Updated `README.md` to present the public demonstration portfolio instead of a single public MVP demo.
- Updated `index.html` landing page to show all three public demonstration tracks.
- Replaced the Institutional Approval Review landing-page link from the previous feature branch URL to the current `main` branch path.
- Added Grant Expense Review visibility to the public landing page.

### Documentation

- Clarified that public demonstrations remain human-review-only.
- Preserved explicit safety boundaries:
  - no autonomous approval;
  - no autonomous rejection;
  - no fraud determinations;
  - no legal conclusions;
  - no production mutation;
  - no autonomous enforcement.

### Evidence Notes

- Existing Institutional Approval Review documentation references a documented runtime baseline of `2451 passed in 56.87s`.
- The runtime baseline is treated as a documented test baseline reference, not as a general production-readiness claim.

---

## [1.0.0] - 2026-06-17

### Added

- Published the Institutional Approval Review public MVP demo.
- Added reviewer-facing dashboard materials for local evidence review.
- Added public demonstration materials for institutional approval review workflow.
- Added local input datasets, generated output artifacts, validation scripts, and human-review package materials for the Institutional Approval Review demo.
- Added documentation describing human-in-the-loop operation and zero-autonomy boundaries.

### Notes

- This release was a public MVP/research demonstration release.
- It did not represent production deployment.
- It did not grant LEO autonomous decision-making, enforcement, approval, rejection, legal, or fraud-determination authority.

---

## [0.1.0] - 2025-11-08

### Added

- Initial LEO conceptual architecture.
- Initial public research structure and governance documentation.
- Initial legal, licensing, contribution, security, and trademark documentation.

---

## Public Boundary

LEO is a research-oriented institutional integrity and evidence-review project.

Public demonstrations are provided for inspection, testing, and review of demonstrated capabilities and operational boundaries.

LEO does not replace institutional authority or legal decision-making.