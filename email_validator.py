# email_validator.py

import re

def is_valid_email(email):
    """
    Validate if the given string is a properly formatted email address.

    Parameters:
    email (str): The email address to validate.

    Returns:
    bool: True if the email address is valid, False otherwise.
    """
    email_regex = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    return re.match(email_regex, email) is not None

if __name__ == "__main__":
    # Example usage
    print(is_valid_email("example@example.com"))  # Output: True
    print(is_valid_email("invalid-email"))  # Output: False