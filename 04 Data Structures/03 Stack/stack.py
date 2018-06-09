class Stack:

    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_to_stack_start(self, node):
        if self.__root:
            node.set_next(self.__root)
        self.__root = node

    def remove_start_from_stack(self):
        if not self.__root:
            raise RuntimeError("Tried to remove from the list but it was already empty!")
        temp = self.__root
        self.__root = self.__root.get_next()
        return temp

    def find(self, text):
        marker = self.__root

        while marker:
            if marker.get_text() == text:
                return marker
            marker = marker.get_next()
        raise LookupError(f"Node with text {text} was not found in the linked list!")

    def print_list(self):
        marker = self.__root

        while marker:
            marker.print_details()
            marker = marker.get_next()

    def size(self):
        marker = self.__root
        count = 0
        while marker:
            count += 1
            marker = marker.get_next()
        return count