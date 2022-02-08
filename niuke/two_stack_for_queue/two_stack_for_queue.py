class Stack:
    def __init__(self):
        self.list_s = []

    def push(self, val):
        self.list_s.append(val)

    def is_empty(self):
        return not self.list_s

    def pop(self):
        if not self.is_empty():
            return self.list_s.pop()
        else:
            return False


class Queue:
    def __init__(self):
        self.s_in = Stack()
        self.s_out = Stack()

    def push(self, val):
        while not self.s_out.is_empty():
            self.s_in.push(self.s_out.pop)
        else:
            self.s_in.push(val)

    def pop(self):
        while not self.s_in.is_empty():
            self.s_out.push(self.s_in.pop())
        else:
            if self.s_out.is_empty():
                return False
            else:
                return self.s_out.pop()


if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
