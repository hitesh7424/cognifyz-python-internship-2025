"""
Task 03: Password Strength Checker
Create a Python function that evaluates
the strength of a password entered by the
user. Implement checks for factors such as
length, presence of uppercase and
lowercase letters, digits, and special
characters.
"""


def password_strength_checker(password: str):
    marks = 0
    remarks = []

    if len(password) >= 8:
        marks += 1
    else:
        remarks.append("> Password length must be at least 8 characters long.")

    if any(c.islower() for c in password):
        marks += 1
    else:
        remarks.append("> Include at least one lowercase letter.")

    if any(c.isupper() for c in password):
        marks += 1
    else:
        remarks.append("> Include at least one uppercase letter.")

    if any(c.isnumeric() for c in password):
        marks += 1
    else:
        remarks.append("> Include at least one digit.")

    if any(not c.isalnum() for c in password):
        marks += 1
    else:
        remarks.append("> Include at least one special character.")

    return marks, remarks


password = input()
# password = input("Enter your password: ")

marks, remarks = password_strength_checker(password)

STRONG_SCORE = 5
MODERATE_SCORE = 4


if marks >= STRONG_SCORE:
    print("Your password is Strong")
elif marks == MODERATE_SCORE:
    print("Your password is Moderate")
else:
    print("Your password is Weak")

for remark in remarks:
    print(remark)
