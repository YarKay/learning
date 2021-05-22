from BiTree_defination import BiTree
from BiTree_defination import instance

# 中序遍历


def inOrder(root: BiTree):
    stack = []
    res = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        if stack:
            root = stack.pop()
            res.append(root.val)
            root = root.right
    return res


# 递归方式中序遍历
def inOrder_recusion(root: BiTree, res=[]):
    if root != None:
        res = inOrder_recusion(root.left, res)
        res.append(root.val)
        res = inOrder_recusion(root.right, res)
    return res

# 非递归方法结果
print("非递归: " + " ".join([str(i) for i in inOrder(instance)]))

# 递归法结果
print("递  归: " +" ".join([str(i) for i in inOrder_recusion(instance)]))
