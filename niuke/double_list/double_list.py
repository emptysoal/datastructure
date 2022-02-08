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
    if num == lis[0][0]:
        return True
    if c == 0:
        c = len(lis) - 1
    if num == lis[c][r]:
        return True
    elif num > lis[c][r]:
        r += 1
        if r < len(lis[0]):
            return find_num(num, lis, c, r)
        else:
            r -= 1
        c -= 1
        if c > 0:
            return find_num(num, lis, c, r)
        else:
            c += 1
        return False
    elif num < lis[c][r]:
        c -= 1
        if c > 0:
            return find_num(num, lis, c, r)
        else:
            c += 1
        r += 1
        if r < len(lis[0]):
            return find_num(num, lis, c, r)
        else:
            r -= 1
        return False


print(find_num(2, lis))
