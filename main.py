def add_numbers(a, b):
    """Add two numbers together.

    This function will be tested.
    """
    return a + b


def multiply_numbers(a, b):
    """Multiply two numbers together.

    This function will be tested.
    """
    if a == 0 or b == 0:
        return 0
    return a * b


def divide_numbers(a, b):
    """Divide two numbers.

    This function will NOT be tested.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def special_sum(x,y):
    result = x + y
    result *= 2
    return result

def dev_function():
    print("This function came from side branch")
    print("this function is dummy and will not be tested")

def is_even(n):
    """Check if a number is even."""
    n = int(n)
    remainder = n % 2
    return remainder == 0


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def special_function(x,y):
    result = x + y + 4
    result *= 2
    if result > 20:
        print("The result is greater than 20")
        result *= 2
        print(result)
    return result
