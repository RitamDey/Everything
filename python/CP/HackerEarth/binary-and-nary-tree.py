class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def append(self, data, pos):
        curr = pos[0]

        if curr == 'L':
            if self.left:
                self.left.append(data, pos[1:])
            else:
                self.left = Tree(data)
        elif curr == 'R':
            if self.right:
                self.right.append(data, pos[1:])
            else:
                self.right = Tree(data)


def height(tree):
    if tree.left is None and tree.right is None:
        return 1

    left = right = 0

    if tree.left:
        left += height(tree.left)

    if tree.right:
        right += height(tree.right)

    return max((left, right)) + 1


if __name__ == '__main__':
    length, root = input().split()
    tree = Tree(root)

    for _ in range(int(length)-1):
        pos = input()
        data = input()
        tree.append(data, pos)

    print(height(tree.left) + height(tree.right) + 1)
