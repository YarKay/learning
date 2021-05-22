from BiTree_defination import BiTree
from BiTree_defination import instance


def levelOrder(root: BiTree):
    queue = [root]
    res = []
    while queue:
        root = queue.pop(0)
        res.append(root.val)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
    return res

  # 非递归方法结果
print("非递归: " + " ".join([str(i) for i in levelOrder(instance)]))
