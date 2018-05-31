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

    # def reverse_list(node):
    #     temp = None
    #     while node:
    #         temp = Node ( node.value, temp )
    #         node = node.next
    #     return temp

    def compare_two_lists_by_name(self, head_a, head_b):

        while head_a and head_b:

            if head_a.get_name() != head_b.get_name():
                return False

            head_a = head_a.get_next()
            head_b = head_b.get_next ()

        return True if head_a == head_b else False

# 1.

# def reverse_doubly_linked_list(head):
#     if not head:
#         return head
#     head.next, head.prev = head.prev, head.next
#     if not head.prev:
#         return head
#     return reverse_doubly_linked_list(head.prev)

# 2.

# def get_node_from_position_from_tail(head, position_from_tail):
#     results = []
#
#     while head:
#         results.append(head)
#         head = head.next
#     # try:
#     #     del results[position_from_tail + 1]
#     # except:
#     #     pass
#
#     return results[- position_from_tail - 1]

# 3.
#   Merge two lists with data in ascending order into one lists
#   maintaining descending order

#       Sample Input:

#       1 -> 3 -> 5 -> 6 -> NULL
#       2 -> 4 -> 7 -> NULL

#       Output:         1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> NULL

# def merge_lists(headA, headB):
#     if not headB:
#         return headA
#     if not headA:
#         return headB
#
#     if headA.data < headB.data:
#         headA.next = merge_lists(headA.next, headB)
#         return headA
#     else:
#         headB.next = merge_lists(headA, headB.next)
#         return headB


# 4.
# def removeDuplicates(head):
#     cur = head
#     while cur.next != None:
#         if cur.data == cur.next.data:
#             cur.next = cur.next.next
#         else:
#             cur = cur.next
#     return head

# 5. Check if there are repeating elements in the linked_list, i.e. if there is a cycle

# def has_cycle(head):
#     lista = [head]
#     while head.next:
#         if head.next in lista:
#             return True
#         lista.append(head.next)
#         head = head.next
#     return False

# 6.

# def FindMergeNode(head_a, head_b):
#     temp_a, temp_b = head_a, head_b
#     while temp_a != temp_b:
#         temp_a, temp_b = temp_a.next or head_a, temp_b.next or head_b
#     return temp_a.data

# 7.
# Given a reference to the head of a doubly-linked list and an integer, ,
# create a new DoublyLinkedListNode object having data value
# and insert it into a sorted linked list.

# def sortedInsert(head, data):
#     node = DoublyLinkedListNode(data)
#     if (head == None):
#         return node
#     elif (data < head.data):
#         node.next = head
#         head.prev = node
#         return node
#     else:
#         node = sortedInsert(head.next, data)
#         head.next = node
#         node.prev = head
#         return head

