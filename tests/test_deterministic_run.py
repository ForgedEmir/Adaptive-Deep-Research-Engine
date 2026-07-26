import json
from pathlib import Path

from adaptive_deep_research_engine import run_fixture


FIXTURE_PATH = Path(__file__).parent / "fixtures" / "minimal_research_run.json"


def load_fixture() -> dict[str, object]:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def test_minimal_fixture_produces_a_traceable_research_run() -> None:
    trace = run_fixture(load_fixture())

    assert trace.to_dict() == {
        "research_question": "Does a software subscription include API usage?",
        "contract": {
            "max_waves": 2,
            "max_queries": 5,
            "max_documents": 1,
            "max_cost_eur": 1.0,
            "max_duration_seconds": 60,
        },
        "claims": [
            {
                "id": "claim-subscription-billing",
                "statement": "The software subscription and API usage are billed separately.",
                "status": "supported",
            },
            {
                "id": "claim-current-api-price",
                "statement": "The current API price is documented by the provider.",
                "status": "open",
            },
        ],
        "snippets": [],
        "documents": [
            {
                "id": "document-official-billing",
                "title": "Official billing documentation",
                "canonical_url": "https://example.test/official-billing",
                "content": (
                    "API usage is billed and managed separately from the subscription."
                ),
            }
        ],
        "evidence": [
            {
                "id": "evidence-separate-billing",
                "document_id": "document-official-billing",
                "quote": "API usage is billed and managed separately from the subscription.",
                "start_char": 0,
                "end_char": 65,
            }
        ],
        "evidence_links": [
            {
                "claim_id": "claim-subscription-billing",
                "evidence_id": "evidence-separate-billing",
                "stance": "supports",
            }
        ],
        "evidence_gaps": [
            {
                "id": "gap:claim-current-api-price",
                "claim_id": "claim-current-api-price",
                "requirement": "A current official pricing page that states the API price.",
            }
        ],
        "stopping_reason": "document_limit_reached",
    }


def test_same_fixture_produces_the_same_json_trace() -> None:
    first_trace = run_fixture(load_fixture()).to_json()
    second_trace = run_fixture(load_fixture()).to_json()

    assert first_trace == second_trace
