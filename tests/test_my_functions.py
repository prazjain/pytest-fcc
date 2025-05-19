import pytest

from source.my_functions import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0

def test_substract():
    assert subtract(2, 1) == 1
    assert subtract(1, 1) == 0
    assert subtract(0, 0) == 0
    assert subtract(2.5, 1.5) == 1.0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0
    assert multiply(1.5, 2) == 3.0
    
def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(0, 1) == 0
    assert divide(1.5, 0.5) == 3.0
    with pytest.raises(ValueError):
        divide(1, 0)