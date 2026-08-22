"""Evidence lineage validation for KnowledgeIntegrationRecord objects.

This module performs deterministic, read-only structural validation of the
evidence lineage and provenance references carried by a
KnowledgeIntegrationRecord.

The validator does not resolve external artifacts, infer provenance, verify
the truth of evidence, classify content, mutate records, or produce legal,
fraud, compliance, approval, rejection, or enforcement decisions.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)


@dataclass(frozen=True)
class EvidenceLineageValidationIssue:
    """A read-only structural validation issue."""

    issue_type: str
    message: str
    field_name: str


@dataclass(frozen=True)
class EvidenceLineageValidationResult:
    """Immutable evidence lineage validation result."""

    is_valid: bool
    explicit_unknown_fields: tuple[str, ...] = field(default_factory=tuple)
    issues: tuple[EvidenceLineageValidationIssue, ...] = field(default_factory=tuple)

    @property
    def requires_human_review(self) -> bool:
        """Return True when validation found unresolved or invalid references."""

        return not self.is_valid or bool(self.explicit_unknown_fields)

    @property
    def is_enforcement_output(self) -> bool:
        """Return False because validation is review support only."""

        return False

    @property
    def is_fraud_verdict(self) -> bool:
        """Return False because validation never produces a fraud verdict."""

        return False

    @property
    def mutates_production(self) -> bool:
        """Return False because validation is read-only."""

        return False


class EvidenceLineageValidator:
    """Validate explicit lineage references without resolving their targets."""

    REQUIRED_REFERENCE_FIELDS: tuple[str, ...] = (
        "evidence_lineage_reference",
        "provenance_reference",
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
    ) -> EvidenceLineageValidationResult:
        """Validate lineage-related fields on a KnowledgeIntegrationRecord."""

        if not isinstance(record, KnowledgeIntegrationRecord):
            raise TypeError("record must be a KnowledgeIntegrationRecord")

        explicit_unknown_fields: list[str] = []
        issues: list[EvidenceLineageValidationIssue] = []

        for field_name in self.REQUIRED_REFERENCE_FIELDS:
            value = getattr(record, field_name)

            if value in self.EXPLICIT_UNKNOWN_VALUES:
                explicit_unknown_fields.append(field_name)
                issues.append(
                    EvidenceLineageValidationIssue(
                        issue_type="explicit_unknown_reference",
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
                    EvidenceLineageValidationIssue(
                        issue_type="reference_whitespace_not_normalized",
                        message=(
                            f"{field_name} must not contain leading or "
                            "trailing whitespace"
                        ),
                        field_name=field_name,
                    )
                )

        return EvidenceLineageValidationResult(
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
        """Return False because target resolution belongs to another component."""

        return False

    @property
    def creates_autonomous_decision(self) -> bool:
        """Return False because the validator does not make decisions."""

        return False
