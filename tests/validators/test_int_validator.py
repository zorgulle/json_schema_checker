import pytest
from random import randint, choices
from string import digits, ascii_letters

from json_schema_checker.validators import Int, StringValidator
from json_schema_checker.validators.validators import SimpleValidator, ValidatorTypeUndefinedException

@pytest.fixture()
def simple_validator_without_type():
    class C(SimpleValidator):
        pass
    return C


@pytest.fixture()
def int_validator():
    return Int()

@pytest.fixture()
def string_validator():
    return StringValidator()


def get_random_string():
    length = randint(0, 1024)
    alphabet = ascii_letters + digits
    word_letters = choices(alphabet, k=length)
    return ''.join(word_letters)

@pytest.mark.parametrize('value', argvalues=list(get_random_string() for i in range(10)))
def test_string_with_good_value(string_validator, value):
    assert string_validator.is_valid(value)


@pytest.mark.parametrize('value', argvalues=list(randint(-10000, 10000) for i in range(10)))
def test_with_good_value(int_validator, value):
    assert int_validator.is_valid(value)


def test_with_string(int_validator):
    assert not int_validator.is_valid("TOTO")


def test_with_float(int_validator):
    assert not int_validator.is_valid(1.2)


def test_simple_validator_without_type(simple_validator_without_type):
    with pytest.raises(ValidatorTypeUndefinedException):
        simple_validator_without_type()