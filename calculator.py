# Arithmetic Operator Functions

def addition(num1, num2):
    validate_numbers(num1, num2)
    return num1 + num2

def subtraction(num1, num2):
    validate_numbers(num1, num2)
    return num1 - num2

def multiplication(num1, num2):
    validate_numbers(num1, num2)
    return num1 * num2

def division(num1, divisor):
    validate_numbers(num1, divisor)

    if divisor == 0:
        raise ValueError("Cannot divide by zero.")
    
    return num1 / divisor
    
def validate_numbers(num1, num2):
    if (
        type(num1) not in (int, float)
        or type(num2) not in (int, float)
    ):
        raise ValueError("Please enter valid numbers.")

