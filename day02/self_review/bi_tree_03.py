"""
    二叉树
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root

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

    def pre_travel(self, node=None):
        if not node:
            return []
        res = [node.val]
        left = self.pre_travel(node.left)
        right = self.pre_travel(node.right)
        res += left
        res += right
        return res

    def mid_travel(self, node=None):
        if not node:
            return []
        res = []
        left = self.mid_travel(node.left)
        res += left
        res.append(node.val)
        right = self.mid_travel(node.right)
        res += right
        return res

    def post_travel(self, node=None):
        if not node:
            return []
        res = []
        left = self.post_travel(node.left)
        res += left
        right = self.post_travel(node.right)
        res += right
        res.append(node.val)
        return res


if __name__ == '__main__':
    t = Tree()
    t.add('A')
    t.add('B')
    t.add('C')
    t.add('D')
    t.add('E')
    t.add('F')
    print(t.breadth_travel())
    print(t.pre_travel(t.root))
    print(t.mid_travel(t.root))
    print(t.post_travel(t.root))
