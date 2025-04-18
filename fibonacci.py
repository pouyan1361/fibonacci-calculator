def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.
    This is more efficient for larger numbers as it avoids recursive call overhead.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-based)
    
    Returns:
        int: The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 1:
        return n
        
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using a recursive approach.
    Note: This is less efficient for large numbers due to recursive calls.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-based)
    
    Returns:
        int: The nth Fibonacci number
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoized(n, memo=None):
    """
    Calculate the nth Fibonacci number using a memoized recursive approach.
    This combines the simplicity of recursion with better performance.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-based)
        memo (dict): Memoization dictionary to store previously calculated values
    
    Returns:
        int: The nth Fibonacci number
    """
    if memo is None:
        memo = {}
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 1:
        return n
    
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]

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

# Example usage
if __name__ == "__main__":
    while True:
        try:
            n = int(input("\nEnter a number to calculate its Fibonacci sequence (or enter a negative number to exit): "))
            if n < 0:
                print("Exiting program...")
                break
                
            sequence = get_fibonacci_sequence(n)
            
            print(f"\nFibonacci sequence up to position {n}:")
            print("-" * 40)
            
            # Print sequence with position numbers
            for i, num in enumerate(sequence):
                print(f"F({i}) = {num}")
            
            # Print as a continuous sequence
            print("\nComplete sequence:")
            print(sequence)
            
        except ValueError:
            print("Please enter a valid integer!") 