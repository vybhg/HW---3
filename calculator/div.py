# This is division function

def division(a, b):
    """using try - except block to catch Zero division error."""
    try:
        division_product = a/b
        return division_product
    except ZeroDivisionError:
        return ZeroDivisionError
    