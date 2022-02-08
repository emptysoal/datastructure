lis = [
    [1, 3, 4, 5, 8],
    [2, 6, 7, 9, 12],
    [7, 10, 14, 15, 18],
    [11, 13, 16, 19, 21]
]


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        c = len(array) - 1
        r = 0
        while c >= 0 and r <= len(array[0]) - 1:
            if target > array[c][r]:
                r += 1
            elif target < array[c][r]:
                c -= 1
            else:
                return True
        else:
            return False


for i in range(25):
    s = Solution().Find(i, lis)
    print(i, s)
