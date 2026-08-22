"""Read-only Knowledge Layer record loader.

This module defines the controlled input boundary for loading authorized
Knowledge Layer integration records from explicitly supplied local inputs.

The loader may accept supported local JSON sources, controlled directories,
in-memory mappings, or existing KnowledgeIntegrationRecord objects. It must
not infer missing values, generate record identifiers, alter source content,
perform external lookups, follow untrusted references, or produce autonomous
review, legal, fraud, compliance, approval, rejection, or enforcement
decisions.

Loaded mappings are converted into immutable KnowledgeIntegrationRecord
objects through the existing KnowledgeIntegrationRecordBuilder so that record
construction rules remain centralized and are not duplicated by this module.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, ClassVar, Mapping

from leo.runtime.knowledge_layer.knowledge_integration_record import (
    KnowledgeIntegrationRecord,
)
from leo.runtime.knowledge_layer.knowledge_integration_record_builder import (
    KnowledgeIntegrationRecordBuilder,
)


_SUPPORTED_FILE_EXTENSIONS = frozenset({".json"})

_ALLOWED_LOAD_STATUSES = frozenset(
    {
        "LOAD_SUCCESSFUL",
        "LOAD_PARTIALLY_SUCCESSFUL",
        "LOAD_FAILED",
        "INPUT_NOT_FOUND",
        "INPUT_INACCESSIBLE",
        "UNSUPPORTED_INPUT",
        "MALFORMED_SERIALIZATION",
    }
)


@dataclass(frozen=True)
class KnowledgeRecordLoadingIssue:
    """Immutable issue produced while loading one candidate record or source."""

    issue_type: str
    message: str
    source_descriptor: str
    source_path: str | None = None
    candidate_index: int | None = None
    record_identifier: str | None = None

    def __post_init__(self) -> None:
        """Validate the issue without modifying supplied values."""

        required_text_fields = {
            "issue_type": self.issue_type,
            "message": self.message,
            "source_descriptor": self.source_descriptor,
        }

        for field_name, value in required_text_fields.items():
            if not isinstance(value, str):
                raise TypeError(f"{field_name} must be a string")
            if value == "":
                raise ValueError(f"{field_name} must not be empty")

        optional_text_fields = {
            "source_path": self.source_path,
            "record_identifier": self.record_identifier,
        }

        for field_name, value in optional_text_fields.items():
            if value is not None and not isinstance(value, str):
                raise TypeError(f"{field_name} must be a string or None")

        if self.candidate_index is not None:
            if not isinstance(self.candidate_index, int):
                raise TypeError("candidate_index must be an integer or None")
            if self.candidate_index < 0:
                raise ValueError("candidate_index must not be negative")

    def to_dict(self) -> dict[str, Any]:
        """Return a detached machine-readable representation."""

        return {
            "issue_type": self.issue_type,
            "message": self.message,
            "source_descriptor": self.source_descriptor,
            "source_path": self.source_path,
            "candidate_index": self.candidate_index,
            "record_identifier": self.record_identifier,
        }


@dataclass(frozen=True)
class KnowledgeRecordLoaderResult:
    """Immutable structured result of one controlled loading operation."""

    load_status: str
    loaded_records: tuple[KnowledgeIntegrationRecord, ...]
    source_descriptor: str
    source_path: str | None
    supported_format: bool
    serialization_issues: tuple[KnowledgeRecordLoadingIssue, ...] = field(
        default_factory=tuple
    )
    record_loading_issues: tuple[KnowledgeRecordLoadingIssue, ...] = field(
        default_factory=tuple
    )
    total_candidate_record_count: int = 0
    successfully_loaded_record_count: int = 0
    rejected_record_count: int = 0

    ALLOWED_LOAD_STATUSES: ClassVar[frozenset[str]] = _ALLOWED_LOAD_STATUSES

    def __post_init__(self) -> None:
        """Validate result consistency without altering loader evidence."""

        if self.load_status not in self.ALLOWED_LOAD_STATUSES:
            raise ValueError(
                "load_status must be one of the approved "
                "KnowledgeRecordLoader result statuses"
            )

        if not isinstance(self.loaded_records, tuple):
            raise TypeError("loaded_records must be a tuple")

        for record in self.loaded_records:
            if not isinstance(record, KnowledgeIntegrationRecord):
                raise TypeError(
                    "loaded_records must contain KnowledgeIntegrationRecord "
                    "objects only"
                )

        if not isinstance(self.source_descriptor, str):
            raise TypeError("source_descriptor must be a string")
        if self.source_descriptor == "":
            raise ValueError("source_descriptor must not be empty")

        if self.source_path is not None and not isinstance(self.source_path, str):
            raise TypeError("source_path must be a string or None")

        if not isinstance(self.supported_format, bool):
            raise TypeError("supported_format must be a boolean")

        if not isinstance(self.serialization_issues, tuple):
            raise TypeError("serialization_issues must be a tuple")

        if not isinstance(self.record_loading_issues, tuple):
            raise TypeError("record_loading_issues must be a tuple")

        for issue in self.serialization_issues:
            if not isinstance(issue, KnowledgeRecordLoadingIssue):
                raise TypeError(
                    "serialization_issues must contain "
                    "KnowledgeRecordLoadingIssue objects only"
                )

        for issue in self.record_loading_issues:
            if not isinstance(issue, KnowledgeRecordLoadingIssue):
                raise TypeError(
                    "record_loading_issues must contain "
                    "KnowledgeRecordLoadingIssue objects only"
                )

        count_fields = {
            "total_candidate_record_count": self.total_candidate_record_count,
            "successfully_loaded_record_count": (
                self.successfully_loaded_record_count
            ),
            "rejected_record_count": self.rejected_record_count,
        }

        for field_name, value in count_fields.items():
            if not isinstance(value, int):
                raise TypeError(f"{field_name} must be an integer")
            if value < 0:
                raise ValueError(f"{field_name} must not be negative")

        if self.successfully_loaded_record_count != len(self.loaded_records):
            raise ValueError(
                "successfully_loaded_record_count must equal the number of "
                "loaded_records"
            )

        if (
            self.successfully_loaded_record_count + self.rejected_record_count
            != self.total_candidate_record_count
        ):
            raise ValueError(
                "successful and rejected record counts must equal the total "
                "candidate record count"
            )

        if (
            self.load_status == "LOAD_SUCCESSFUL"
            and self.rejected_record_count != 0
        ):
            raise ValueError(
                "LOAD_SUCCESSFUL must not contain rejected candidate records"
            )

        if (
            self.load_status == "LOAD_PARTIALLY_SUCCESSFUL"
            and (
                self.successfully_loaded_record_count == 0
                or self.rejected_record_count == 0
            )
        ):
            raise ValueError(
                "LOAD_PARTIALLY_SUCCESSFUL requires both loaded and rejected "
                "candidate records"
            )

    def to_dict(self) -> dict[str, Any]:
        """Return a detached result structure for review and testing."""

        return {
            "load_status": self.load_status,
            "loaded_records": [
                record.to_dict()
                for record in self.loaded_records
            ],
            "source_descriptor": self.source_descriptor,
            "source_path": self.source_path,
            "supported_format": self.supported_format,
            "serialization_issues": [
                issue.to_dict()
                for issue in self.serialization_issues
            ],
            "record_loading_issues": [
                issue.to_dict()
                for issue in self.record_loading_issues
            ],
            "total_candidate_record_count": self.total_candidate_record_count,
            "successfully_loaded_record_count": (
                self.successfully_loaded_record_count
            ),
            "rejected_record_count": self.rejected_record_count,
        }

    @property
    def requires_human_review(self) -> bool:
        """Return True because loader results remain subject to human review."""

        return True

    @property
    def is_review_support_only(self) -> bool:
        """Return True because this result supports human review only."""

        return True

    @property
    def mutates_source(self) -> bool:
        """Return False because loading must never alter the input source."""

        return False

    @property
    def creates_autonomous_decision(self) -> bool:
        """Return False because loading does not make institutional decisions."""

        return False


class KnowledgeRecordLoader:
    """Controlled read-only loader for authorized Knowledge Layer records.

    The loader dispatches explicitly supplied inputs according to their
    concrete type. It does not search for records, resolve external
    references, infer missing values, repair malformed content, or modify
    input sources.

    Filesystem-specific JSON parsing and controlled directory traversal are
    implemented by dedicated private methods so that source handling remains
    isolated from record construction.
    """

    SUPPORTED_FILE_EXTENSIONS: ClassVar[frozenset[str]] = (
        _SUPPORTED_FILE_EXTENSIONS
    )

    def load(
        self,
        source: (
            str
            | Path
            | Mapping[str, Any]
            | KnowledgeIntegrationRecord
        ),
    ) -> KnowledgeRecordLoaderResult:
        """Load one explicitly supplied and supported source.

        Supported input categories are:

        * an existing KnowledgeIntegrationRecord;
        * an in-memory mapping representing one record;
        * a local JSON file path;
        * a controlled local directory path.

        Unsupported values are rejected through a structured loader result.
        """

        if isinstance(source, KnowledgeIntegrationRecord):
            return self._load_existing_record(source)

        if isinstance(source, Mapping):
            return self._load_mapping(source)

        if isinstance(source, (str, Path)):
            return self._load_path(Path(source))

        return self._unsupported_input_result(source)

    def _load_existing_record(
        self,
        record: KnowledgeIntegrationRecord,
    ) -> KnowledgeRecordLoaderResult:
        """Return an existing validated record without reconstructing it."""

        return KnowledgeRecordLoaderResult(
            load_status="LOAD_SUCCESSFUL",
            loaded_records=(record,),
            source_descriptor="knowledge_integration_record",
            source_path=None,
            supported_format=True,
            total_candidate_record_count=1,
            successfully_loaded_record_count=1,
            rejected_record_count=0,
        )

    def _load_mapping(
        self,
        source: Mapping[str, Any],
    ) -> KnowledgeRecordLoaderResult:
        """Build one record from an explicitly supplied in-memory mapping."""

        source_descriptor = "in_memory_mapping"
        detached_mapping = dict(source)
        record_identifier = self._extract_record_identifier(detached_mapping)

        try:
            builder = KnowledgeIntegrationRecordBuilder()
            record = builder.set_fields(**detached_mapping).build()
        except (TypeError, ValueError) as exc:
            issue = KnowledgeRecordLoadingIssue(
                issue_type="RECORD_CONSTRUCTION_FAILED",
                message=str(exc),
                source_descriptor=source_descriptor,
                source_path=None,
                candidate_index=0,
                record_identifier=record_identifier,
            )

            return KnowledgeRecordLoaderResult(
                load_status="LOAD_FAILED",
                loaded_records=(),
                source_descriptor=source_descriptor,
                source_path=None,
                supported_format=True,
                record_loading_issues=(issue,),
                total_candidate_record_count=1,
                successfully_loaded_record_count=0,
                rejected_record_count=1,
            )

        return KnowledgeRecordLoaderResult(
            load_status="LOAD_SUCCESSFUL",
            loaded_records=(record,),
            source_descriptor=source_descriptor,
            source_path=None,
            supported_format=True,
            total_candidate_record_count=1,
            successfully_loaded_record_count=1,
            rejected_record_count=0,
        )

    def _load_path(
        self,
        source_path: Path,
    ) -> KnowledgeRecordLoaderResult:
        """Dispatch a local filesystem path without modifying its source."""

        preserved_source_path = str(source_path)

        try:
            source_exists = source_path.exists()
        except OSError as exc:
            return self._input_inaccessible_result(
                source_path=preserved_source_path,
                message=str(exc),
            )

        if not source_exists:
            return self._input_not_found_result(preserved_source_path)

        try:
            is_file = source_path.is_file()
            is_directory = source_path.is_dir()
        except OSError as exc:
            return self._input_inaccessible_result(
                source_path=preserved_source_path,
                message=str(exc),
            )

        if is_file:
            if source_path.suffix.lower() not in self.SUPPORTED_FILE_EXTENSIONS:
                return self._unsupported_file_format_result(
                    preserved_source_path
                )

            return self._load_json_file(source_path)

        if is_directory:
            return self._load_directory(source_path)

        return self._unsupported_filesystem_input_result(
            preserved_source_path
        )

    def _unsupported_input_result(
        self,
        source: object,
    ) -> KnowledgeRecordLoaderResult:
        """Return a structured result for an unsupported input type."""

        source_type = type(source).__name__
        issue = KnowledgeRecordLoadingIssue(
            issue_type="UNSUPPORTED_INPUT_TYPE",
            message=f"Unsupported input type: {source_type}",
            source_descriptor="unsupported_input",
        )

        return KnowledgeRecordLoaderResult(
            load_status="UNSUPPORTED_INPUT",
            loaded_records=(),
            source_descriptor="unsupported_input",
            source_path=None,
            supported_format=False,
            record_loading_issues=(issue,),
            total_candidate_record_count=0,
            successfully_loaded_record_count=0,
            rejected_record_count=0,
        )

    def _input_not_found_result(
        self,
        source_path: str,
    ) -> KnowledgeRecordLoaderResult:
        """Return a structured result when a supplied path does not exist."""

        issue = KnowledgeRecordLoadingIssue(
            issue_type="INPUT_NOT_FOUND",
            message="The supplied local input path does not exist",
            source_descriptor="filesystem_path",
            source_path=source_path,
        )

        return KnowledgeRecordLoaderResult(
            load_status="INPUT_NOT_FOUND",
            loaded_records=(),
            source_descriptor="filesystem_path",
            source_path=source_path,
            supported_format=False,
            record_loading_issues=(issue,),
            total_candidate_record_count=0,
            successfully_loaded_record_count=0,
            rejected_record_count=0,
        )

    def _input_inaccessible_result(
        self,
        source_path: str,
        message: str,
    ) -> KnowledgeRecordLoaderResult:
        """Return a structured result for an inaccessible local input."""

        issue = KnowledgeRecordLoadingIssue(
            issue_type="INPUT_INACCESSIBLE",
            message=message,
            source_descriptor="filesystem_path",
            source_path=source_path,
        )

        return KnowledgeRecordLoaderResult(
            load_status="INPUT_INACCESSIBLE",
            loaded_records=(),
            source_descriptor="filesystem_path",
            source_path=source_path,
            supported_format=False,
            record_loading_issues=(issue,),
            total_candidate_record_count=0,
            successfully_loaded_record_count=0,
            rejected_record_count=0,
        )

    def _unsupported_file_format_result(
        self,
        source_path: str,
    ) -> KnowledgeRecordLoaderResult:
        """Return a structured result for an unsupported file extension."""

        issue = KnowledgeRecordLoadingIssue(
            issue_type="UNSUPPORTED_FILE_FORMAT",
            message="Only local JSON files are supported",
            source_descriptor="local_file",
            source_path=source_path,
        )

        return KnowledgeRecordLoaderResult(
            load_status="UNSUPPORTED_INPUT",
            loaded_records=(),
            source_descriptor="local_file",
            source_path=source_path,
            supported_format=False,
            record_loading_issues=(issue,),
            total_candidate_record_count=0,
            successfully_loaded_record_count=0,
            rejected_record_count=0,
        )

    def _unsupported_filesystem_input_result(
        self,
        source_path: str,
    ) -> KnowledgeRecordLoaderResult:
        """Reject filesystem objects that are neither files nor directories."""

        issue = KnowledgeRecordLoadingIssue(
            issue_type="UNSUPPORTED_FILESYSTEM_INPUT",
            message=(
                "The supplied filesystem input is neither a supported file "
                "nor a controlled directory"
            ),
            source_descriptor="filesystem_path",
            source_path=source_path,
        )

        return KnowledgeRecordLoaderResult(
            load_status="UNSUPPORTED_INPUT",
            loaded_records=(),
            source_descriptor="filesystem_path",
            source_path=source_path,
            supported_format=False,
            record_loading_issues=(issue,),
            total_candidate_record_count=0,
            successfully_loaded_record_count=0,
            rejected_record_count=0,
        )

    def _load_json_file(
        self,
        source_path: Path,
    ) -> KnowledgeRecordLoaderResult:
        """Load records from one explicitly supplied local JSON file.

        The method reads the file exactly once, performs no repair or
        inference, and accepts only a JSON object or a JSON array of objects.
        Every record is delegated to the existing mapping-loading boundary.
        """

        preserved_source_path = str(source_path)
        source_descriptor = "local_json_file"

        try:
            with source_path.open(
                mode="r",
                encoding="utf-8",
            ) as source_file:
                serialized_content = json.load(source_file)
        except json.JSONDecodeError as exc:
            issue = KnowledgeRecordLoadingIssue(
                issue_type="MALFORMED_SERIALIZATION",
                message=(
                    f"Invalid JSON serialization at line {exc.lineno}, "
                    f"column {exc.colno}: {exc.msg}"
                ),
                source_descriptor=source_descriptor,
                source_path=preserved_source_path,
            )

            return KnowledgeRecordLoaderResult(
                load_status="MALFORMED_SERIALIZATION",
                loaded_records=(),
                source_descriptor=source_descriptor,
                source_path=preserved_source_path,
                supported_format=True,
                record_loading_issues=(issue,),
                total_candidate_record_count=0,
                successfully_loaded_record_count=0,
                rejected_record_count=0,
            )
        except UnicodeDecodeError as exc:
            issue = KnowledgeRecordLoadingIssue(
                issue_type="MALFORMED_SERIALIZATION",
                message=(
                    "The supplied JSON file is not valid UTF-8: "
                    f"{exc}"
                ),
                source_descriptor=source_descriptor,
                source_path=preserved_source_path,
            )

            return KnowledgeRecordLoaderResult(
                load_status="MALFORMED_SERIALIZATION",
                loaded_records=(),
                source_descriptor=source_descriptor,
                source_path=preserved_source_path,
                supported_format=True,
                record_loading_issues=(issue,),
                total_candidate_record_count=0,
                successfully_loaded_record_count=0,
                rejected_record_count=0,
            )
        except OSError as exc:
            return self._input_inaccessible_result(
                source_path=preserved_source_path,
                message=str(exc),
            )

        if isinstance(serialized_content, Mapping):
            candidate_mappings = (serialized_content,)
        elif isinstance(serialized_content, list):
            candidate_mappings = tuple(serialized_content)
        else:
            issue = KnowledgeRecordLoadingIssue(
                issue_type="UNSUPPORTED_SERIALIZED_ROOT",
                message=(
                    "The JSON root must be an object or an array of objects"
                ),
                source_descriptor=source_descriptor,
                source_path=preserved_source_path,
            )

            return KnowledgeRecordLoaderResult(
                load_status="LOAD_FAILED",
                loaded_records=(),
                source_descriptor=source_descriptor,
                source_path=preserved_source_path,
                supported_format=True,
                record_loading_issues=(issue,),
                total_candidate_record_count=1,
                successfully_loaded_record_count=0,
                rejected_record_count=1,
            )

        return self._load_json_candidates(
            candidate_mappings=candidate_mappings,
            source_descriptor=source_descriptor,
            source_path=preserved_source_path,
        )

    def _load_json_candidates(
        self,
        candidate_mappings: tuple[Any, ...],
        source_descriptor: str,
        source_path: str,
    ) -> KnowledgeRecordLoaderResult:
        """Load an ordered sequence of candidates from one JSON source.

        Every mapping candidate is delegated to the existing record builder
        through ``_load_mapping``. Builder issues are preserved rather than
        replaced with inferred loader-level conclusions.

        Rejected record counts represent rejected candidate records, not the
        number of issues reported for those candidates.
        """

        loaded_records: list[KnowledgeIntegrationRecord] = []
        loading_issues: list[KnowledgeRecordLoadingIssue] = []
        rejected_candidate_count = 0

        for candidate_index, candidate in enumerate(candidate_mappings):
            if not isinstance(candidate, Mapping):
                loading_issues.append(
                    KnowledgeRecordLoadingIssue(
                        issue_type="UNSUPPORTED_RECORD_REPRESENTATION",
                        message=(
                            "Each JSON record candidate must be an object"
                        ),
                        source_descriptor=source_descriptor,
                        source_path=source_path,
                        candidate_index=candidate_index,
                    )
                )
                rejected_candidate_count += 1
                continue

            detached_candidate = dict(candidate)
            record_identifier = self._extract_record_identifier(
                detached_candidate
            )

            mapping_result = self._load_mapping(detached_candidate)

            if (
                mapping_result.successfully_loaded_record_count == 1
                and len(mapping_result.loaded_records) == 1
            ):
                loaded_records.extend(mapping_result.loaded_records)
                continue

            rejected_candidate_count += 1

            if mapping_result.record_loading_issues:
                for mapping_issue in mapping_result.record_loading_issues:
                    loading_issues.append(
                        self._rebase_loading_issue(
                            issue=mapping_issue,
                            source_descriptor=source_descriptor,
                            source_path=source_path,
                            candidate_index=candidate_index,
                            record_identifier=record_identifier,
                        )
                    )
                continue

            loading_issues.append(
                KnowledgeRecordLoadingIssue(
                    issue_type="RECORD_CONSTRUCTION_FAILED",
                    message=(
                        "The record builder did not construct the candidate "
                        "and returned no structured loading issue"
                    ),
                    source_descriptor=source_descriptor,
                    source_path=source_path,
                    candidate_index=candidate_index,
                    record_identifier=record_identifier,
                )
            )

        total_candidate_count = len(candidate_mappings)
        successful_count = len(loaded_records)

        if total_candidate_count == 0:
            load_status = "LOAD_SUCCESSFUL"
        elif successful_count == total_candidate_count:
            load_status = "LOAD_SUCCESSFUL"
        elif successful_count > 0:
            load_status = "LOAD_PARTIALLY_SUCCESSFUL"
        else:
            load_status = "LOAD_FAILED"

        return KnowledgeRecordLoaderResult(
            load_status=load_status,
            loaded_records=tuple(loaded_records),
            source_descriptor=source_descriptor,
            source_path=source_path,
            supported_format=True,
            record_loading_issues=tuple(loading_issues),
            total_candidate_record_count=total_candidate_count,
            successfully_loaded_record_count=successful_count,
            rejected_record_count=rejected_candidate_count,
        )

    @staticmethod
    def _rebase_loading_issue(
        issue: KnowledgeRecordLoadingIssue,
        source_descriptor: str,
        source_path: str,
        candidate_index: int,
        record_identifier: str | None,
    ) -> KnowledgeRecordLoadingIssue:
        """Attach JSON-source context while preserving a builder issue.

        The method does not reinterpret, suppress, merge, or prioritize the
        builder's issue. It only adds the deterministic source coordinates
        needed by the loader-level audit result.
        """

        preserved_identifier = (
            issue.record_identifier
            if issue.record_identifier is not None
            else record_identifier
        )

        return KnowledgeRecordLoadingIssue(
            issue_type=issue.issue_type,
            message=issue.message,
            source_descriptor=source_descriptor,
            source_path=source_path,
            candidate_index=candidate_index,
            record_identifier=preserved_identifier,
        )

    def _load_directory(
        self,
        source_path: Path,
    ) -> KnowledgeRecordLoaderResult:
        """Load directly contained JSON files in deterministic name order.

        Directory traversal is intentionally non-recursive. The loader does
        not follow symbolic links, inspect parent directories, or search for
        related records outside the explicitly supplied directory.
        """

        preserved_source_path = str(source_path)
        source_descriptor = "local_json_directory"

        try:
            directory_entries = tuple(
                sorted(
                    source_path.iterdir(),
                    key=lambda entry: entry.name,
                )
            )
        except OSError as exc:
            return self._input_inaccessible_result(
                source_path=preserved_source_path,
                message=str(exc),
            )

        json_files: list[Path] = []
        directory_issues: list[KnowledgeRecordLoadingIssue] = []

        for entry in directory_entries:
            try:
                if entry.is_symlink():
                    directory_issues.append(
                        KnowledgeRecordLoadingIssue(
                            issue_type="SYMBOLIC_LINK_SKIPPED",
                            message=(
                                "Symbolic links are not followed by the "
                                "controlled directory loader"
                            ),
                            source_descriptor=source_descriptor,
                            source_path=str(entry),
                        )
                    )
                    continue

                if (
                    entry.is_file()
                    and entry.suffix.lower()
                    in self.SUPPORTED_FILE_EXTENSIONS
                ):
                    json_files.append(entry)
            except OSError as exc:
                directory_issues.append(
                    KnowledgeRecordLoadingIssue(
                        issue_type="DIRECTORY_ENTRY_INACCESSIBLE",
                        message=str(exc),
                        source_descriptor=source_descriptor,
                        source_path=str(entry),
                    )
                )

        if not json_files:
            directory_issues.append(
                KnowledgeRecordLoadingIssue(
                    issue_type="NO_SUPPORTED_FILES",
                    message=(
                        "The supplied directory contains no directly "
                        "accessible supported JSON files"
                    ),
                    source_descriptor=source_descriptor,
                    source_path=preserved_source_path,
                )
            )

            return KnowledgeRecordLoaderResult(
                load_status="LOAD_FAILED",
                loaded_records=(),
                source_descriptor=source_descriptor,
                source_path=preserved_source_path,
                supported_format=True,
                record_loading_issues=tuple(directory_issues),
                total_candidate_record_count=0,
                successfully_loaded_record_count=0,
                rejected_record_count=0,
            )

        loaded_records: list[KnowledgeIntegrationRecord] = []
        loading_issues: list[KnowledgeRecordLoadingIssue] = list(
            directory_issues
        )
        total_candidate_count = 0
        rejected_count = 0

        for json_file in json_files:
            file_result = self._load_json_file(json_file)

            loaded_records.extend(file_result.loaded_records)
            total_candidate_count += (
                file_result.total_candidate_record_count
            )
            rejected_count += file_result.rejected_record_count
            loading_issues.extend(file_result.record_loading_issues)

        successful_count = len(loaded_records)

        if successful_count > 0 and not loading_issues:
            load_status = "LOAD_SUCCESSFUL"
        elif successful_count > 0:
            load_status = "LOAD_PARTIALLY_SUCCESSFUL"
        else:
            load_status = "LOAD_FAILED"

        return KnowledgeRecordLoaderResult(
            load_status=load_status,
            loaded_records=tuple(loaded_records),
            source_descriptor=source_descriptor,
            source_path=preserved_source_path,
            supported_format=True,
            record_loading_issues=tuple(loading_issues),
            total_candidate_record_count=total_candidate_count,
            successfully_loaded_record_count=successful_count,
            rejected_record_count=rejected_count,
        )

    @staticmethod
    def _extract_record_identifier(
        source: Mapping[str, Any],
    ) -> str | None:
        """Preserve an explicitly supplied record identifier when available."""

        candidate_identifier = source.get("integration_record_id")

        if isinstance(candidate_identifier, str):
            return candidate_identifier

        return None

    @property
    def is_read_only(self) -> bool:
        """Return True because the loader must never modify its sources."""

        return True

    @property
    def performs_external_lookups(self) -> bool:
        """Return False because external lookup is prohibited."""

        return False

    @property
    def follows_external_references(self) -> bool:
        """Return False because untrusted references must not be followed."""

        return False

    @property
    def infers_missing_values(self) -> bool:
        """Return False because missing record values must not be inferred."""

        return False

    @property
    def creates_autonomous_decision(self) -> bool:
        """Return False because loading cannot create institutional decisions."""

        return False