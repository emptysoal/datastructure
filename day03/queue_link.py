"""
    python实现队列 - 链式结构
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        return not self.head

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def dequeue(self):
        if self.is_empty():
            raise Exception('dequeue from empty queue')
        cur = self.head
        self.head = self.head.next

        return cur.val

    def size(self):
        if self.is_empty():
            return 0
        count = 0
        cur = self.head
        while cur:
            cur = cur.next
            count += 1
        return count


if __name__ == '__main__':
    q = Queue()
    q.enqueue(100)
    q.enqueue(200)
    q.enqueue(300)
    print(q.is_empty())
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
