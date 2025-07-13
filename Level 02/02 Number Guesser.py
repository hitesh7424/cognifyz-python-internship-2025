"""
Task 02: Number Guesser
Create a number guessing game where the
program generates a random number
between a specified range, and the user tries
to guess it. Provide feedback to the user if
their guess is too high or too low.
"""

import random


def generate_number(a: int, b: int) -> int:
    """Generates and returns a random integer between a and b inclusive."""
    return random.randint(a, b)


def get_user_guess() -> int:
    """Prompts the user for an integer guess and handles invalid input."""
    while True:
        try:
            return int(input("Guess the Number: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def give_hint(guess: int, answer: int) -> str:
    """
    Returns a hint based on the user's guess compared to the answer.
    Returns 'correct' if the guess is correct.
    """
    threshold = 15
    if guess == answer:
        return "correct"
    diff = guess - answer
    if abs(diff) > threshold:
        return "Too high" if diff > 0 else "Too low"
    else:
        return "Slightly high" if diff > 0 else "Slightly low"


def guessing_game():
    """
    Runs an interactive number guessing game where the user
    guesses a number between 1 and 100 with hints.
    """

    print("Welcome to the Number Guessing Game!")
    print("Please enter the range of numbers you'd like to guess from.")
    while True:
        try:
            lower = int(input("Enter the LOWER LIMIT: "))
            upper = int(input("Enter the UPPER LIMIT: "))

            if lower >= upper:
                print("⚠️ Upper limit must be greater than lower limit. Try again.")
            else:
                break
        except ValueError:
            print("❌ Please enter valid integers for both limits.")

    random_number = generate_number(lower, upper)
    print(f"A random number has been selected between {lower} and {upper}.")

    attempts = 1
    while True:
        number = get_user_guess()

        hint = give_hint(number, random_number)

        if hint == "correct":
            attempt_word = "attempt" if attempts == 1 else "attempts"
            print(f"You guessed the number correctly in {attempts} {attempt_word}")
            break
        else:
            print(f"[HINT] {hint}")
        attempts += 1


if __name__ == "__main__":
    guessing_game()
