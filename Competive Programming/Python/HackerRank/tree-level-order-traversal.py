def levelOrder(root):
    queue = [root, ]

    while queue:
        node = queue.pop(0)
        print(node.info, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

