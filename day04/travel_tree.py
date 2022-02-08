"""
    【1】题目描述
        从上到下按层打印二叉树，同一层结点从左至右输出，每一层输出一行

    【2】试题解析
        1、广度遍历，利用队列思想
        2、要有2个队列，分别存放当前层的节点 和 下一层的节点
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def print_node_layer(self, root):
        res = []
        mid_res = []
        if not root:
            return res
        cur_queue = [root]
        next_queue = []
        while cur_queue:
            node = cur_queue.pop(0)
            mid_res.append(node.val)

            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)

            if not cur_queue:
                cur_queue, next_queue = next_queue, cur_queue
                res.append(mid_res)
                mid_res = []

        return res


if __name__ == '__main__':
    s = Solution()
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

    result = s.print_node_layer(t1)
    for item in result:
        print(item)
