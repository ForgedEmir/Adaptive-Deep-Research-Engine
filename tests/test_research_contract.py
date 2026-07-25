from copy import deepcopy

import pytest

from adaptive_deep_research_engine import run_fixture
from test_deterministic_run import load_fixture


VALID_CONTRACT = {
    "max_waves": 2,
    "max_queries": 5,
    "max_documents": 10,
    "max_cost_eur": 1,
    "max_duration_seconds": 60,
}


@pytest.mark.parametrize("missing_limit", VALID_CONTRACT)
def test_missing_required_limit_is_rejected(missing_limit: str) -> None:
    fixture = deepcopy(load_fixture())
    fixture["contract"] = VALID_CONTRACT | {}
    del fixture["contract"][missing_limit]

    with pytest.raises(ValueError, match=missing_limit):
        run_fixture(fixture)


@pytest.mark.parametrize("invalid_limit", VALID_CONTRACT)
def test_zero_limit_is_rejected(invalid_limit: str) -> None:
    fixture = deepcopy(load_fixture())
    fixture["contract"] = VALID_CONTRACT | {invalid_limit: 0}

    with pytest.raises(ValueError, match=invalid_limit):
        run_fixture(fixture)


def test_valid_contract_is_serialized_in_the_trace() -> None:
    fixture = deepcopy(load_fixture())
    fixture["contract"] = VALID_CONTRACT

    trace = run_fixture(fixture)

    assert trace.to_dict()["contract"] == VALID_CONTRACT


def test_reaching_a_limit_keeps_unresolved_claims_open() -> None:
    fixture = deepcopy(load_fixture())
    fixture["contract"] = VALID_CONTRACT | {"max_documents": 1}

    trace = run_fixture(fixture)

    assert trace.to_dict()["stopping_reason"] == "document_limit_reached"
    assert [claim.status.value for claim in trace.claims] == ["supported", "open"]
