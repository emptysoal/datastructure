"""
    栈：入栈、出栈、是否为空、查看栈顶元素
"""


class SStack:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return not self.elems

    def push(self, val):
        self.elems.append(val)

    def pop(self):
        if self.is_empty():
            raise Exception('pop from empty stack')
        return self.elems.pop()

    def top(self):
        if self.is_empty():
            raise Exception('top from empty stack')
        return self.elems[-1]


if __name__ == '__main__':
    st = SStack()
    print(st.is_empty())
    st.push(100)
    st.push(200)
    print(st.top())
