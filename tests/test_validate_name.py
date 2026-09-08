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
