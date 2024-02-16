# this file is test file for division

from calculator.div import division

def test_division():
    division_result = division(4, 2)
    assert division_result == 2

def test_zero_division():
    division_result_by_zero = division(4, 0)
    assert division_result_by_zero == ZeroDivisionError
