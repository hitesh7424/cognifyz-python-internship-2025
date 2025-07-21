"""
Task 04: Fibonacci Sequence
Write a Python function that generates the
Fibonacci sequence up to a given number of
terms. The function should take an integer
input from the user and display the
Fibonacci sequence up to that number of
terms.
"""


def fibonacci(n: int) -> list:
    """
    Generate the Fibonacci sequence up to a given number of terms.

    Parameters:
        n (int): The number of terms desired in the Fibonacci sequence.

    Returns:
        list: A list containing the Fibonacci sequence up to 'n' terms.
    """
    sequence = [0, 1]

    if n < 0:
        return "[InputError] Input should be positive number"
    elif n <= 2:
        return sequence[:n]

    for i in range(2, n):
        next_number = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_number)

    return sequence


# print(f"-1 > {fibonacci(-1)}")
# print(f" 0 > {fibonacci(0)}")
# print(f" 1 > {fibonacci(1)}")
# print(f" 2 > {fibonacci(2)}")
# print(f" 3 > {fibonacci(3)}")
# print(f" 4 > {fibonacci(4)}")
# print(f" 5 > {fibonacci(5)}")
# print(f" 7 > {fibonacci(7)}")
# print(f"10 > {fibonacci(10)}")

num = int(input("Enter a number: "))

print(f"Fibinacci Series upto {num}")
for i in fibonacci(num):
    print(i, end=" ")

print()
