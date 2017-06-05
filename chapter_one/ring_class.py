from factorization import gcd, lcm

class BinaryRing:
    """
    A ring representation of the set {0,1}.
    """
    
    def __init__(self, value):
        self.value = value % 2

    def __repr__(self):
        return "BinaryRing({})".format(self.value)

    def __abs__(self):
        return self.value

    def __bool__(self):
        return bool(self.value)

    def __add__(self, other):
        new_value = (self.value + other.value) % 2
        return BinaryRing(new_value)

    def __mul__(self, other):
        new_value = (self.value * other.value) % 2
        return BinaryRing(new_value)

class NRing:

    def __init__(self, value, n):
        self.n = n
        self.value = value % self.n

    def __repr__(self):
        return "NRing({})".format(self.value)

    def __abs__(self):
        return self.value

    def __bool__(self):
        return bool(self.value)

    def __add__(self, other):
        new_n = lcm(self.n, other.n)
        new_value = (self.value + other.value) % self.n
        return NRing(new_value, new_n)

    def __mul__(self, other):
        new_n = lcm(self.n, other.n)
        new_value = (self.value * other.value) % self.n
        return NRing(new_value, new_n)

    
