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



if __name__ == '__main__':
    unittest.main()