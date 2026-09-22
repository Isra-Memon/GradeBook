import pytest
from gradebook import GradeBook, Student, Roster

@pytest.fixture
def empty_roster():
    """Function scope (default): fresh Roster for every test,
    since each test adds students with different score-counts
    and must not leak state into other tests."""
    return Roster()

@pytest.fixture(scope="module")
def rounding_gradebook():
    """Module scope: this GradeBook is built once and reused by every
    test in this module, because the setup (2 students with fixed
    scores) is expensive-ish and read-only — no test modifies it,
    so re-creating it per test would just waste time."""
    gb = GradeBook()

    s1 = Student("Student A", 1)
    s1.add_score(79.99)
    gb.add_student(s1)

    s2 = Student("Student B", 2)
    s2.add_score(80.0)
    gb.add_student(s2)

    return gb
