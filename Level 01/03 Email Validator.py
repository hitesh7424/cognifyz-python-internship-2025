"""
Level 1
Task 3

Task: Email Validator
Develop a Python function that validates
whether a given string is a valid email
address. Implement checks for the format,
including the presence of an "@" symbol and
a domain name
"""


def email_validator(email: str) -> bool:
    try:
        # Convert the email to lowercase and split it into local and domain parts using '@'
        local_part, domain = email.lower().split("@")
    except ValueError:
        # If splitting fails (no '@' or more than one '@'), the email is invalid
        return False

    # Split the domain part by '.' to check for valid domain structure
    domain_parts = domain.split(".")
    # If any part of the domain is empty or there are less than two parts, it's invalid
    if "" in domain_parts or len(domain_parts) < 2:
        return False

    # If all checks pass, the email is considered valid
    return True


# input_email = input("Enter the email: ")
input_email = input()

print(email_validator(input_email))
