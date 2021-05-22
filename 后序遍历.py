from BiTree_defination import BiTree
from BiTree_defination import instance


# 非递归方式后序遍历
def postOrder(root: BiTree):
    instack = []
    outstack = []
    res = []
    while root or outstack:
        while root:
            outstack.append(root)
            instack.append(root)
            root = root.right
        if outstack:
            root = outstack.pop().left
    while instack:
        res.append(instack.pop().val)
    return res


# 递归方式前序遍历
def postOrder_recusion(root: BiTree, res=[]):
    if root != None:
        res = postOrder_recusion(root.left, res)
        res = postOrder_recusion(root.right, res)
        res.append(root.val)
    return res


# 非递归方法结果
print("非递归: " + " ".join([str(i) for i in postOrder(instance)]))

# 递归法结果
print("递  归: " + " ".join([str(i) for i in postOrder_recusion(instance)]))
