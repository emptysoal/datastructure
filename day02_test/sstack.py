"""
    实现顺序栈
        入栈、出栈、判断栈是否为空
"""


class SStack:
    def __init__(self):
        self.elems = []

    def push(self, value):
        self.elems.append(value)

    def is_empty(self):
        return not self.elems

    def pop(self):
        if self.is_empty():
            raise Exception('pop from empty stack')
        return self.elems.pop()

    def top(self):
        if self.is_empty():
            raise Exception('top from empty stack')
        return self.elems[-1]


if __name__ == '__main__':
    s = SStack()
    s.push(9)
    print(s.top())
    s.pop()
    print(s.top())
