import unittest
from node import Node
from queue_model import Queue


class TestQueue(unittest.TestCase):


    def test_node_creation(self):
        name = "Jose"
        phone = "123-456-7890"

        node = Node(name, phone)

        self.assertEqual(name, node.name)
        self.assertEqual(phone, node.phone)

    def test_list_creation(self):
        linked_list = Queue()

        self.assertIsNone(linked_list.get_root())

    def test_enqueue(self):
        name = "Jose"
        phone = "123-456-7890"

        node = Node(name, phone)

        linked_list = Queue()

        linked_list.enqueue(node)

        self.assertEqual(linked_list.get_root(), node)

    def test_enqueue_many(self):
        names = ("Jose", "1234-356"), ("Rolf", "2345-1-53563-2"), ("Anna", "345623-16779-3")

        nodes = [Node(name, phone) for name, phone in names]

        linked_list = Queue()

        for node in nodes:
            linked_list.enqueue(node)

        marker = linked_list.get_root()
        for i in range(len(nodes)-1, -1, -1):
            self.assertEqual(marker, nodes[i])
            marker = marker.get_next()

    def test_dequeue(self):
        names = ("Jose", "1234-356"), ("Rolf", "2345-1-53563-2"), ("Anna", "345623-16779-3")

        nodes = [Node(name, phone) for name, phone in names]

        linked_list = Queue()

        for node in nodes:
            linked_list.enqueue(node)

        self.assertIsNotNone(linked_list.find("Jose"))

        popped_node = linked_list.dequeue()

        self.assertEqual(popped_node, nodes[0])

        with self.assertRaises(LookupError):
            linked_list.find("Jose")

    def test_find_in_list(self):
        names = ("Jose", "1234-356"), ("Rolf", "2345-1-53563-2"), ("Anna", "345623-16779-3")

        nodes = [Node(name, phone) for name, phone in names]

        linked_list = Queue()

        for node in nodes:
            linked_list.enqueue(node)

        marker = linked_list.get_root()
        for i in range(len(nodes) - 1, -1, -1):
            self.assertEqual(linked_list.find(marker.name), nodes[i])
            marker = marker.get_next()

    def test_find_missing_in_list(self):
        linked_list = Queue()

        with self.assertRaises(LookupError):
            linked_list.find("Smith")

    def test_push_to_queue(self):
        name = "Jose"
        phone = "123-456-7890"

        node = Node(name, phone)
        queue = Queue()

        queue.push(node)

        self.assertEqual(len(queue), 1)

    def test_pop_from_queue(self):
        name = "Jose"
        phone = "123-456-7890"

        node = Node(name, phone)
        queue = Queue()

        queue.push(node)

        self.assertEqual(len(queue), 1)

        popped = queue.pop()

        self.assertEqual(popped, node)
        self.assertEqual(len(queue), 0)

    def test_find_in_queue(self):
        name = "Jose"
        phone = "123-456-7890"

        node = Node(name, phone)
        queue = Queue()

        queue.push(node)

        self.assertEqual(queue.find(name), node)

if __name__ == '__main__':
    unittest.main()