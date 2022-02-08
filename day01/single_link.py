"""
    单链表实现
"""


# 节点类
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# 单链表类
class SingleLinkList:
    def __init__(self, node=None):
        self.head = node

    def multi_append(self, lis):
        current = self.head
        if current:
            while current.next:
                current = current.next
            for item in lis:
                node = Node(item)
                current.next = node
                current = current.next
        else:
            self.head = Node(lis[0])
            self.multi_append(lis[1:])

    def is_empty(self):
        return self.head is None

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def travel(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    # def insert(self, value, index):
    #     if index <= 0:
    #         self.add(value)
    #     elif index >= self.length():
    #         self.append(value)
    #     else:
    #         pre = self.head
    #         for i in range(1, index):
    #             pre = pre.next
    #         node = Node(value)
    #         node.next = pre.next
    #         pre.next = node

    def insert(self, value, index):
        if index <= 0:
            self.add(value)
            return
        current = self.head
        pre = current
        for i in range(1, index + 1):
            if current:
                pre = current
                current = current.next
            else:
                self.append(value)
                return
        node = Node(value)
        pre.next = node
        node.next = current

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            else:
                current = current.next
        return False

    def remove(self, value):
        current = self.head
        if not current:
            raise ('the value is not in link')
        if current.value == value:
            self.head = current.next
        else:
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    break
                current = current.next
            else:
                raise ('the value is not in link')


if __name__ == '__main__':
    single = SingleLinkList()
    single.multi_append([6, 7, 8, 9, 10])
    single.travel()
    print('---------------')
    single.insert(100, 6)
    single.travel()
