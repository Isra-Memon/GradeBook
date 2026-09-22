import pytest
from gradebook import Student


@pytest.mark.parametrize("score,expected_len", [
    pytest.param(0, 1, id="lowest-valid-score"),
    pytest.param(100, 1, id="highest-valid-score"),
    pytest.param(75, 1, id="mid-range-score"),
    pytest.param(-1, 0, id="negative-score-invalid"),
    pytest.param(101, 0, id="above-max-invalid"),
    pytest.param(59.5, 1, id="decimal-score-valid"),
], ids=[
    "lowest-valid-score", "highest-valid-score", "mid-range-score",
    "negative-score-invalid", "above-max-invalid", "decimal-score-valid",
])
def test_add_score_edge_cases(score, expected_len):
    student = Student("Test Student", 1)

    if expected_len == 1:
        student.add_score(score)
        assert len(student.scores) == 1
        assert student.scores[0] == score
    else:
        with pytest.raises(ValueError):
            student.add_score(score)
        assert len(student.scores) == 0
