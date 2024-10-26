import pytest


def addition(a, b):
    return a + b


def division(a, b):
    return a / b


def hello(name: str):
    return f"Hello {name}"


def test_addition():
    assert addition(1, 2) == 3


def test_division():
    assert division(10, 2) == 5, "Should be 5"


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)


def test_hello():
    assert hello("John") == "Hello John"


def test_hello_with_empty_string():
    assert "Hello " in hello("")


def test_for_broken():
    # assert addition(1) == 2
    with pytest.raises(TypeError) as e:
        addition(1)
    assert str(e.value) == "addition() missing 1 required positional argument: 'b'"
