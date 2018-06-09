import unittest
from node import Node
from stack import Stack


class TestLinkedList(unittest.TestCase):

    def test_node_creation(self):
        name = "Jose"

        node = Node(name)

        self.assertEqual(name, node.text)

    def test_stack_creation(self):
        stack = Stack()

        self.assertIsNone(stack.get_root())

    def test_add_to_stack_start(self):
        name = "Jose"

        node = Node(name)

        stack = Stack()

        stack.add_to_stack_start(node)

        self.assertEqual(stack.get_root(), node)

    def test_add_many_to_stack_start(self):
        names = ("Jose", "Rolf", "Anna")

        nodes = [Node(name) for name in names]

        stack = Stack()

        for node in nodes:
            stack.add_to_stack_start(node)

        marker = stack.get_root()
        for i in range(len(nodes)-1, -1, -1):
            self.assertEqual(marker, nodes[i])
            marker = marker.get_next()

    def test_remove_start_from_stack(self):
        names = ("Jose", "Rolf", "Anna")

        nodes = [Node(name) for name in names]

        stack = Stack()

        for node in nodes:
            stack.add_to_stack_start(node)

        self.assertIsNotNone(stack.find("Jose"))

        popped_node = stack.remove_start_from_stack()

        self.assertEqual(popped_node, nodes[len(nodes) - 1])

        with self.assertRaises(LookupError):
            stack.find("Anna")

    def test_find_in_stack(self):
        names = ("Jose", "Rolf", "Anna")

        nodes = [Node(name) for name in names]

        stack = Stack()

        for node in nodes:
            stack.add_to_stack_start(node)

        marker = stack.get_root()
        for i in range(len(nodes) - 1, -1, -1):
            self.assertEqual(stack.find(marker.text), nodes[i])
            marker = marker.get_next()

    def test_find_missing_in_stack(self):
        stack = Stack()

        with self.assertRaises(LookupError):
            stack.find("Smith")


if __name__ == '__main__':
    unittest.main()