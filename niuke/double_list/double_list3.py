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
        return self.find_num(target, array, c, 0)

    def find_num(self, target, array, c=0, r=0):
        if target == array[c][r]:
            return True
        elif target > array[c][r]:
            r += 1
            if r < len(array[0]):
                return self.find_num(target, array, c, r)
            return False

        elif target < array[c][r]:
            c -= 1
            if c >= 0:
                return self.find_num(target, array, c, r)
            return False


s = Solution().Find(24, lis)
print(s)
