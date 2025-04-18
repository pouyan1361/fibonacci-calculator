def get_fibonacci_sequence(n):
    """
    Generate the complete Fibonacci sequence up to the nth number.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-based)
    
    Returns:
        list: List containing the complete Fibonacci sequence up to n
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    sequence = []
    a, b = 0, 1
    
    for i in range(n + 1):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence 