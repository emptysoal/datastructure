"""
    二叉树
"""


class Node:
    def __init__(self, val, left_child=None, right_child=None):
        self.val = val
        self.left_child = left_child
        self.right_child = right_child


class Tree:
    def __init__(self, node=None):
        self.root = node

    def add(self, val):
        """添加一个节点"""
        node = Node(val)
        if not self.root:
            self.root = node
            return
        node_list = [self.root]
        while node_list:
            obj = node_list.pop(0)
            if not obj.left_child:
                obj.left_child = node
                return
            else:
                node_list.append(obj.left_child)
            if not obj.right_child:
                obj.right_child = node
                return
            else:
                node_list.append(obj.right_child)

    def breadth_travel(self):
        if not self.root:
            return
        node_list = [self.root]
        while node_list:
            obj = node_list.pop(0)
            print(obj.val, end=' ')
            if obj.left_child:
                node_list.append(obj.left_child)
            if obj.right_child:
                node_list.append(obj.right_child)

    def pre_travel(self, node):
        if not node:
            return
        print(node.val, end=' ')
        self.pre_travel(node.left_child)
        self.pre_travel(node.right_child)

    def in_travel(self, node):
        if not node:
            return
        self.in_travel(node.left_child)
        print(node.val, end=' ')
        self.in_travel(node.right_child)

    def post_travel(self, node):
        if not node:
            return
        self.post_travel(node.left_child)
        self.post_travel(node.right_child)
        print(node.val, end=' ')


if __name__ == '__main__':
    node = Node('A')
    tree = Tree(node)
    tree.add('B')
    tree.add('C')
    tree.add('D')
    tree.breadth_travel()
    print()
    tree.pre_travel(node)
    print()
    tree.in_travel(node)
    print()
    tree.post_travel(node)
