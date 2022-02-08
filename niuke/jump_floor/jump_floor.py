# -*- coding:utf-8 -*-

"""
    floor_num     method
        1            1
        2            1*2  2 -> 2
        3            1*3  1*1+2*1(2*1) -> 3
        4            1*4  1*2+2*1(第一个位置1:1*2*1 + 第一个位置2:1*1*1 = 3)  2*2(1)  ->  5
        5            1*5  1*3+2*1(f1:4个台阶时的3种 + f2:1*1*1 = 4) 1*1+2*2(f1:1 + f2:2 = 3) -> 8
        6            1*6  1*4+2*1(f1:5台阶的4 + f2:1 = 5)  1*2+2*2(f1:5台阶的3 + f2:4台阶的3 = 6)  2*3(1) -> 13
"""

"""
    floor_num     method
        1            1
        2            第一个为1 -> 1 + 第一个为2 -> 1 = 2
        3            第一个为1 -> 2(2个台阶时的情况) + 第一个为2 -> 1(1个台阶时的情况) = 3
        4            第一个为1 -> 3(3个台阶时的情况) + 第一个为2 -> 2(2个台阶时的情况) = 5
        5            第一个为1 -> 5(4个台阶时的情况) + 第一个为2 -> 3(3个台阶时的情况) = 8
        6            第一个为1 -> 8(5个台阶时的情况) + 第一个为2 -> 5(4个台阶时的情况) = 3
        ...
        n            第一个为1 -> x(n-1个台阶时的情况) + 第一个为2 -> y(n-2个台阶时的情况) = target
"""


class Solution:
    def jumpFloor(self, number):
        # write code here
        count = 0
        n1 = 1
        n2 = 2
        if number == 1:
            target = n1
        elif number == 2:
            target = n2
        else:
            while number - 2 > count:
                """
                    number   ccount
                      3   ->   1
                      4   ->   2
                      5   ->   3
                      ...
                """
                target = n1 + n2
                count += 1
                n1 = n2
                n2 = target
        return target


if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(10))
