def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    try:                                 # Used try block to catch Divide by Zero Error.
        division_product = a/b
        return division_product
    except ZeroDivisionError:
        return ZeroDivisionError