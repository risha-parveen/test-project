#implement fibonacci series


def fibonacci(n):
    """
    Generate a list of the first n Fibonacci numbers.

    Parameters:
    n (int): The number of terms in the Fibonacci series to generate.

    Returns:
    list: A list containing the first n terms of the Fibonacci series.
    """
    if n <= 0:
        return []
    
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    
    return series[:n]

if __name__ == "__main__":
    # Example usage
    print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
