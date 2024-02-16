# This python file tests the functions
from calculator.operations import add, multiply, subtract, divide

def test_addition():
    assert add(4,4) == 8

def test_subtraction():
    assert subtract(8,2) == 6

def test_multiplication():
    assert multiply(7,7) == 49

def test_division():
    assert divide(20,4) == 5

def test_zero_division():
    division_result_by_zero = divide(4, 0)
    assert division_result_by_zero == ZeroDivisionError