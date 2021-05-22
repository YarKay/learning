from BiTree_defination import BiTree
from BiTree_defination import instance

# 前序遍历


def preOrder(root: BiTree):
    stack = []
    res = []
    while root or stack:
        while root:
            res.append(root.val)
            stack.append(root)
            root = root.left
        if stack:
            root = stack.pop().right
    return res


# 递归方式前序遍历
def preOrder_recusion(root: BiTree, res=[]):
    if root != None:
        res.append(root.val)
        res = preOrder_recusion(root.left, res)
        res = preOrder_recusion(root.right, res)
    return res

# 非递归方法结果
print("非递归: " + " ".join([str(i) for i in preOrder(instance)]))

# 递归法结果
print("递  归: " +" ".join([str(i) for i in preOrder_recusion(instance)]))
