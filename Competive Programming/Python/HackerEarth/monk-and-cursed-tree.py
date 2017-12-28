class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def append(self, data):
        root = self

        if data > root.data:
            if root.left:
                root.left.append(data)
            else:
                root.left = Node(data)
        elif data < root.data:
            if root.right:
                root.right.append(data)
            else:
                root.right = Node(data)


