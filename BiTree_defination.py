class BiTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# instance 为一个每个节点值都为其对应编号的3层满二叉树
instance = BiTree(1)
instance.left = BiTree(2)
instance.right = BiTree(3)
instance.left.left = BiTree(4)
instance.left.right = BiTree(5)
instance.right.left = BiTree(6)
instance.right.right = BiTree(7)
