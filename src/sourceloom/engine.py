from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .models import (
    Claim,
    ClaimStatus,
    Evidence,
    EvidenceGap,
    EvidenceLink,
    EvidenceStance,
    ResearchContract,
    ResearchTrace,
    StoppingReason,
)


def run_fixture(fixture: Mapping[str, Any]) -> ResearchTrace:
    contract = ResearchContract.from_mapping(fixture.get("contract"))
    evidence = tuple(
        Evidence(
            id=item["id"],
            quote=item["quote"],
            source_title=item["source_title"],
            source_url=item["source_url"],
        )
        for item in fixture["evidence"]
    )
    links = tuple(
        EvidenceLink(
            claim_id=item["claim_id"],
            evidence_id=item["evidence_id"],
            stance=EvidenceStance(item["stance"]),
        )
        for item in fixture["links"]
    )

    supported_claim_ids = {
        link.claim_id for link in links if link.stance is EvidenceStance.SUPPORTS
    }
    claims = tuple(
        Claim(
            id=item["id"],
            statement=item["statement"],
            status=(
                ClaimStatus.SUPPORTED
                if item["id"] in supported_claim_ids
                else ClaimStatus.OPEN
            ),
        )
        for item in fixture["claims"]
    )
    evidence_gaps = tuple(
        EvidenceGap(
            # Derivation from the claim keeps identifiers stable across repeated runs.
            id=f"gap:{item['id']}",
            claim_id=item["id"],
            requirement=item["evidence_requirement"],
        )
        for item in fixture["claims"]
        if item["id"] not in supported_claim_ids
    )

    if len(evidence) >= contract.max_documents:
        stopping_reason = StoppingReason.DOCUMENT_LIMIT_REACHED
    elif evidence_gaps:
        stopping_reason = StoppingReason.FIXTURE_EXHAUSTED
    else:
        stopping_reason = StoppingReason.COVERAGE_REACHED

    return ResearchTrace(
        research_question=fixture["question"],
        contract=contract,
        claims=claims,
        evidence=evidence,
        evidence_links=links,
        evidence_gaps=evidence_gaps,
        stopping_reason=stopping_reason,
    )
