import json
from pathlib import Path

import pytest

from adaptive_deep_research_engine import run_fixture


FIXTURE_PATH = Path(__file__).parent / "fixtures" / "separated_sources_research_run.json"


def test_research_trace_preserves_source_boundaries() -> None:
    fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    trace = run_fixture(fixture).to_dict()

    assert trace["snippets"] == [
        {
            "id": "snippet-overclaim",
            "text": "The subscription includes unlimited API usage.",
            "provider": "search-fixture",
            "query": "subscription API usage billing",
            "rank": 1,
            "discovered_url": "https://example.test/official-billing?utm_source=search",
        }
    ]
    assert trace["documents"] == [
        {
            "id": "document-official-billing",
            "title": "Official billing documentation",
            "canonical_url": "https://example.test/official-billing",
            "content": (
                "API usage is billed and managed separately from the subscription. "
                "Current prices are listed elsewhere."
            ),
        }
    ]
    assert trace["evidence"] == [
        {
            "id": "evidence-separate-billing",
            "document_id": "document-official-billing",
            "quote": "API usage is billed and managed separately from the subscription.",
            "start_char": 0,
            "end_char": 65,
        }
    ]
    assert trace["claims"] == [
        {
            "id": "claim-subscription-billing",
            "statement": "The subscription and API usage are billed separately.",
            "status": "supported",
        }
    ]


def test_evidence_must_match_the_exact_document_passage() -> None:
    fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    fixture["evidence"][0]["quote"] = "The subscription includes unlimited API usage."

    with pytest.raises(ValueError, match="exact document passage"):
        run_fixture(fixture)


def test_snippet_cannot_be_linked_directly_to_a_claim() -> None:
    fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    fixture["links"][0]["evidence_id"] = "snippet-overclaim"

    with pytest.raises(ValueError, match="snippet cannot be linked directly"):
        run_fixture(fixture)


def test_claim_link_must_reference_existing_evidence() -> None:
    fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    fixture["links"][0]["evidence_id"] = "unknown-evidence"

    with pytest.raises(ValueError, match="must reference existing evidence"):
        run_fixture(fixture)
