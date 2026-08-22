"""Structural provenance validation for KnowledgeIntegrationRecord objects.

This module performs deterministic, read-only validation of provenance-related
fields already carried by a KnowledgeIntegrationRecord.

The validator does not inspect repository state, resolve external artifacts,
infer missing provenance, determine canonical authority, determine archive
status, mutate records, or produce legal, fraud, compliance, approval,
rejection, or enforcement decisions.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)


@dataclass(frozen=True)
class ProvenanceValidationIssue:
    """A read-only structural provenance validation issue."""

    issue_type: str
    message: str
    field_name: str


@dataclass(frozen=True)
class ProvenanceValidationResult:
    """Immutable structural provenance validation result."""

    is_valid: bool
    explicit_unknown_fields: tuple[str, ...] = field(default_factory=tuple)
    issues: tuple[ProvenanceValidationIssue, ...] = field(default_factory=tuple)

    @property
    def requires_human_review(self) -> bool:
        """Return True when provenance remains unresolved or invalid."""

        return not self.is_valid or bool(self.explicit_unknown_fields)

    @property
    def is_review_support_only(self) -> bool:
        """Return True because validation supports human review."""

        return True

    @property
    def is_enforcement_output(self) -> bool:
        """Return False because provenance validation is not enforcement."""

        return False

    @property
    def is_fraud_verdict(self) -> bool:
        """Return False because provenance validation is not a fraud verdict."""

        return False

    @property
    def is_legal_verdict(self) -> bool:
        """Return False because provenance validation is not a legal verdict."""

        return False

    @property
    def mutates_production(self) -> bool:
        """Return False because validation is read-only."""

        return False


class ProvenanceValidator:
    """Validate explicit provenance-related record fields structurally."""

    PROVENANCE_FIELDS: tuple[str, ...] = (
        "provenance_reference",
        "source_artifact_path",
        "source_artifact_status",
        "source_artifact_commit",
        "integration_record_status",
    )

    EXPLICIT_UNKNOWN_VALUES: frozenset[str] = frozenset(
        {
            "missing",
            "unknown",
            "not_applicable",
        }
    )

    def validate(
        self,
        record: KnowledgeIntegrationRecord,
    ) -> ProvenanceValidationResult:
        """Validate available provenance-related fields without inference."""

        if not isinstance(record, KnowledgeIntegrationRecord):
            raise TypeError("record must be a KnowledgeIntegrationRecord")

        explicit_unknown_fields: list[str] = []
        issues: list[ProvenanceValidationIssue] = []

        for field_name in self.PROVENANCE_FIELDS:
            value = getattr(record, field_name)

            if value in self.EXPLICIT_UNKNOWN_VALUES:
                explicit_unknown_fields.append(field_name)
                issues.append(
                    ProvenanceValidationIssue(
                        issue_type="explicit_unknown_provenance",
                        message=(
                            f"{field_name} uses an explicit unknown marker "
                            f"and requires human review: {value}"
                        ),
                        field_name=field_name,
                    )
                )
                continue

            if value != value.strip():
                issues.append(
                    ProvenanceValidationIssue(
                        issue_type="provenance_whitespace_not_normalized",
                        message=(
                            f"{field_name} must not contain leading or "
                            "trailing whitespace"
                        ),
                        field_name=field_name,
                    )
                )

        return ProvenanceValidationResult(
            is_valid=not issues,
            explicit_unknown_fields=tuple(explicit_unknown_fields),
            issues=tuple(issues),
        )

    @property
    def is_review_support_only(self) -> bool:
        """Return True because the validator supports human review."""

        return True

    @property
    def mutates_record(self) -> bool:
        """Return False because the validator never changes records."""

        return False

    @property
    def resolves_external_references(self) -> bool:
        """Return False because external resolution belongs to another component."""

        return False

    @property
    def inspects_repository_state(self) -> bool:
        """Return False because repository inspection is outside this validator."""

        return False

    @property
    def infers_provenance(self) -> bool:
        """Return False because implicit provenance inference is prohibited."""

        return False

    @property
    def determines_canonical_status(self) -> bool:
        """Return False because canonical status is not explicit in the record."""

        return False

    @property
    def determines_archive_status(self) -> bool:
        """Return False because archive status is not explicit in the record."""

        return False

    @property
    def creates_autonomous_decision(self) -> bool:
        """Return False because the validator does not make decisions."""

        return False