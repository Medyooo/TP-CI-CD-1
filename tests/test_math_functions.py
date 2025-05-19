# tests/test_math_functions.py

from app.math_functions import addition, division
import pytest

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0

def test_division():
    assert division(10, 2) == 5
    assert division(-6, 3) == -2

def test_division_by_zero():
    with pytest.raises(ValueError):
        division(1, 0)
