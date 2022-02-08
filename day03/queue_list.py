"""
    python实现队列 - 顺序存储
"""


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return not self.queue

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise Exception('pop from empty queue')
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())
    print(q.size())
    print(q.dequeue())
    print(q.is_empty())
    print(q.size())
