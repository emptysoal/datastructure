"""
    若n1+n2+n3=1000,且n1^2+n2^2=n3^2(n1,n2,n3为自然数),求出所有n1、n2、n3可能的组合
"""
import time


def fun():
    re_list = []
    for i in range(0, 1001):
        for j in range(0, 1001):
            for k in range(0, 1001):
                if i + j + k == 1000 and i ** 2 + j ** 2 == k ** 2:
                    re_list.append((i, j, k))
    return re_list


if __name__ == '__main__':
    start_time = time.time()
    re = fun()
    end_time = time.time()
    print('执行时间：', end_time - start_time)
    print('组合：', re)
