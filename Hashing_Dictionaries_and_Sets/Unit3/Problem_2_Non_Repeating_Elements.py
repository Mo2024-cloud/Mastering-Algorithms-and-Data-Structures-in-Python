"""
Our next issue is slightly more complex. 
We must determine all elements in a given list that appear only once,
meaning they don't have any duplicates in the same list.

Or all elements that Repeted
"""


def repeating_elements(nums):
    seen, repeted = set(), set()
    for num in nums:
        if num in seen:
            repeted.add(num)
        else:
            seen.add(num)
    return list(repeted)


print(repeating_elements([9, 8, 7, 8, 7, 6, 5]))  # expected output : [8, 7]
print(repeating_elements([-1, 2, 3, -1, 2, 3]))  # expected output : [-1, 2, 3]
print(repeating_elements([1, 2, 3, 4, 5]))  # expected output : []
