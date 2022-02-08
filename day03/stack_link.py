"""
    Python实现栈 - 使用链式结构
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return not self.top

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise Exception('pop from empty stack')
        value = self.top.val
        self.top = self.top.next
        return value

    def size(self):
        if self.is_empty():
            return 0
        cur = self.top
        count = 0
        while cur:
            cur = cur.next
            count += 1
        return count


if __name__ == '__main__':
    s = Stack()
    s.push(100)
    s.push(200)
    s.push(300)
    print(s.size())
    print(s.pop())
    print(s.is_empty())
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s.is_empty())
