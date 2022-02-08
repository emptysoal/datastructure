lis = [
    [1, 3, 4, 5, 8],
    [2, 6, 7, 9, 12],
    [7, 10, 14, 15, 18],
    [11, 13, 16, 19, 21]
]


# lis = [
#     [7, 10],
#     [11, 13]
# ]


def find_num(num, lis, c=0, r=0):
    if num == lis[c][r]:
        return True
    elif num > lis[c][r]:
        r += 1
        if r < len(lis[0]):
            return find_num(num, lis, c, r)
        return False
    elif num < lis[c][r]:
        c -= 1
        if c >= 0:
            return find_num(num, lis, c, r)
        return False


def search_num(num, lis):
    c = len(lis) - 1
    return find_num(num, lis, c, 0)


for i in range(25):
    print(i, search_num(i, lis))
