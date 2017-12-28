class BinaryTree:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left
    
    def PreOrder(self):
        data = self.data
        if self.left:
            data+=self.left.PreOrder()
        if self.right:
            data+=self.right.PreOrder()
        return data
   
   def PostOrder(tree):
    if tree.left:
        PostOrder(tree.left)
    if tree.right:
        PostOrder(tree.right)
    print(tree.data, end=" ")

