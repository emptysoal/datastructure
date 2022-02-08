class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        lis = []
        while listNode:
            lis.append(listNode.val)
            listNode = listNode.next
        return lis[::-1]


if __name__ == '__main__':
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    # class LinkList:
    #     def __init__(self):
    #         self.head = ListNode(None)
    #
    #     def init_link(self, lis):
    #         p = self.head
    #         for item in lis:
    #             p.next = ListNode(item)
    #             p = p.next
    #
    #     def show_link(self):
    #         p = self.head.next
    #         while p:
    #             print(p.val)
    #             p = p.next
    #
    #
    # l = LinkList()
    # l.init_link([1, 2, 3, 4, 5])
    # l.show_link()
