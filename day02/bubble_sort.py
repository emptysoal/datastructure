"""
    冒泡排序
"""
import time


def bubble_sort(li):
    for j in range(len(li) - 1):
        for i in range(len(li) - 1 - j):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
    return li


if __name__ == '__main__':
    l = [3, 8, 5, 15, 9, 20, 45, 6, 25, 34, 13, 62, 1, 19, 7, 10]
    start = time.time()
    res = bubble_sort(l)
    print(res)
    end = time.time()
    print(end - start)
