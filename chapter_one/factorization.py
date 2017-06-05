def gcd(a, b):
    """
    Calculate the greatest common divisor of a and b.
    
    Parameters
    ----------
    a - a contained in Z (integers)
    b - b contained in Z (integers)
    
    Examples:
    >>> gcd(12, 15)
    3
    >>> gcd(27, 15)
    3
    >>> gcd(30, 15)
    15
    """
    while b > 0:
        a, b = b, a % b
    return int(a)

def lcm(a, b):
    """
    Least common multiple of two numbers a, b.
    
    Parameters
    ----------
    a - a contained in Z (integers)
    b - b contained in Z (integers)
    
    >>> lcm(5, 3)
    15
    >>> lcm(17, 2)
    34
    >>> lcm(15, 5)
    15
    """
   
    return int((a * b)/ gcd(a, b))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    

