def add(a,b):
    """
    Calculates the sum between two numbers

    Args:
        a: first number added
        b: second number added

    Returns: 
        Sum of a and b
    """
    return a + b

def subtract(a,b):
    """
    Calculates the substraction between two numbers
    
    Args:
        a: initial number 
        b: number to substract from a
    
    Returns: 
        Difference between a and b
    """
    return a - b

def multiply(a,b):
    """
    Calculates the product between two numbers
    
    Args:
        a: initial number
        b: multiplier number
    
    Returns: 
        Product of a and b
    """
    return a * b

def divide(a,b):
    """
    Calculates the division of two numbers
    
    Args:
        a: dividend
        b: divider
    
    Returns: 
        Division of a by b
    """
    if b == 0:
        raise ValueError("division by 0 isn't allowed")
    return a // b
