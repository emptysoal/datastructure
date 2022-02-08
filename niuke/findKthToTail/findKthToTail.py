# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k <= 0:
            return
        point1 = head
        for i in range(k - 1):
            if point1.next:
                point1 = point1.next
            else:
                return
        point2 = head
        while point1.next:
            point1 = point1.next
            point2 = point2.next
        return point2
