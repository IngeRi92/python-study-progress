"""Basic calculator."""


def calculator(num1, num2, operator):
    """Perform basic arithmetic operations."""
    if operator == "+":
        return round(num1 + num2)
    elif operator == "-":
        return round(num1 - num2)
    elif operator == "*":
        return round(num1 * num2)
    elif operator == "/":
        if num2 == 0:
            return "Error"
        return round(num1 / num2)
    else:
        return "Invalid operator"
