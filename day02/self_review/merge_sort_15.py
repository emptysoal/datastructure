"""
    归并排序
"""


def merge_sort(li):
    if len(li) == 1:
        return li
    mid = len(li) // 2
    left_li = li[:mid]
    right_li = li[mid:]
    left = merge_sort(left_li)
    right = merge_sort(right_li)

    return merge(left, right)


def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res += left
    res += right
    return res


if __name__ == '__main__':
    li = [3, 8, 5, 15, 9, 20, 45, 6, 25, 34, 13, 62, 1, 19, 7, 10]
    res = merge_sort(li)
    print(res)
