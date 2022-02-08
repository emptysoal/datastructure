"""
    【1】题目描述
        给定一棵二叉搜索树，请找出其中的第 K 小的结点。例如，(5,3,7,2,4,6,8)中， 按结点数值大小顺序第三小结点的值是 4

    【2】试题解析
        1、二叉搜索树定义及特点
            a> 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
            b> 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
            c> 它的左、右子树也分别为二叉排序树
        2、二叉搜索树的中序遍历是递增的序列，利用中序遍历来解决
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_k_node(self, root, k):
        array_list = self.inorder_travel(root)
        if k <= 0 or len(array_list) < k:
            return
        return array_list[k - 1]

    def inorder_travel(self, root):
        if not root:
            return []
        res = []
        left = self.inorder_travel(root.left)
        res += left
        res.append(root.val)
        right = self.inorder_travel(root.right)
        res += right

        return res


if __name__ == '__main__':
    t12 = Node(12)
    t5 = Node(5)
    t18 = Node(18)
    t2 = Node(2)
    t9 = Node(9)
    t15 = Node(15)
    t19 = Node(19)
    t17 = Node(17)
    t16 = Node(16)
    # 开始创建二叉搜索树
    t12.left = t5
    t12.right = t18
    t5.left = t2
    t5.right = t9
    t18.left = t15
    t18.right = t19
    t15.right = t17
    t17.left = t16

    s = Solution()
    result = s.get_k_node(t12, 1)
    print(result)
