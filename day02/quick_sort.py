"""
    快速排序
"""
import time


def quick_sort(li, first, last):
    # 递归出口
    if first >= last:
        return

    # 一轮比较，右边遇到大的移动游标，左边遇到小的移动游标
    mid_value = li[first]
    left_cur = first
    right_cur = last
    while left_cur < right_cur:
        # right_cur左移
        while li[right_cur] >= mid_value and right_cur > left_cur:
            right_cur -= 1

        # left_cur右移
        while li[left_cur] <= mid_value and left_cur < right_cur:
            left_cur += 1
        # 两个循环结束，交换位置
        li[left_cur], li[right_cur] = li[right_cur], li[left_cur]
    li.insert(left_cur + 1, mid_value)
    li.pop(first)

    # 递归思想 - 对左边的列表进行排序
    quick_sort(li, first, left_cur - 1)

    # 递归思想 - 对右边的列表进行排序
    quick_sort(li, left_cur + 1, last)


if __name__ == '__main__':
    li = [3, 8, 5, 15, 9, 20, 45, 6, 25, 34, 13, 62, 1, 19, 7, 10]
    start = time.time()
    quick_sort(li, 0, 15)
    print(li)
    end = time.time()
    print(end - start)
