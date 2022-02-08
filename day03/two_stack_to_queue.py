"""
    两个栈实现一个队列
"""


class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, value):
        while self.out_stack:
            self.in_stack.append(self.out_stack.pop())
        self.in_stack.append(value)

    def dequeue(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        if self.out_stack:
            return self.out_stack.pop()
        else:
            raise Exception('dequeue from empty queue')


if __name__ == '__main__':
    q = Queue()
    q.enqueue(100)
    q.enqueue(200)
    print(q.dequeue())
    q.enqueue(300)
    print(q.dequeue())
    q.enqueue(400)
    print(q.dequeue())
    print(q.dequeue())
