from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer n.

    Parameters:
    n (int): The number to calculate the factorial for. Must be a non-negative integer.

    Returns:
    int: The factorial of the number n.
    
    Raises:
    ValueError: If n is a negative integer or not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Example usage
    print(factorial(5))  # Output: 120