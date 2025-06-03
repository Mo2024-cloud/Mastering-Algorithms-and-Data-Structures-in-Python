def rec(num):
    print(num)
    if num <= 0:
        return
    else:
        rec(num - 1)

rec(5)