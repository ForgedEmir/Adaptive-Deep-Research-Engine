from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .models import (
    Claim,
    ClaimStatus,
    Document,
    Evidence,
    EvidenceGap,
    EvidenceLink,
    EvidenceStance,
    ResearchContract,
    ResearchTrace,
    SearchSnippet,
    StoppingReason,
)


def run_fixture(fixture: Mapping[str, Any]) -> ResearchTrace:
    contract = ResearchContract.from_mapping(fixture.get("contract"))
    snippets = tuple(
        SearchSnippet(
            id=item["id"],
            text=item["text"],
            provider=item["provider"],
            query=item["query"],
            rank=item["rank"],
            discovered_url=item["discovered_url"],
        )
        for item in fixture["snippets"]
    )
    documents = tuple(
        Document(
            id=item["id"],
            title=item["title"],
            canonical_url=item["canonical_url"],
            content=item["content"],
        )
        for item in fixture["documents"]
    )
    evidence = tuple(
        Evidence(
            id=item["id"],
            document_id=item["document_id"],
            quote=item["quote"],
            start_char=item["start_char"],
            end_char=item["end_char"],
        )
        for item in fixture["evidence"]
    )
    documents_by_id = {document.id: document for document in documents}
    for item in evidence:
        document = documents_by_id[item.document_id]
        if document.content[item.start_char : item.end_char] != item.quote:
            raise ValueError(
                f"evidence {item.id} must quote the exact document passage"
            )

    links = tuple(
        EvidenceLink(
            claim_id=item["claim_id"],
            evidence_id=item["evidence_id"],
            stance=EvidenceStance(item["stance"]),
        )
        for item in fixture["links"]
    )
    snippet_ids = {snippet.id for snippet in snippets}
    evidence_ids = {item.id for item in evidence}
    for link in links:
        if link.evidence_id in snippet_ids:
            raise ValueError("a snippet cannot be linked directly to a claim")
        if link.evidence_id not in evidence_ids:
            raise ValueError("a claim link must reference existing evidence")

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

    if len(documents) >= contract.max_documents:
        stopping_reason = StoppingReason.DOCUMENT_LIMIT_REACHED
    elif evidence_gaps:
        stopping_reason = StoppingReason.FIXTURE_EXHAUSTED
    else:
        stopping_reason = StoppingReason.COVERAGE_REACHED

    return ResearchTrace(
        research_question=fixture["question"],
        contract=contract,
        claims=claims,
        snippets=snippets,
        documents=documents,
        evidence=evidence,
        evidence_links=links,
        evidence_gaps=evidence_gaps,
        stopping_reason=stopping_reason,
    )
