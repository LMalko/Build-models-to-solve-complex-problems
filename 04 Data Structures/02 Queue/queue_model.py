class Queue:


    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def enqueue(self, node):
        #Add element to end of queue.
        if self.__root:
            node.set_next(self.__root)
        self.__root = node

    def find_name(self, name):
        marker = self.__root
        while marker:
            if marker.get_name() == name:
                return marker
            marker = marker.get_next()
        raise LookupError("End of queue - no results")

    def size(self):
        marker = self.__root
        count = 0
        while marker:
            count += 1
            marker = marker.get_next()
        return count

    def dequeue(self):
        # Remove element from front of queue.
        marker = self.__root

        if not marker.get_next():
            self.__root = None
            return marker

        while marker:

            if not marker.get_next().get_next():
                dropped_element = marker.get_next()
                marker.set_next(None)
                return dropped_element
            marker = marker.get_next()