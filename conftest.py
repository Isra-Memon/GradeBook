import pytest
from gradebook import GradeBook, Student, Roster

@pytest.fixture
def empty_roster():
    """Function scope (default): fresh Roster for every test,
    since each test adds students with different score-counts
    and must not leak state into other tests."""
    return Roster()
