# -*- coding:utf-8 -*-

s = 'We Are Happy'


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        list_s = []
        for item in s:
            if item == ' ':
                item = '%20'
            list_s.append(item)
        return ''.join(list_s)


so = Solution().replaceSpace(s)
print(so)
