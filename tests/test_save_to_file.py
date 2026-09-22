import pytest
from gradebook import GradeBook, GradeBookIOError, Student


@pytest.fixture
def one_student_gradebook():
    gb = GradeBook()
    s = Student("Ali", 1)
    s.add_score(80)
    gb.add_student(s)
    return gb


def test_save_to_file_writes_content(mocker, one_student_gradebook):
    # Arrange: replace the built-in open() with a fake so no real file is touched
    mock_open = mocker.patch("builtins.open", mocker.mock_open())

    # Act
    one_student_gradebook.save_to_file("fake_path.txt")

    # Assert: open() was called correctly, and write() got the expected content
    mock_open.assert_called_once_with("fake_path.txt", "w")
    handle = mock_open()
    handle.write.assert_called_once_with("Ali,1,80.0")


def test_save_to_file_raises_custom_error_on_os_error(mocker, one_student_gradebook):
    # Arrange: make open() blow up like a real disk failure would
    mocker.patch("builtins.open", side_effect=OSError("disk full"))

    # Act + Assert: our own clean exception should come out, not the raw OSError
    with pytest.raises(GradeBookIOError):
        one_student_gradebook.save_to_file("fake_path.txt")
