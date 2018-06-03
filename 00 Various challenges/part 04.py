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

# 03. For loops

lista = [122, 2, 63, 34, 55, 6, 7, 8]
lista2 = ["albert", "bernard", "fred", "evan"]


for i in enumerate(lista):
    print(i[0], "position holds the value of", i[1])


for i in zip(lista, lista2):
    print(i)


for i in sorted(lista2, reverse=True, key=len):
    print(i)

print(lista2)