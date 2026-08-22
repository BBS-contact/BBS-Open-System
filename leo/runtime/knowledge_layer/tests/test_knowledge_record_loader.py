"""Tests for KnowledgeRecordLoader."""

from copy import deepcopy
from dataclasses import FrozenInstanceError
import json
from pathlib import Path

import pytest

from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)
from leo.runtime.knowledge_layer.knowledge_record_loader import (
    KnowledgeRecordLoader,
    KnowledgeRecordLoaderResult,
    KnowledgeRecordLoadingIssue,
)


def valid_record_data(
    *,
    integration_record_id: str = "KIR-LOADER-001",
) -> dict[str, object]:
    """Return one complete explicit Knowledge Layer record mapping."""

    return {
        "integration_record_id": integration_record_id,
        "integration_record_version": "0.1",
        "integration_record_status": "DRAFT",
        "created_at": "2026-07-19T00:00:00Z",
        "source_artifact_path": (
            "foundation/engineering_ontology/loader-test-source.md"
        ),
        "source_artifact_type": "reviewed_document",
        "source_artifact_status": "reviewed",
        "source_artifact_commit": "abcdef12",
        "referenced_runtime_layer": "leo/runtime/knowledge_layer",
        "referenced_runtime_output_path": "not_applicable",
        "ontology_concept_reference": (
            "knowledge_layer_runtime_integration"
        ),
        "knowledge_architecture_reference": "LEO_KNOWLEDGE_MODEL.md",
        "institutional_memory_reference": (
            "INSTITUTIONAL_MEMORY_REGISTRY.md"
        ),
        "evidence_lineage_reference": "EVIDENCE_LINEAGE_FRAMEWORK.md",
        "provenance_reference": (
            "INSTITUTIONAL_MEMORY_PROVENANCE_MODEL.md"
        ),
        "public_evaluation_relevance": "review_support",
        "human_review_required": True,
        "implementation_limitations": ["loader test only"],
        "reviewer_notes": ["explicit test record"],
    }


def write_json(path: Path, content: object) -> None:
    """Write deterministic UTF-8 JSON test content."""

    path.write_text(
        json.dumps(content, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def test_loader_loads_valid_single_json_file(tmp_path: Path) -> None:
    loader = KnowledgeRecordLoader()
    source_path = tmp_path / "record.json"
    write_json(source_path, valid_record_data())

    result = loader.load(source_path)

    assert isinstance(result, KnowledgeRecordLoaderResult)
    assert result.load_status == "LOAD_SUCCESSFUL"
    assert result.supported_format is True
    assert result.source_descriptor == "local_json_file"
    assert result.source_path == str(source_path)
    assert result.total_candidate_record_count == 1
    assert result.successfully_loaded_record_count == 1
    assert result.rejected_record_count == 0
    assert len(result.loaded_records) == 1
    assert result.loaded_records[0].integration_record_id == "KIR-LOADER-001"
    assert result.record_loading_issues == ()


def test_loader_reports_malformed_json(tmp_path: Path) -> None:
    loader = KnowledgeRecordLoader()
    source_path = tmp_path / "malformed.json"
    source_path.write_text('{"invalid": ', encoding="utf-8")

    result = loader.load(source_path)

    assert result.load_status == "MALFORMED_SERIALIZATION"
    assert result.supported_format is True
    assert result.loaded_records == ()
    assert result.total_candidate_record_count == 0
    assert result.successfully_loaded_record_count == 0
    assert result.rejected_record_count == 0
    assert len(result.record_loading_issues) == 1
    assert (
        result.record_loading_issues[0].issue_type
        == "MALFORMED_SERIALIZATION"
    )
    assert result.record_loading_issues[0].source_path == str(source_path)


def test_loader_reports_missing_file(tmp_path: Path) -> None:
    loader = KnowledgeRecordLoader()
    source_path = tmp_path / "missing.json"

    result = loader.load(source_path)

    assert result.load_status == "INPUT_NOT_FOUND"
    assert result.supported_format is False
    assert result.loaded_records == ()
    assert len(result.record_loading_issues) == 1
    assert result.record_loading_issues[0].issue_type == "INPUT_NOT_FOUND"
    assert result.record_loading_issues[0].source_path == str(source_path)


def test_loader_rejects_unsupported_file_extension(
    tmp_path: Path,
) -> None:
    loader = KnowledgeRecordLoader()
    source_path = tmp_path / "record.txt"
    source_path.write_text("not a supported record", encoding="utf-8")

    result = loader.load(source_path)

    assert result.load_status == "UNSUPPORTED_INPUT"
    assert result.supported_format is False
    assert result.loaded_records == ()
    assert len(result.record_loading_issues) == 1
    assert (
        result.record_loading_issues[0].issue_type
        == "UNSUPPORTED_FILE_FORMAT"
    )
    assert result.record_loading_issues[0].source_path == str(source_path)


def test_loader_loads_mixed_valid_and_invalid_directory_records(
    tmp_path: Path,
) -> None:
    loader = KnowledgeRecordLoader()
    source_directory = tmp_path / "records"
    source_directory.mkdir()

    valid_path = source_directory / "01-valid.json"
    invalid_path = source_directory / "02-invalid.json"

    write_json(
        valid_path,
        valid_record_data(integration_record_id="KIR-DIRECTORY-VALID"),
    )

    invalid_record = valid_record_data(
        integration_record_id="KIR-DIRECTORY-INVALID"
    )
    del invalid_record["provenance_reference"]
    write_json(invalid_path, invalid_record)

    result = loader.load(source_directory)

    assert result.load_status == "LOAD_PARTIALLY_SUCCESSFUL"
    assert result.supported_format is True
    assert result.source_descriptor == "local_json_directory"
    assert result.source_path == str(source_directory)
    assert result.total_candidate_record_count == 2
    assert result.successfully_loaded_record_count == 1
    assert result.rejected_record_count == 1
    assert len(result.loaded_records) == 1
    assert (
        result.loaded_records[0].integration_record_id
        == "KIR-DIRECTORY-VALID"
    )
    assert len(result.record_loading_issues) == 1
    assert (
        result.record_loading_issues[0].issue_type
        == "RECORD_CONSTRUCTION_FAILED"
    )
    assert (
        result.record_loading_issues[0].record_identifier
        == "KIR-DIRECTORY-INVALID"
    )
    assert result.record_loading_issues[0].source_path == str(invalid_path)


def test_loader_reports_inaccessible_input(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    loader = KnowledgeRecordLoader()
    source_path = tmp_path / "inaccessible.json"
    original_exists = Path.exists

    def controlled_exists(path: Path) -> bool:
        if path == source_path:
            raise OSError("controlled access failure")
        return original_exists(path)

    monkeypatch.setattr(Path, "exists", controlled_exists)

    result = loader.load(source_path)

    assert result.load_status == "INPUT_INACCESSIBLE"
    assert result.supported_format is False
    assert result.loaded_records == ()
    assert len(result.record_loading_issues) == 1
    assert (
        result.record_loading_issues[0].issue_type
        == "INPUT_INACCESSIBLE"
    )
    assert result.record_loading_issues[0].source_path == str(source_path)
    assert "controlled access failure" in result.record_loading_issues[0].message


def test_loader_preserves_source_identifier_in_loaded_record() -> None:
    loader = KnowledgeRecordLoader()
    source = valid_record_data(
        integration_record_id="KIR-PRESERVED-IDENTIFIER"
    )

    result = loader.load(source)

    assert result.load_status == "LOAD_SUCCESSFUL"
    assert (
        result.loaded_records[0].integration_record_id
        == "KIR-PRESERVED-IDENTIFIER"
    )


def test_loader_preserves_source_identifier_in_loading_issue() -> None:
    loader = KnowledgeRecordLoader()
    source = valid_record_data(
        integration_record_id="KIR-REJECTED-IDENTIFIER"
    )
    del source["provenance_reference"]

    result = loader.load(source)

    assert result.load_status == "LOAD_FAILED"
    assert result.loaded_records == ()
    assert len(result.record_loading_issues) == 1
    assert (
        result.record_loading_issues[0].record_identifier
        == "KIR-REJECTED-IDENTIFIER"
    )


def test_loader_does_not_mutate_source_mapping() -> None:
    loader = KnowledgeRecordLoader()
    source = valid_record_data()
    preserved_source = deepcopy(source)

    result = loader.load(source)

    assert result.load_status == "LOAD_SUCCESSFUL"
    assert source == preserved_source


def test_loader_loads_existing_record_without_reconstruction() -> None:
    loader = KnowledgeRecordLoader()
    record = KnowledgeIntegrationRecord(**valid_record_data())

    result = loader.load(record)

    assert result.load_status == "LOAD_SUCCESSFUL"
    assert result.loaded_records == (record,)
    assert result.loaded_records[0] is record
    assert result.source_descriptor == "knowledge_integration_record"


def test_loader_loads_valid_in_memory_mapping() -> None:
    loader = KnowledgeRecordLoader()
    source = valid_record_data()

    result = loader.load(source)

    assert result.load_status == "LOAD_SUCCESSFUL"
    assert result.source_descriptor == "in_memory_mapping"
    assert result.source_path is None
    assert result.supported_format is True
    assert result.total_candidate_record_count == 1
    assert result.successfully_loaded_record_count == 1
    assert result.rejected_record_count == 0


def test_loader_rejects_unsupported_input_type() -> None:
    loader = KnowledgeRecordLoader()

    result = loader.load(123)

    assert result.load_status == "UNSUPPORTED_INPUT"
    assert result.supported_format is False
    assert result.loaded_records == ()
    assert result.total_candidate_record_count == 0
    assert len(result.record_loading_issues) == 1
    assert (
        result.record_loading_issues[0].issue_type
        == "UNSUPPORTED_INPUT_TYPE"
    )


def test_loader_rejects_unsupported_serialized_root(
    tmp_path: Path,
) -> None:
    loader = KnowledgeRecordLoader()
    source_path = tmp_path / "unsupported-root.json"
    write_json(source_path, "not a record object")

    result = loader.load(source_path)

    assert result.load_status == "LOAD_FAILED"
    assert result.supported_format is True
    assert result.loaded_records == ()
    assert result.total_candidate_record_count == 1
    assert result.successfully_loaded_record_count == 0
    assert result.rejected_record_count == 1
    assert len(result.record_loading_issues) == 1
    assert (
        result.record_loading_issues[0].issue_type
        == "UNSUPPORTED_SERIALIZED_ROOT"
    )


def test_loader_rejects_non_object_candidate_in_json_array(
    tmp_path: Path,
) -> None:
    loader = KnowledgeRecordLoader()
    source_path = tmp_path / "mixed-array.json"
    write_json(
        source_path,
        [
            valid_record_data(
                integration_record_id="KIR-ARRAY-VALID"
            ),
            "not an object",
        ],
    )

    result = loader.load(source_path)

    assert result.load_status == "LOAD_PARTIALLY_SUCCESSFUL"
    assert result.total_candidate_record_count == 2
    assert result.successfully_loaded_record_count == 1
    assert result.rejected_record_count == 1
    assert len(result.loaded_records) == 1
    assert len(result.record_loading_issues) == 1
    assert (
        result.record_loading_issues[0].issue_type
        == "UNSUPPORTED_RECORD_REPRESENTATION"
    )
    assert result.record_loading_issues[0].candidate_index == 1


def test_loader_preserves_deterministic_directory_order(
    tmp_path: Path,
) -> None:
    loader = KnowledgeRecordLoader()
    source_directory = tmp_path / "ordered-records"
    source_directory.mkdir()

    write_json(
        source_directory / "z-record.json",
        valid_record_data(integration_record_id="KIR-Z"),
    )
    write_json(
        source_directory / "a-record.json",
        valid_record_data(integration_record_id="KIR-A"),
    )

    result = loader.load(source_directory)

    assert result.load_status == "LOAD_SUCCESSFUL"
    assert [
        record.integration_record_id
        for record in result.loaded_records
    ] == ["KIR-A", "KIR-Z"]


def test_loader_reports_directory_without_supported_files(
    tmp_path: Path,
) -> None:
    loader = KnowledgeRecordLoader()
    source_directory = tmp_path / "empty-records"
    source_directory.mkdir()
    (source_directory / "notes.txt").write_text(
        "not a supported JSON file",
        encoding="utf-8",
    )

    result = loader.load(source_directory)

    assert result.load_status == "LOAD_FAILED"
    assert result.supported_format is True
    assert result.loaded_records == ()
    assert result.total_candidate_record_count == 0
    assert result.successfully_loaded_record_count == 0
    assert result.rejected_record_count == 0
    assert len(result.record_loading_issues) == 1
    assert (
        result.record_loading_issues[0].issue_type
        == "NO_SUPPORTED_FILES"
    )


def test_loader_preserves_read_only_governance_boundaries() -> None:
    loader = KnowledgeRecordLoader()

    assert loader.is_read_only is True
    assert loader.performs_external_lookups is False
    assert loader.follows_external_references is False
    assert loader.infers_missing_values is False
    assert loader.creates_autonomous_decision is False


def test_loader_result_preserves_review_support_boundaries() -> None:
    loader = KnowledgeRecordLoader()

    result = loader.load(valid_record_data())

    assert result.requires_human_review is True
    assert result.is_review_support_only is True
    assert result.mutates_source is False
    assert result.creates_autonomous_decision is False


def test_loader_result_and_issues_are_immutable() -> None:
    loader = KnowledgeRecordLoader()
    result = loader.load(123)
    issue = result.record_loading_issues[0]

    assert isinstance(issue, KnowledgeRecordLoadingIssue)

    with pytest.raises(FrozenInstanceError):
        result.load_status = "LOAD_FAILED"

    with pytest.raises(FrozenInstanceError):
        issue.issue_type = "CHANGED"
