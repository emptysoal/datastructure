"""
    快速排序
"""


def quick_sort(li):
    inner(li, 0, len(li) - 1)
    return li


def inner(li, first, last):
    if first >= last:
        return
    target = li[first]
    left = first
    right = last
    while left < right:
        while li[right] >= target and left < right:
            right -= 1
        while li[left] <= target and left < right:
            left += 1
        li[left], li[right] = li[right], li[left]
    li.insert(left + 1, target)
    li.pop(first)

    inner(li, first, left - 1)
    inner(li, left + 1, last)


if __name__ == '__main__':
    li = [3, 8, 5, 15, 9, 20, 45, 6, 25, 34, 13, 62, 1, 19, 7, 10]
    res = quick_sort(li)
    print(res)
