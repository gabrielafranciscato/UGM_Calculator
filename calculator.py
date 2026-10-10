# Arithmetic Operator Functions

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, divisor):
    try:
        return num1 / divisor
    except ZeroDivisionError:
        return "Error: Division by zero is undefined."

