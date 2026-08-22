"""Validate Knowledge Layer implementation contracts before record construction."""

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)


__all__ = [
    "ImplementationContractValidationIssue",
    "ImplementationContractValidationResult",
    "ImplementationContractValidator",
]


_REQUIRED_FIELDS: tuple[str, ...] = (
    "integration_record_id",
    "integration_record_version",
    "integration_record_status",
    "created_at",
    "source_artifact_path",
    "source_artifact_type",
    "source_artifact_status",
    "source_artifact_commit",
    "referenced_runtime_layer",
    "referenced_runtime_output_path",
    "ontology_concept_reference",
    "knowledge_architecture_reference",
    "institutional_memory_reference",
    "evidence_lineage_reference",
    "provenance_reference",
    "public_evaluation_relevance",
    "human_review_required",
)

_REQUIRED_TEXT_FIELDS: tuple[str, ...] = (
    "integration_record_id",
    "integration_record_version",
    "created_at",
    "source_artifact_path",
    "source_artifact_type",
    "source_artifact_status",
    "source_artifact_commit",
    "referenced_runtime_layer",
    "referenced_runtime_output_path",
    "ontology_concept_reference",
    "knowledge_architecture_reference",
    "institutional_memory_reference",
    "evidence_lineage_reference",
    "provenance_reference",
    "public_evaluation_relevance",
)

_LIST_FIELDS: tuple[str, ...] = (
    "implementation_limitations",
    "reviewer_notes",
)


@dataclass(frozen=True)
class ImplementationContractValidationIssue:
    """Represent one immutable implementation contract validation issue."""

    issue_type: str
    message: str
    field_name: str | None = None


@dataclass(frozen=True)
class ImplementationContractValidationResult:
    """Represent the immutable outcome of implementation contract validation."""

    is_valid: bool
    issues: tuple[ImplementationContractValidationIssue, ...] = field(
        default_factory=tuple
    )

    @property
    def requires_human_review(self) -> bool:
        """Return True when implementation contract issues require review."""

        return not self.is_valid or bool(self.issues)

    @property
    def is_review_support_only(self) -> bool:
        """Return True because contract validation supports human review."""

        return True

    @property
    def is_enforcement_output(self) -> bool:
        """Return False because contract validation is not enforcement."""

        return False

    @property
    def is_fraud_verdict(self) -> bool:
        """Return False because contract validation is not a fraud verdict."""

        return False

    @property
    def is_legal_verdict(self) -> bool:
        """Return False because contract validation is not a legal verdict."""

        return False

    @property
    def mutates_production(self) -> bool:
        """Return False because contract validation is read-only."""

        return False

    @property
    def creates_autonomous_decision(self) -> bool:
        """Return False because contract validation does not make decisions."""

        return False


class ImplementationContractValidator:
    """Validate an initial mapping against the implementation contract."""

    REQUIRED_FIELDS: tuple[str, ...] = _REQUIRED_FIELDS
    REQUIRED_TEXT_FIELDS: tuple[str, ...] = _REQUIRED_TEXT_FIELDS
    LIST_FIELDS: tuple[str, ...] = _LIST_FIELDS

    def validate(
        self,
        initial_mapping: Mapping[str, Any],
    ) -> ImplementationContractValidationResult:
        """Validate an initial mapping against the implementation contract."""

        if not isinstance(initial_mapping, Mapping):
            raise TypeError("initial_mapping must be a mapping")

        issues: list[ImplementationContractValidationIssue] = []
        allowed_fields = set(KnowledgeIntegrationRecord.__dataclass_fields__)

        field_names = tuple(initial_mapping.keys())

        for field_name in field_names:
            if not isinstance(field_name, str):
                issues.append(
                    ImplementationContractValidationIssue(
                        issue_type="invalid_field_name",
                        message="Implementation contract field names must be strings.",
                    )
                )
                continue

            if field_name not in allowed_fields:
                issues.append(
                    ImplementationContractValidationIssue(
                        issue_type="unsupported_field",
                        message=(
                            "Unsupported KnowledgeIntegrationRecord field: "
                            f"{field_name}"
                        ),
                        field_name=field_name,
                    )
                )

        for field_name in self.REQUIRED_FIELDS:
            if field_name not in initial_mapping:
                issues.append(
                    ImplementationContractValidationIssue(
                        issue_type="missing_required_field",
                        message=(
                            "Required KnowledgeIntegrationRecord field is missing: "
                            f"{field_name}"
                        ),
                        field_name=field_name,
                    )
                )

        self._validate_status(initial_mapping, issues)
        self._validate_human_review(initial_mapping, issues)
        self._validate_text_fields(initial_mapping, issues)
        self._validate_list_fields(initial_mapping, issues)

        immutable_issues = tuple(issues)

        return ImplementationContractValidationResult(
            is_valid=not immutable_issues,
            issues=immutable_issues,
        )

    def _validate_status(
        self,
        initial_mapping: Mapping[str, Any],
        issues: list[ImplementationContractValidationIssue],
    ) -> None:
        """Validate the explicit integration record status when supplied."""

        field_name = "integration_record_status"

        if field_name not in initial_mapping:
            return

        value = initial_mapping[field_name]

        if not isinstance(value, str):
            issues.append(
                ImplementationContractValidationIssue(
                    issue_type="invalid_field_type",
                    message="integration_record_status must be a string",
                    field_name=field_name,
                )
            )
            return

        if value not in KnowledgeIntegrationRecord.ALLOWED_STATUSES:
            issues.append(
                ImplementationContractValidationIssue(
                    issue_type="invalid_status",
                    message=(
                        "integration_record_status must be one of the approved "
                        "KnowledgeIntegrationRecord status values"
                    ),
                    field_name=field_name,
                )
            )

    def _validate_human_review(
        self,
        initial_mapping: Mapping[str, Any],
        issues: list[ImplementationContractValidationIssue],
    ) -> None:
        """Validate the mandatory human-review contract when supplied."""

        field_name = "human_review_required"

        if field_name not in initial_mapping:
            return

        value = initial_mapping[field_name]

        if value is not True:
            issues.append(
                ImplementationContractValidationIssue(
                    issue_type="human_review_not_required",
                    message="human_review_required must be True",
                    field_name=field_name,
                )
            )

    def _validate_text_fields(
        self,
        initial_mapping: Mapping[str, Any],
        issues: list[ImplementationContractValidationIssue],
    ) -> None:
        """Validate required text fields that are explicitly supplied."""

        for field_name in self.REQUIRED_TEXT_FIELDS:
            if field_name not in initial_mapping:
                continue

            value = initial_mapping[field_name]

            if not isinstance(value, str):
                issues.append(
                    ImplementationContractValidationIssue(
                        issue_type="invalid_field_type",
                        message=f"{field_name} must be a string",
                        field_name=field_name,
                    )
                )
                continue

            if value == "":
                issues.append(
                    ImplementationContractValidationIssue(
                        issue_type="empty_required_text_field",
                        message=(
                            f"{field_name} must not be empty; use missing, "
                            "unknown, or not_applicable when the value is "
                            "unavailable"
                        ),
                        field_name=field_name,
                    )
                )

    def _validate_list_fields(
        self,
        initial_mapping: Mapping[str, Any],
        issues: list[ImplementationContractValidationIssue],
    ) -> None:
        """Validate optional list fields when explicitly supplied."""

        for field_name in self.LIST_FIELDS:
            if field_name not in initial_mapping:
                continue

            value = initial_mapping[field_name]

            if not isinstance(value, list):
                issues.append(
                    ImplementationContractValidationIssue(
                        issue_type="invalid_list_field",
                        message=f"{field_name} must be a list",
                        field_name=field_name,
                    )
                )
                continue

            for item in value:
                if not isinstance(item, str):
                    issues.append(
                        ImplementationContractValidationIssue(
                            issue_type="invalid_list_item",
                            message=f"{field_name} must contain strings only",
                            field_name=field_name,
                        )
                    )

    @property
    def is_review_support_only(self) -> bool:
        """Return True because validation only supports human review."""

        return True

    @property
    def mutates_input(self) -> bool:
        """Return False because validation does not mutate input mappings."""

        return False

    @property
    def mutates_production(self) -> bool:
        """Return False because validation does not mutate production."""

        return False

    @property
    def inspects_repository_state(self) -> bool:
        """Return False because validation uses only supplied values."""

        return False

    @property
    def infers_missing_information(self) -> bool:
        """Return False because validation does not infer missing values."""

        return False

    @property
    def creates_autonomous_decision(self) -> bool:
        """Return False because validation does not create decisions."""

        return False
