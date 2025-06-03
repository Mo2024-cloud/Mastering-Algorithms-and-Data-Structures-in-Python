def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)  # 5  4  3   2  1 

print(factorial(5))