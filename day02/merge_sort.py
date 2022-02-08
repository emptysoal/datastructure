"""
    归并排序
"""
import time


def merge_sort(li):
    # 递归出口
    if len(li) == 1:
        return li
    # 先分
    mid = len(li) // 2
    left_li = li[:mid]
    right_li = li[mid:]
    left_one = merge_sort(left_li)
    right_one = merge_sort(right_li)
    # 再合
    result = merge(left_one, right_one)
    return result


# def merge(left_one, right_one):
#     """[5, 6] -> [3, 8]"""
#     result = []
#     left = 0
#     right = 0
#     while left < len(left_one) and right < len(right_one):
#         if left_one[left] > right_one[right]:
#             result.append(right_one[right])
#             right += 1
#         else:
#             result.append(left_one[left])
#             left += 1
#     if left == len(left_one):
#         result += right_one[right:]
#     else:
#         result += left_one[left:]
#     return result


def merge(left_one, right_one):
    result = []
    while len(left_one) > 0 and len(right_one) > 0:
        if left_one[0] <= right_one[0]:
            result.append(left_one.pop(0))
        else:
            result.append(right_one.pop(0))
    result += left_one
    result += right_one
    return result


if __name__ == '__main__':
    li = [3, 8, 5, 15, 9, 20, 45, 6, 25, 34, 13, 62, 1, 19, 7, 10]
    start = time.time()
    res = merge_sort(li)
    print(res)
    end = time.time()
    print(end - start)
