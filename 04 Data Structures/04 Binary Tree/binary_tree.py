class BinaryTree:

    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add(self, node):
        if not self.__root:
            self.__root = node
        else:
            marker = self.__root
            while marker:
                if node.value == marker.value:
                    raise ValueError("Node's value already exists")
                elif node.value > marker.value:
                    if marker.get_right():
                        marker = marker.get_right()
                    else:
                        marker.set_right(node)
                        return
                else:
                    if marker.get_left():
                        marker = marker.get_left()
                    else:
                        marker.set_left(node)
                        return

    def find(self, value):
        marker = self.__root
        while marker:
            if value == marker.value:
                return marker
            elif value > marker.value:
                marker = marker.get_right()
            elif value < marker.value:
                marker = marker.get_left()

        raise LookupError("Value was not found.")

    def print_inorder(self):
        self.__print_inorder_r(self.__root)

    def __print_inorder_r(self, current_node):
        if not current_node:
            return
        self.__print_inorder_r(current_node.get_left())
        print(current_node.print_details())
        self.__print_inorder_r(current_node.get_right())
