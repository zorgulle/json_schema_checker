from json_schema_checker.composed import List, IntList
from json_schema_checker.validators import Int
import pytest

@pytest.fixture()
def list_int():
    return List([Int()])

@pytest.fixture()
def int_list():
    return IntList()

from random import randint

@pytest.mark.parametrize('values', argvalues=list(list(randint(-1100, 1100) for _ in range(10)) for _ in range(10)))
def test_list_int(list_int, values):
    assert list_int.is_valid(values) == True

def test_list_int_wrong(list_int, values=["TOTO", "TITI"]):
    assert list_int.is_valid(values) == False

@pytest.mark.parametrize('values', argvalues=list(list(randint(-1100, 1100) for _ in range(10)) for _ in range(10)))
def test_int_list_composed(int_list, values):
    assert int_list.is_valid(values) == True


