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

    def test_queue_creation(self):
        queue = Queue()

        self.assertIsNone(queue.get_root())

    def test_enqueue(self):
        name = "Jose"
        phone = "123-456-7890"

        node = Node(name, phone)

        queue = Queue()

        queue.enqueue(node)

        self.assertEqual(queue.get_root(), node)

    def test_enqueue_many(self):
        names = ("Jose", "1234-356"), ("Rolf", "2345-1-53563-2"), ("Anna", "345623-16779-3")

        nodes = [Node(name, phone) for name, phone in names]

        queue = Queue()

        for node in nodes:
            queue.enqueue(node)

        marker = queue.get_root()
        for i in range(len(nodes)-1, -1, -1):
            self.assertEqual(marker, nodes[i])
            marker = marker.get_next()

    def test_dequeue(self):
        names = ("Jose", "1234-356"), ("Rolf", "2345-1-53563-2"), ("Anna", "345623-16779-3")

        nodes = [Node(name, phone) for name, phone in names]

        queue = Queue()

        for node in nodes:
            queue.enqueue(node)

        self.assertIsNotNone(queue.find_name("Jose"))

        popped_node = queue.dequeue()

        self.assertEqual(popped_node, nodes[0])

        with self.assertRaises(LookupError):
            queue.find_name("Jose")

    def test_find_in_queue(self):
        names = ("Jose", "1234-356"), ("Rolf", "2345-1-53563-2"), ("Anna", "345623-16779-3")

        nodes = [Node(name, phone) for name, phone in names]

        queue = Queue()

        for node in nodes:
            queue.enqueue(node)

        marker = queue.get_root()
        for i in range(len(nodes) - 1, -1, -1):
            self.assertEqual(queue.find_name(marker.name), nodes[i])
            marker = marker.get_next()

    def test_find_missing_in_queue(self):
        queue = Queue()

        with self.assertRaises(LookupError):
            queue.find_name("Smith")

    def test_push_to_queue(self):
        name = "Jose"
        phone = "123-456-7890"

        node = Node(name, phone)
        queue = Queue()

        queue.enqueue(node)

        self.assertEqual(queue.size(), 1)

    def test_pop_from_queue(self):
        name = "Jose"
        phone = "123-456-7890"

        node = Node(name, phone)
        queue = Queue()

        queue.enqueue(node)

        self.assertEqual(queue.size(), 1)

        popped = queue.dequeue()

        self.assertEqual(popped, node)
        self.assertEqual(queue.size(), 0)

    def test_find_in_queue2(self):
        name = "Jose"
        phone = "123-456-7890"

        node = Node(name, phone)
        queue = Queue()

        queue.enqueue(node)

        self.assertEqual(queue.find_name(name), node)

    def peek(self):
        names = ("Jose", "1234-356"), ("Rolf", "2345-1-53563-2"), ("Anna", "345623-16779-3")

        nodes = [Node(name, phone) for name, phone in names]

        queue = Queue()

        for node in nodes:
            queue.enqueue(node)

        print(queue.peek())


if __name__ == '__main__':
    unittest.main()