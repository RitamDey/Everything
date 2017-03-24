def PostOrder(tree):
    if tree.left:
        PostOrder(tree.left)
    if tree.right:
        PostOrder(tree.right)
    print(tree.data, end=" ")

