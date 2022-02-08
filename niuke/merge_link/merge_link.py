# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pHead = ListNode(None)
        cur = pHead
        while True:
            if pHead1 is None:
                cur.next = pHead2
                break
            elif pHead2 is None:
                cur.next = pHead1
                break
            else:
                if pHead1.val < pHead2.val:
                    cur.next = pHead1
                    cur = cur.next
                    pHead1 = pHead1.next
                else:
                    cur.next = pHead2
                    cur = cur.next
                    pHead2 = pHead2.next
        return pHead.next
