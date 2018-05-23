class LinkedList:

    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_to_list(self, node):
        #Add node the beginning of the linked list.
        if self.__root:
            node.set_next(self.__root)
        self.__root = node

    def find_name(self, name):
        marker = self.__root
        while marker:
            if marker.get_name() == name:
                return marker
            marker = marker.get_next()
        raise LookupError("End of list - no results")

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

