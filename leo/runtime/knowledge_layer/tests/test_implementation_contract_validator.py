from copy import deepcopy
from dataclasses import FrozenInstanceError

import pytest

from leo.runtime.knowledge_layer.implementation_contract_validator import (
    ImplementationContractValidationIssue,
    ImplementationContractValidationResult,
    ImplementationContractValidator,
)


def make_valid_mapping() -> dict[str, object]:
    return {
        "integration_record_id": "KIR-IMPLEMENTATION-CONTRACT-TEST-001",
        "integration_record_version": "0.1",
        "integration_record_status": "DRAFT",
        "created_at": "2026-07-23T00:00:00Z",
        "source_artifact_path": "foundation/engineering_ontology/example.md",
        "source_artifact_type": "reviewed_document",
        "source_artifact_status": "reviewed",
        "source_artifact_commit": "abcdef12",
        "referenced_runtime_layer": "leo/runtime/knowledge_layer",
        "referenced_runtime_output_path": "not_applicable",
        "ontology_concept_reference": (
            "LEO_ENGINEERING_ONTOLOGY_FOUNDATION.md"
        ),
        "knowledge_architecture_reference": "LEO_KNOWLEDGE_MODEL.md",
        "institutional_memory_reference": (
            "INSTITUTIONAL_MEMORY_REGISTRY.md"
        ),
        "evidence_lineage_reference": "EVIDENCE_LINEAGE_FRAMEWORK.md",
        "provenance_reference": "INSTITUTIONAL_MEMORY_PROVENANCE_MODEL.md",
        "public_evaluation_relevance": "review_support",
        "human_review_required": True,
        "implementation_limitations": [
            "Validation is limited to the supplied mapping.",
        ],
        "reviewer_notes": [
            "Human review remains required.",
        ],
    }


def test_valid_complete_mapping_passes_validation() -> None:
    validator = ImplementationContractValidator()
    initial_mapping = make_valid_mapping()
    original_mapping = deepcopy(initial_mapping)

    result = validator.validate(initial_mapping)

    assert isinstance(result, ImplementationContractValidationResult)
    assert result.is_valid is True
    assert result.issues == ()
    assert result.requires_human_review is False
    assert initial_mapping == original_mapping


def test_missing_required_fields_are_reported_together() -> None:
    validator = ImplementationContractValidator()
    initial_mapping = make_valid_mapping()
    del initial_mapping["integration_record_id"]
    del initial_mapping["provenance_reference"]

    result = validator.validate(initial_mapping)

    assert result.is_valid is False
    assert result.requires_human_review is True
    assert len(result.issues) == 2
    assert ImplementationContractValidationIssue(
        issue_type="missing_required_field",
        message=(
            "Required KnowledgeIntegrationRecord field is missing: "
            "integration_record_id"
        ),
        field_name="integration_record_id",
    ) in result.issues
    assert ImplementationContractValidationIssue(
        issue_type="missing_required_field",
        message=(
            "Required KnowledgeIntegrationRecord field is missing: "
            "provenance_reference"
        ),
        field_name="provenance_reference",
    ) in result.issues


def test_invalid_and_unsupported_field_names_are_reported() -> None:
    validator = ImplementationContractValidator()
    initial_mapping = make_valid_mapping()
    initial_mapping["unsupported_contract_field"] = "unexpected"
    initial_mapping[7] = "invalid-name"  # type: ignore[index]

    result = validator.validate(initial_mapping)

    assert result.is_valid is False
    assert result.requires_human_review is True
    assert ImplementationContractValidationIssue(
        issue_type="invalid_field_name",
        message="Implementation contract field names must be strings.",
    ) in result.issues
    assert ImplementationContractValidationIssue(
        issue_type="unsupported_field",
        message=(
            "Unsupported KnowledgeIntegrationRecord field: "
            "unsupported_contract_field"
        ),
        field_name="unsupported_contract_field",
    ) in result.issues


@pytest.mark.parametrize(
    ("value", "issue_type"),
    [
        (7, "invalid_field_type"),
        ("UNAPPROVED_STATUS", "invalid_status"),
    ],
)
def test_invalid_status_values_are_reported(
    value: object,
    issue_type: str,
) -> None:
    validator = ImplementationContractValidator()
    initial_mapping = make_valid_mapping()
    initial_mapping["integration_record_status"] = value

    result = validator.validate(initial_mapping)

    assert result.is_valid is False
    assert result.requires_human_review is True
    assert any(
        issue.issue_type == issue_type
        and issue.field_name == "integration_record_status"
        for issue in result.issues
    )


@pytest.mark.parametrize(
    "value",
    [
        False,
        None,
        1,
        "true",
    ],
)
def test_human_review_must_be_explicitly_true(value: object) -> None:
    validator = ImplementationContractValidator()
    initial_mapping = make_valid_mapping()
    initial_mapping["human_review_required"] = value

    result = validator.validate(initial_mapping)

    assert result.is_valid is False
    assert result.requires_human_review is True
    assert ImplementationContractValidationIssue(
        issue_type="human_review_not_required",
        message="human_review_required must be True",
        field_name="human_review_required",
    ) in result.issues


@pytest.mark.parametrize(
    ("field_name", "value"),
    [
        ("integration_record_id", 1),
        ("created_at", None),
        ("source_artifact_path", ["foundation/example.md"]),
        ("provenance_reference", {"reference": "example"}),
    ],
)
def test_required_text_fields_must_be_strings(
    field_name: str,
    value: object,
) -> None:
    validator = ImplementationContractValidator()
    initial_mapping = make_valid_mapping()
    initial_mapping[field_name] = value

    result = validator.validate(initial_mapping)

    assert result.is_valid is False
    assert result.requires_human_review is True
    assert ImplementationContractValidationIssue(
        issue_type="invalid_field_type",
        message=f"{field_name} must be a string",
        field_name=field_name,
    ) in result.issues


@pytest.mark.parametrize(
    "field_name",
    [
        "integration_record_id",
        "created_at",
        "source_artifact_path",
        "provenance_reference",
    ],
)
def test_empty_required_text_fields_are_reported(
    field_name: str,
) -> None:
    validator = ImplementationContractValidator()
    initial_mapping = make_valid_mapping()
    initial_mapping[field_name] = ""

    result = validator.validate(initial_mapping)

    assert result.is_valid is False
    assert result.requires_human_review is True
    assert ImplementationContractValidationIssue(
        issue_type="empty_required_text_field",
        message=(
            f"{field_name} must not be empty; use missing, "
            "unknown, or not_applicable when the value is unavailable"
        ),
        field_name=field_name,
    ) in result.issues


@pytest.mark.parametrize(
    ("field_name", "value", "issue_type"),
    [
        (
            "implementation_limitations",
            "not-a-list",
            "invalid_list_field",
        ),
        (
            "reviewer_notes",
            ("review note",),
            "invalid_list_field",
        ),
        (
            "implementation_limitations",
            ["valid limitation", 7],
            "invalid_list_item",
        ),
        (
            "reviewer_notes",
            [None],
            "invalid_list_item",
        ),
    ],
)
def test_optional_list_fields_must_be_lists_of_strings(
    field_name: str,
    value: object,
    issue_type: str,
) -> None:
    validator = ImplementationContractValidator()
    initial_mapping = make_valid_mapping()
    initial_mapping[field_name] = value

    result = validator.validate(initial_mapping)

    assert result.is_valid is False
    assert result.requires_human_review is True
    assert any(
        issue.issue_type == issue_type
        and issue.field_name == field_name
        for issue in result.issues
    )


def test_validator_rejects_non_mapping_input() -> None:
    validator = ImplementationContractValidator()

    with pytest.raises(
        TypeError,
        match="initial_mapping must be a mapping",
    ):
        validator.validate(  # type: ignore[arg-type]
            ["not", "a", "mapping"]
        )


def test_validation_result_is_immutable() -> None:
    validator = ImplementationContractValidator()
    result = validator.validate(make_valid_mapping())

    with pytest.raises(FrozenInstanceError):
        result.is_valid = False  # type: ignore[misc]


def test_validator_preserves_review_support_governance_boundaries() -> None:
    validator = ImplementationContractValidator()
    result = validator.validate(make_valid_mapping())

    assert validator.is_review_support_only is True
    assert validator.mutates_input is False
    assert validator.mutates_production is False
    assert validator.inspects_repository_state is False
    assert validator.infers_missing_information is False
    assert validator.creates_autonomous_decision is False

    assert result.is_review_support_only is True
    assert result.is_enforcement_output is False
    assert result.is_fraud_verdict is False
    assert result.is_legal_verdict is False
    assert result.mutates_production is False
    assert result.creates_autonomous_decision is False
