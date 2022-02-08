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
    def convert_tree_link(self, root):
        array_list = self.mid_travel(root)
        if len(array_list) == 0:
            return
        if len(array_list) == 1:
            return root

        # 先把头节点和尾节点搞定
        array_list[0].left = None
        array_list[0].right = array_list[1]
        array_list[-1].left = array_list[-2]
        array_list[-1].right = None
        # 搞定中间节点
        for i in range(1, len(array_list) - 1):
            array_list[i].left = array_list[i - 1]
            array_list[i].right = array_list[i + 1]

        return array_list[0]

    def mid_travel(self, node):
        if not node:
            return []
        res = []
        left = self.mid_travel(node.left)
        res += left
        res.append(node)
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
    node = s.convert_tree_link(t12)
    while node:
        print(node.val, end=' ')
        node = node.right
