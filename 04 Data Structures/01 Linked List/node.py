class Node:

    def __init__(self, name, matric, year):
        self.__name = name
        self.matric = matric
        self.year = year
        self.__next = None

    def set_next(self, node):
        if isinstance(node, (Node, type(None))) or node:
            self.__next = node
        else:
            raise TypeError("The 'next' node must be of type Node or None")

    def get_next(self):
        return self.__next

    def display_node(self):
        print(f"{self.matric}: {self.__name} (year {self.year})")

    def get_name(self):
        return self.__name

    def get_year(self):
        return self.year
