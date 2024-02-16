# this is test file for addition

from calculator.add import addition

def test_addition_of_two_numbers():
    result = addition(2, 3)
    assert result == 5
