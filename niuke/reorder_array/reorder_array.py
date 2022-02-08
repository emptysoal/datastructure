# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        return sorted(array, key=lambda x: x % 2, reverse=True)


if __name__ == '__main__':
    l = [3, 6, 2, 7, 5, 4, 1, 9, 8]
    so = Solution()
    print(so.reOrderArray(l))
