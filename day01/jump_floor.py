def jump_floor(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return jump_floor(n - 2) + jump_floor(n - 1)


print(jump_floor(4))
