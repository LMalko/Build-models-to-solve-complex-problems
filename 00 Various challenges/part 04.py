# 01. Arguments list from terminal.

from sys import argv

# 02. Override compare methods.

class Apple():
    def __init__(self, size, age):
        self.size = size
        self.age = age

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.size == other.size

a = Apple(40, 2)
b = Apple(40, 50)

print(a == b)

def __ne__(self, other):
    """Override the default Unequal behavior"""
    return self.color != other.color or self.size != other.size


                # object.__lt__(self, other) # For x < y
                # object.__le__(self, other) # For x <= y
                # object.__eq__(self, other) # For x == y
                # object.__ne__(self, other) # For x != y OR x <> y
                # object.__gt__(self, other) # For x > y
                # object.__ge__(self, other) # For x >= y