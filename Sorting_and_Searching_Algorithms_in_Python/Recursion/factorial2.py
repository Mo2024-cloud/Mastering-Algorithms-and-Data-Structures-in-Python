"""
Here We Have A problem and we Try To brack this problem into a Small Pieces
1 - Frist Function Return The Factorial For every Number Passes to it
  - And Handle (The Negative Number)
2 - Second Function Get array of Numbers and Send Every Number to the frist Function
    and Return The Factorial For Every Number
"""

def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num < 0:
        return 'Error'
    else:
        return num * factorial(num - 1)


def factorials(nums):
    results = []
    for num in nums:
        f = factorial(num)
        if f is not None:
            results.append(f)
    return results


print(factorials([2, 3, 4]))  # Should print: [2, 6, 24]
print(factorials([1, 5, 6]))  # Should print: [1, 120, 720]
print(factorials([0, -3, 10]))  # Should print: [1, 'Error', 3628800]

# print(factorial(-3))