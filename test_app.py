import pytest

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(0, 3) == -3
    assert subtract_numbers(3, 3) == 0

