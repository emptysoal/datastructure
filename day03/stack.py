"""
    python实现栈 - 顺序存储方式
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def is_empty(self):
        return not self.stack

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise Exception('pop from empty stack')


if __name__ == '__main__':
    s = Stack()
    s.push(100)
    s.push(200)
    s.push(300)
    print(s.pop())
