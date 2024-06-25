import re

def is_palindrome(s):
    """
    Check if the given string is a palindrome, ignoring spaces, punctuation, and capitalization.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]