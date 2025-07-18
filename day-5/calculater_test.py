import pytest

from calculater import add,devide

def test_add():
    assert add(2,3) == 5
    assert add(0,0) == 0
def test_devide():
    assert devide(10,2) == 5
    assert devide(9,3) == 3
def test_devide_by_zero():
    with pytest.raises(ValueError, match="Can not be divided by zero"):devide(5,0)