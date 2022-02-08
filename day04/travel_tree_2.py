"""
    【1】题目描述
        请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印， 第二层按照从右至左的顺序打印，
     第三行按照从左到右的顺序打印，其他行以此类推

    【2】试题解析
        1、采用层次遍历的思想，用队列或者栈（先进先出或后进先出，此处二选一，我们选择栈）
        2、把每一层的节点添加到一个栈中，添加时判断是奇数层还是偶数层
           a) 奇数层：栈中存储时，二叉树中节点从右向左append，出栈时pop()则从左向右打印输出
           b) 偶数层: 栈中存储时，二叉树中节点从左向右append，出栈时pop()则从右向左打印输出
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def print_binarytree(self, root):
        res = []
        mid_res = []

        if not root:
            return res

        level = 1
        cur_stack = [root]
        next_stack = []
        while cur_stack:
            node = cur_stack.pop()
            mid_res.append(node.val)

            if level % 2 == 1:
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            else:
                if node.right:
                    next_stack.append(node.right)
                if node.left:
                    next_stack.append(node.left)

            if not cur_stack:
                cur_stack, next_stack = next_stack, cur_stack
                level += 1
                res.append(mid_res)
                mid_res = []

        return res


if __name__ == '__main__':
    t1 = Node(1)
    t2 = Node(2)
    t3 = Node(3)
    t4 = Node(4)
    t5 = Node(5)
    t6 = Node(6)
    t7 = Node(7)
    t8 = Node(8)
    t9 = Node(9)
    t10 = Node(10)
    # 开始创建树
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t4.left = t8
    t4.right = t9
    t5.left = t10
    t3.left = t6
    t3.right = t7

    s = Solution()
    result = s.print_binarytree(t1)
    for item in result:
        print(item)
