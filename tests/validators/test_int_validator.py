import pytest
from random import randint

from json_schema_checker.validators import IntValidator

@pytest.fixture()
def int_validator():
    return IntValidator()

@pytest.mark.parametrize('value', argvalues=list(randint(-10000, 10000) for i in range(10)))
def test_with_good_value(int_validator, value):
    assert int_validator.is_valid(value)


def test_with_string(int_validator):
    assert not int_validator.is_valid("TOTO")


def test_with_float(int_validator):
    assert not int_validator.is_valid(1.2)