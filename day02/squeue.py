"""
    队列：入队、出队、判断是否为空
"""


class SQueue:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return not self.elems

    def push(self, val):
        self.elems.append(val)

    def pop(self):
        if self.is_empty():
            raise Exception('pop from empty queue')
        return self.elems.pop(0)


if __name__ == '__main__':
    sq = SQueue()
    print(sq.is_empty())
    sq.push(100)
    sq.push(200)
    print(sq.is_empty())
    print(sq.pop())
    print(sq.pop())
