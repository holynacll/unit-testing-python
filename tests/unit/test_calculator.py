import pytest

from src.calculator import add, subtract, multiply, divide


class TestAddition:
    def test_add_positive_numbers(self):
        assert add(2.5, 3) == 5.5

    def test_add_negative_numbers(self):
        assert add(-2.25, -3.0) == -5.25

    def test_add_mixed_numbers(self):
        assert add(2, -3) == -1


def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_mixed_numbers():
    assert subtract(5, -3) == 8
