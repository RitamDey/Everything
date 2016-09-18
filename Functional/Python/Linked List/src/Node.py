class Node:
    """
    A Implementation Of Singly Linked List in Python 3
    """

    def __init__(self, data, next_node):
        self.data = data
        self.node = next_node

    def append(self, data):
        """
        This method append a new at the end of the linked list
        """
        if self.node:
            self.node.append(data)
        else:
            self.node = Node(data, None)

    def pop(self):
        """
        A method exactly like the list's pop
        :return: The popped Node object's data
        """
        if self.node.node:
            return self.node.pop()
        else:
            tmp = self.node.data
            self.node = None
            return tmp

    def __delete__(self, instance):
        pass