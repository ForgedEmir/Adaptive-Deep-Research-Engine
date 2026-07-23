from __future__ import annotations

import json
from dataclasses import dataclass
from enum import StrEnum


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
    claims: tuple[Claim, ...]
    evidence: tuple[Evidence, ...]
    evidence_links: tuple[EvidenceLink, ...]
    evidence_gaps: tuple[EvidenceGap, ...]
    stopping_reason: StoppingReason

    def to_dict(self) -> dict[str, object]:
        return {
            "research_question": self.research_question,
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
