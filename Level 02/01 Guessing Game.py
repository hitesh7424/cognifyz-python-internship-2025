"""
Task 01: Guessing Game
Write a Python program that generates a
random number between 1 and 100. The
user should then try to guess the number.
The program should provide hints such as
"too high" or "too low" until the correct
number is guessed.
"""

import random


def generate_number() -> int:
    """Generates and returns a random integer between 1 and 100 inclusive."""
    return random.randint(1, 100)


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

    print("🎲 Guessing Games Starts!")
    random_number = generate_number()
    print("A random number has been selected between 1 and 100.")
    attempts = 1
    while True:
        number = get_user_guess()

        hint = give_hint(number, random_number)

        if hint == "correct":
            print(f"You guessed the number correctly in {attempts} attempts")
            break
        else:
            print(f"[HINT] {hint}")
        attempts += 1


if __name__ == "__main__":
    guessing_game()
