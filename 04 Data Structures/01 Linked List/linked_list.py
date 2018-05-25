from node import Node

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
            marker.display_node()
            marker = marker.get_next()

    def delete_element_from_position(self, head, position):
        if position == 0:
            return head.get_next()

        head.set_next(self.delete_element_from_position(head.get_next(), position - 1))
        return head

    def insert_at_tail(self, head, node):
        if not head:
            return node
        else:
            if not head.get_next():
                head.set_next(node)
            else:
                self.insert_at_tail( head.get_next(), node)
            return head

    def delete_year_greater_than(self, head, year):
        if not head:
            return None
        
        if head.get_year() > year:
            self.__root = head.get_next()

            return self.delete_year_greater_than(self.__root, year)

        if not head.get_next():
            if head.get_year() > year:
                return None
            return head

        if head.get_next().get_year() > year:
            if head.get_next().get_next():
                head.set_next(head.get_next().get_next())
                return self.delete_year_greater_than ( head.get_next (), year )
            else:
                head.set_next(None)
        else:
            return self.delete_year_greater_than(head.get_next(), year)






