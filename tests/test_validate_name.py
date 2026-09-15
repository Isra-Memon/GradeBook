import pytest
from gradebook import validate_name


def test_validate_name_valid_typical():
    assert validate_name("Ali Khan") is True


def test_validate_name_empty_string():
    with pytest.raises(ValueError):
        validate_name("")


def test_validate_name_over_length():
    with pytest.raises(ValueError):
        validate_name("A" * 51)


def test_validate_name_contains_digits_symbols():
    with pytest.raises(ValueError):
        validate_name("Ali123!")


@pytest.mark.parametrize("length", [0, 1, 49, 50, 51])
def test_validate_name_length_boundaries(length):
    name = "A" * length
    if 1 <= length <= 50:
        assert validate_name(name) is True
    else:
        with pytest.raises(ValueError):
            validate_name(name)
