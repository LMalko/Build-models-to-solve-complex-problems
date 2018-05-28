import unittest
from node import Node
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_node_creation(self):
        name = "Jose"
        matric = "1234"
        year = 2

        node = Node(name, matric, year)

        self.assertEqual(name, node.get_name())
        self.assertEqual(matric, node.matric)
        self.assertEqual(year, node.year)

    def test_list_creation(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.get_root())

    def test_add_to_list(self):
        name = "Jose"
        matric = "1234"
        year = 2

        node = Node(name, matric, year)

        linked_list = LinkedList()

        linked_list.add_to_list(node)

        self.assertEqual(linked_list.get_root(), node)

    def test_add_many_to_list(self):
        names = ("Jose", "1234", 2), ("Rolf", "2345", 3), ("Anna", "3456", 7)

        nodes = [Node(name, matric, year) for name, matric, year in names]

        linked_list = LinkedList()

        for node in nodes:
            linked_list.add_to_list(node)

        marker = linked_list.get_root()
        for i in range(len(nodes)-1, -1, -1):
            self.assertEqual(marker, nodes[i])
            marker = marker.get_next()

    def test_find_in_list(self):
        names = ("Jose", "1234", 2), ("Rolf", "2345", 3), ("Anna", "3456", 7)

        nodes = [Node(name, matric, year) for name, matric, year in names]

        linked_list = LinkedList()

        for node in nodes:
            linked_list.add_to_list(node)

        marker = linked_list.get_root()
        for i in range(len(nodes) - 1, -1, -1):
            self.assertEqual(linked_list.find_name(marker.get_name()), nodes[i])
            marker = marker.get_next()

    def test_find_missing_in_list(self):
        linked_list = LinkedList()

        with self.assertRaises(LookupError):
            linked_list.find_name("Smith")

    def test_delete_element_from_position(self):
        names = ("Jose", "1234", 2), ("Rolf", "2345", 3), \
                ("Anna", "3456", 7), ("James", "2675", 5)

        nodes = [Node(name, matric, year) for name, matric, year in names]
        linked_list = LinkedList()

        for node in nodes:
            linked_list.add_to_list(node)

        linked_list.delete_element_from_position(linked_list.get_root(), 2)

        nodes_after_delete = [node for node in nodes if node.get_name() != "Rolf"]

        marker = linked_list.get_root ()
        for i in range ( len (nodes_after_delete) - 1, -1, -1 ):
            self.assertEqual(linked_list.find_name(marker.get_name()), nodes_after_delete[i] )
            marker = marker.get_next()

    def test_insert_at_tail(self):
        names = ("Jose", "1234", 2), ("Rolf", "2345", 3), ("Anna", "3456", 7)

        nodes = [Node(name, matric, year) for name, matric, year in names]

        linked_list = LinkedList()

        for node in nodes:
            linked_list.add_to_list ( node )

        marker = linked_list.get_root ()

        last_node = Node("George", "3232", 3)
        linked_list.insert_at_tail(marker, last_node)
        nodes.insert(0, last_node)

        for i in range ( len ( nodes ) - 1, -1, -1 ):
            self.assertEqual ( linked_list.find_name ( marker.get_name () ), nodes[i] )
            marker = marker.get_next ()

    def test_delete_year_greater_than_1(self):
        names = ("Jose", "1234", 7), ("Rolf", "2345", 7), \
                ("Anna", "3456", 7), ("James", "2675", 7)

        nodes = [Node(name, matric, year) for name, matric, year in names]
        linked_list = LinkedList()

        for node in nodes:
            linked_list.add_to_list(node)

        nodes_after_delete = [node for node in nodes if node.get_name() in []]

        marker = linked_list.get_root()

        linked_list.delete_year_greater_than(marker, 3)

        # Make sure the head is updated, it could have been assigned to the node that meets
        # has year <= than .
        marker = linked_list.get_root()

        for i in range ( len (nodes_after_delete) - 1, -1, -1 ):
            self.assertEqual(linked_list.find_name(marker.get_name()), nodes_after_delete[i] )
            marker = marker.get_next()

    def test_delete_year_greater_than_2(self):
        names = ("Jose", "1234", 7), ("Rolf", "2345", 7), \
                ("Anna", "3456", 7), ("James", "2675", 3)

        nodes = [Node ( name, matric, year ) for name, matric, year in names]
        linked_list = LinkedList ()

        for node in nodes:
            linked_list.add_to_list ( node )

        nodes_after_delete = [node for node in nodes if node.get_name () in ["James"]]

        marker = linked_list.get_root ()

        linked_list.delete_year_greater_than ( marker, 3 )

        marker = linked_list.get_root ()

        for i in range ( len ( nodes_after_delete ) - 1, -1, -1 ):
            self.assertEqual ( linked_list.find_name ( marker.get_name () ), nodes_after_delete[i] )
            marker = marker.get_next ()

    def test_delete_year_greater_than_3(self):
        names = ("Jose", "1234", 2), ("Rolf", "2345", 2), \
                ("Anna", "3456", 2), ("James", "2675", 7)

        nodes = [Node ( name, matric, year ) for name, matric, year in names]
        linked_list = LinkedList ()

        for node in nodes:
            linked_list.add_to_list ( node )

        nodes_after_delete = [node for node in nodes if node.get_name () in ["Anna", "Rolf", "Jose"]]

        marker = linked_list.get_root ()

        linked_list.delete_year_greater_than ( marker, 3 )
        marker = linked_list.get_root ()

        for i in range ( len ( nodes_after_delete ) - 1, -1, -1 ):
            self.assertEqual ( linked_list.find_name ( marker.get_name () ), nodes_after_delete[i] )
            marker = marker.get_next ()

    def test_insert_at_position1(self):
        names = ("Jose", "1234", 7), ("Rolf", "2345", 7), \
                ("Anna", "3456", 7), ("James", "2675", 7)

        nodes = [Node ( name, matric, year ) for name, matric, year in names]
        linked_list = LinkedList ()

        for node in nodes:
            linked_list.add_to_list(node)

        new_node = Node("Becky", "9898", 3)

        # Insert at the beginning.

        nodes.insert(4, new_node)
        linked_list.insert_at_position(linked_list.get_root(), new_node, 0)

        marker = linked_list.get_root()

        for i in range(len(nodes) - 1, -1, -1):
            self.assertEqual(linked_list.find_name(marker.get_name()), nodes[i])
            marker = marker.get_next ()

    def test_insert_at_position2(self):
        names = ("Jose", "1234", 7), ("Rolf", "2345", 7), \
                ("Anna", "3456", 7), ("James", "2675", 7)

        nodes = [Node ( name, matric, year ) for name, matric, year in names]
        linked_list = LinkedList ()

        for node in nodes:
            linked_list.add_to_list(node)

        new_node = Node("Becky", "9898", 3)

        # Insert at the end.
        nodes.insert(0, new_node)
        linked_list.insert_at_position(linked_list.get_root(), new_node, 4)

        marker = linked_list.get_root ()

        for i in range(len(nodes) - 1, -1, -1):
            self.assertEqual(linked_list.find_name(marker.get_name()), nodes[i])
            marker = marker.get_next ()

    def test_insert_at_position3(self):
        names = ("Jose", "1234", 7), ("Rolf", "2345", 7), \
                ("Anna", "3456", 7), ("James", "2675", 7)

        nodes = [Node ( name, matric, year ) for name, matric, year in names]
        linked_list = LinkedList ()

        for node in nodes:
            linked_list.add_to_list(node)

        new_node = Node("Becky", "9898", 3)

        # Insert in the middle.
        nodes.insert(3, new_node)
        linked_list.insert_at_position(linked_list.get_root(), new_node, 1)

        marker = linked_list.get_root ()

        for i in range(len(nodes) - 1, -1, -1):
            self.assertEqual(linked_list.find_name(marker.get_name()), nodes[i])
            marker = marker.get_next ()

    def test_reverse_linked_list(self):
        names = ("Jose", "1234", 7), ("Rolf", "2345", 7), \
                ("Anna", "3456", 7), ("James", "2675", 7)

        nodes = [Node ( name, matric, year ) for name, matric, year in names]



        linked_list = LinkedList ()

        for node in nodes:
            linked_list.add_to_list(node)

        nodes.reverse()
        linked_list.reverse_linked_list(linked_list.get_root())

        marker = linked_list.get_root()

        for i in range ( len ( nodes ) - 1, -1, -1 ):
            self.assertEqual(linked_list.find_name(marker.get_name () ), nodes[i])
            marker = marker.get_next ()


if __name__ == '__main__':
    unittest.main()