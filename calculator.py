# Arithmetic Operator Functions

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, divisor):
    if divisor == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / divisor
    

