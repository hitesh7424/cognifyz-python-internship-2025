'''
Task 04: Calculator Program
Create a Python program that acts as a basic
calculator. It should prompt the user to
enter two numbers and an operator (+, -,*, /, %), 
and then display the result of the operation.

'''


# Import Python's built-in operator module for safe math functions
import operator as op


# Define a calculator function that takes two numbers and an operator
def calc(a, b, o):
    # Dictionary mapping operator symbols to their corresponding functions
    ops = {
        "+": op.add,
        "-": op.sub,
        "*": op.mul,
        "**": op.pow,
        "/": op.truediv,
        "//": op.floordiv,
        "%": op.mod,
    }

    # Check for division/modulo by zero
    if o in {"/", "//", "%"} and b == 0:
        return "Error: Division By Zero"

    # Handle invalid operators
    if o not in ops:
        return "Error: Invalid operator entered."

    # Perform the operation using the function mapped in the dictionary
    return ops[o](a, b)


# Test cases to make sure the function works correctly
assert calc(5, 0, "/") == "Error: Division By Zero"
assert calc(2, 3, "**") == 8
assert calc(7, 2, "//") == 3
assert calc(9, 3, "%") == 0
assert calc(5, 2, "??") == "Error: Invalid operator entered."

# Main program: Get user input and calculate the result
try:
    # Take first number as float
    a = float(input("Enter First Number: "))

    # Take second number as float
    b = float(input("Enter Second Number: "))

    # Take the operator as a string
    o = input("Enter an Operation (+, -, /, *, %, **, //): ")

    # Call the calc function with inputs
    answer = calc(a, b, o)

    # Print the result rounded to 4 decimal places
    print(f"{a} {o} {b} = {round(answer, 4)}")

# Handle invalid numeric input
except ValueError:
    print("Input Error")
