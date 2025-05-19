def add(number_one, number_two):
    """Add two numbers together."""
    return number_one + number_two
def subtract(number_one, number_two):
    """Subtract the second number from the first."""
    return number_one - number_two
def multiply(number_one, number_two):
    """Multiply two numbers together."""
    return number_one * number_two
def divide(number_one, number_two):
    """Divide the first number by the second."""
    if number_two == 0:
        raise ValueError("Cannot divide by zero.")
    return number_one / number_two