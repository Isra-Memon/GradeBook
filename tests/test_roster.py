import pytest
from gradebook import Student, Roster


@pytest.mark.parametrize("num_scores", [0, 3, 8])
def test_roster_add_student_score_count(empty_roster, num_scores):
    student = Student("Test Student", 999)
    for i in range(num_scores):
        student.add_score(70)

    if 1 <= num_scores <= 6:
        empty_roster.add_student(student)
        assert student in empty_roster.students
    else:
        with pytest.raises(ValueError):
            empty_roster.add_student(student)


@pytest.mark.parametrize("num_scores", [0, 1, 2, 5, 6, 7])
def test_roster_score_count_boundaries(empty_roster, num_scores):
    student = Student("Boundary Student", 500)
    for i in range(num_scores):
        student.add_score(70)

    if 1 <= num_scores <= 6:
        empty_roster.add_student(student)
        assert student in empty_roster.students
    else:
        with pytest.raises(ValueError):
            empty_roster.add_student(student)
