
import ast

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


# Evaluate mathematical expressions safely, including parentheses
def evaluate_expression(expression):
    operations = {
        ast.Add: addition,
        ast.Sub: subtraction,
        ast.Mult: multiplication,
        ast.Div: division,
    }

    def calculate(node):
        if isinstance(node, ast.Expression):
            return calculate(node.body)

        if isinstance(node, ast.Constant):
            if type(node.value) in (int, float):
                return node.value
            raise ValueError("Invalid number.")

        if isinstance(node, ast.BinOp):
            operation = operations.get(type(node.op))

            if operation is None:
                raise ValueError("Unsupported operator.")

            left = calculate(node.left)
            right = calculate(node.right)

            return operation(left, right)

        if isinstance(node, ast.UnaryOp):
            value = calculate(node.operand)

            if isinstance(node.op, ast.USub):
                return -value

            if isinstance(node.op, ast.UAdd):
                return value

        raise ValueError("Invalid expression.")

    try:
        expression = expression.replace("×", "*").replace("÷", "/")
        tree = ast.parse(expression, mode="eval")
        return calculate(tree)

    except (SyntaxError, TypeError, OverflowError, RecursionError):
        raise ValueError("Invalid expression.") from None

def format_result(value):
    rounded = round(value, 1)
    if rounded == 0:
        rounded = 0.0
    return f"{rounded:.1f}".rstrip("0").rstrip(".")    