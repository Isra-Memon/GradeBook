import pytest
from gradebook import letter_grade


@pytest.mark.parametrize('score,expected', [
    (0, 'F'), (1, 'F'), (59, 'F'),
    (60, 'D'), (61, 'D'), (69, 'D'),
    (70, 'C'), (71, 'C'), (79, 'C'),
    (80, 'B'), (81, 'B'), (89, 'B'),
    (90, 'A'), (91, 'A'), (99, 'A'), (100, 'A'),
])
def test_letter_grade_boundary_valid(score, expected):
    assert letter_grade(score) == expected


@pytest.mark.parametrize('score', [-1, 101])
def test_letter_grade_boundary_invalid(score):
    with pytest.raises(ValueError):
        letter_grade(score)
