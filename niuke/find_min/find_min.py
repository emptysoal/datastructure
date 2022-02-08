class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        left = 0
        right = len(rotateArray) - 1
        if rotateArray[left] < rotateArray[right]:
            return rotateArray[left]
        while right - left > 1:
            middle = (left + right) // 2
            if rotateArray[left] <= rotateArray[middle]:
                left = middle
            elif rotateArray[right] >= rotateArray[middle]:
                right = middle
            elif rotateArray[left] == rotateArray[middle] == rotateArray[right]:
                # minval = rotateArray[left]
                # for item in rotateArray[left:right + 1]:
                minval = rotateArray[0]
                for item in rotateArray:
                    if item < minval:
                        minval = item
                return minval
        return rotateArray[right]


if __name__ == '__main__':
    # l = [4, 5, 6, 7, 8, 9, 2, 3]
    l2 = [2, 2, 1, 2, 2, 2, 2]
    s = Solution()
    re = s.minNumberInRotateArray(l2)
    print(re)
