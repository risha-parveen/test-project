def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the number n.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    # Example usage
    print(factorial(5))  # Output: 120