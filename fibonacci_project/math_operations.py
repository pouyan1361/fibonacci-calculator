def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n (int): The number to calculate factorial for
    
    Returns:
        int: The factorial of n
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result 