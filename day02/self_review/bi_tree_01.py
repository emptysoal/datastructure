"""
    二叉树
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, node=None):
        self.root = node

    def add(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
            return
        q = [self.root]
        while q:
            obj = q.pop(0)
            if obj.left:
                q.append(obj.left)
            else:
                obj.left = node
                return
            if obj.right:
                q.append(obj.right)
            else:
                obj.right = node
                return

    def breadth_travel(self):
        if not self.root:
            return
        q = [self.root]
        res = []
        while q:
            obj = q.pop(0)
            res.append(obj.val)
            if obj.left:
                q.append(obj.left)
            if obj.right:
                q.append(obj.right)
        return res

    def pre_travel(self, node):
        if not node:
            return []
        res = [node.val]
        res_left = self.pre_travel(node.left)
        res_right = self.pre_travel(node.right)
        res += res_left
        res += res_right
        return res

    def in_travel(self, node):
        if not node:
            return []
        res = []
        res_left = self.in_travel(node.left)
        res += res_left
        res.append(node.val)
        res_right = self.in_travel(node.right)
        res += res_right
        return res

    def post_travel(self, node):
        if not node:
            return []
        res = []
        res_left = self.post_travel(node.left)
        res += res_left
        res_right = self.post_travel(node.right)
        res += res_right
        res.append(node.val)
        return res


if __name__ == '__main__':
    node = Node('A')
    t = Tree(node)
    t.add('B')
    t.add('C')
    t.add('D')
    t.add('E')
    t.add('F')
    print(t.breadth_travel())
    print(t.pre_travel(node))
    print(t.in_travel(node))
    print(t.post_travel(node))
