def fun(n):
    if n > 1:
        return n * fun(n - 1)
    else:
        return 1


print(fun(5))
