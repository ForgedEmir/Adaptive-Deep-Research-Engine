from __future__ import annotations

import json
import math
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from typing import Any


class ClaimStatus(StrEnum):
    SUPPORTED = "supported"
    OPEN = "open"


class EvidenceStance(StrEnum):
    SUPPORTS = "supports"


class StoppingReason(StrEnum):
    COVERAGE_REACHED = "coverage_reached"
    DOCUMENT_LIMIT_REACHED = "document_limit_reached"
    FIXTURE_EXHAUSTED = "fixture_exhausted"


@dataclass(frozen=True, slots=True)
class ResearchContract:
    max_waves: int
    max_queries: int
    max_documents: int
    max_cost_eur: float
    max_duration_seconds: int

    @classmethod
    def from_mapping(cls, value: Any) -> ResearchContract:
        if not isinstance(value, Mapping):
            raise ValueError("contract must be an object")

        def positive_integer(name: str) -> int:
            if name not in value:
                raise ValueError(f"missing required limit: {name}")
            limit = value[name]
            if type(limit) is not int or limit <= 0:
                raise ValueError(f"{name} must be a positive integer")
            return limit

        cost_name = "max_cost_eur"
        if cost_name not in value:
            raise ValueError(f"missing required limit: {cost_name}")
        cost = value[cost_name]
        if (
            isinstance(cost, bool)
            or not isinstance(cost, (int, float))
            or not math.isfinite(cost)
            or cost <= 0
        ):
            raise ValueError(f"{cost_name} must be a positive finite number")
        return cls(
            max_waves=positive_integer("max_waves"),
            max_queries=positive_integer("max_queries"),
            max_documents=positive_integer("max_documents"),
            # Normalizing gives one stable JSON representation for 1 and 1.0.
            max_cost_eur=float(cost),
            max_duration_seconds=positive_integer("max_duration_seconds"),
        )

    def to_dict(self) -> dict[str, int | float]:
        return {
            "max_waves": self.max_waves,
            "max_queries": self.max_queries,
            "max_documents": self.max_documents,
            "max_cost_eur": self.max_cost_eur,
            "max_duration_seconds": self.max_duration_seconds,
        }


@dataclass(frozen=True, slots=True)
class Claim:
    id: str
    statement: str
    status: ClaimStatus

    def to_dict(self) -> dict[str, str]:
        return {"id": self.id, "statement": self.statement, "status": self.status.value}


@dataclass(frozen=True, slots=True)
class Evidence:
    id: str
    quote: str
    source_title: str
    source_url: str

    def to_dict(self) -> dict[str, str]:
        return {
            "id": self.id,
            "quote": self.quote,
            "source_title": self.source_title,
            "source_url": self.source_url,
        }


@dataclass(frozen=True, slots=True)
class EvidenceLink:
    claim_id: str
    evidence_id: str
    stance: EvidenceStance

    def to_dict(self) -> dict[str, str]:
        return {
            "claim_id": self.claim_id,
            "evidence_id": self.evidence_id,
            "stance": self.stance.value,
        }


@dataclass(frozen=True, slots=True)
class EvidenceGap:
    id: str
    claim_id: str
    requirement: str

    def to_dict(self) -> dict[str, str]:
        return {"id": self.id, "claim_id": self.claim_id, "requirement": self.requirement}


@dataclass(frozen=True, slots=True)
class ResearchTrace:
    research_question: str
    contract: ResearchContract
    claims: tuple[Claim, ...]
    evidence: tuple[Evidence, ...]
    evidence_links: tuple[EvidenceLink, ...]
    evidence_gaps: tuple[EvidenceGap, ...]
    stopping_reason: StoppingReason

    def to_dict(self) -> dict[str, object]:
        return {
            "research_question": self.research_question,
            "contract": self.contract.to_dict(),
            "claims": [claim.to_dict() for claim in self.claims],
            "evidence": [item.to_dict() for item in self.evidence],
            "evidence_links": [link.to_dict() for link in self.evidence_links],
            "evidence_gaps": [gap.to_dict() for gap in self.evidence_gaps],
            "stopping_reason": self.stopping_reason.value,
        }

    def to_json(self) -> str:
        # Stable key ordering prevents serialization details from breaking replayability.
        return json.dumps(
            self.to_dict(),
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        )
