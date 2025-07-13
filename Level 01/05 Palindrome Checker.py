"""
Task 05: Palindrome Checker
Write a Python function that checks whether
a given string is a palindrome. A palindrome
is a word, phrase, or sequence that reads the
same backward as forward (e.g.,
"madam" or
"racecar").

"""


def is_palindrome(word: str) -> bool:
    """
    Check if a string is a palindrome.
    Ignores case and non-alphanumeric characters.

    Args:
        word (str): The input string to check.

    Returns:
        bool: True if the cleaned string is a palindrome, False otherwise.
    """

    word = word.lower()

    # Remove non-alphanumeric characters
    word = [c for c in word if c.isalnum()]

    return word == word[::-1]


def run_tests():
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("12321") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    print("All tests passed.")


def main():
    word = input("Enter a word: ")

    if is_palindrome(word):
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")


if __name__ == "__main__":
    run_tests()
    main()
