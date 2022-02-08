"""
    【1】题目描述
        输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不 能创建任何新的结点，只能调整树中节点指针的指向

    【2】试题解析
        a> 二叉搜索树的中序遍历是一个不减的排序结果，因此先将二叉树搜索树中序遍历
        b> 将遍历后的结果用相应的指针连接起来
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_kth_node(self, root, k):
        array_list = self.mid_travel(root)
        if k <= 0 or len(array_list) < k:
            return
        return array_list[k - 1]

    def mid_travel(self, node):
        if not node:
            return []
        res = []
        left = self.mid_travel(node.left)
        res += left
        res.append(node.val)
        right = self.mid_travel(node.right)
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
    result = s.get_kth_node(t12, 4)
    print(result)
