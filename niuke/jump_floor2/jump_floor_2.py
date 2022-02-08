"""
    floor_num     method
        1            1
        2            第一个为1(剩余的同1个台阶情况) -> 1 + 第一个为2 -> 1 = 2
        3            第一个为1(剩余的同2个台阶情况) -> 2 +
                     第一个为2(剩余的同1个台阶情况) -> 1 +
                     第一个为3 -> 1 = 4
        4            第一个为1(剩余的同3个台阶情况) -> 4 +
                     第一个为2(剩余的同2个台阶情况) -> 2 +
                     第一个为3(剩余的同1个台阶情况) -> 1 +
                     第一个为4 -> 1 = 8
        ...
        n            前面的全部相加，再加上自身
"""

"""
    floor_num     method
        1            1
        2            2
        3            4
        4            8
        5            16
        6            32
        ...
        n            2^(n-1)
"""


# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2 ** (number - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloorII(5))
