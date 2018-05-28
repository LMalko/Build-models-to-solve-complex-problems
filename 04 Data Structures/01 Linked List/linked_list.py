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

        def set_root(head):
            if head and head.get_year() <= year:
                return head
            if head.get_next():
                return set_root(head.get_next())
            return None

        self.__root = set_root(head)

        def check_rest(previous, head, year):
            if head.get_year() > year:
                if head.get_next():
                    previous.set_next(head.get_next())
                    return check_rest(previous, head.get_next(), year)
                else:
                    previous.set_next(None)
                    return
            previous.set_next(head)
            if head.get_next():
                return check_rest(head, head.get_next(), year)

        if self.__root:
            if self.__root.get_next():
                check_rest(self.__root, self.__root.get_next(), year)
            else:
                self.__root.set_next(None)

    def insert_at_position(self, head, node, position):

        if position == 0:
            self.__root = node
            node.set_next(head)
            return

        if position == 1:
            initial_next = head.get_next()
            head.set_next(node)
            node.set_next(initial_next)
            return

        self.insert_at_position(head.get_next(), node, position - 1)
        return head

    def reverse_print(self, head):
        if head:
            self.reverse_print(head.get_next())
            print(head.get_name())
        else:
            return

    def reverse_linked_list(self, head):

        if not head:
            return head

        if not head.get_next():
            self.__root = head
            return

        next_node = self.reverse_linked_list(head.get_next())
        # print(head.get_next().get_name(), "receives", head.get_name())
        head.get_next().set_next(head)
        # print(head.get_name(), "receives None")
        head.set_next(None)

        return next_node



# def reverse_doubly_linked_list(head):
#     if not head:
#         return head
#     head.next, head.prev = head.prev, head.next
#     if not head.prev:
#         return head
#     return reverse_doubly_linked_list(head.prev)





