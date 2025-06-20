# Implementation of Binary Search on a specific use case

# List of sorted ages in a social media platform
ages = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

def binary_search_iterative(data, target):
    low = 0
    high = len(data)
    while high - low > 1:
        mid = (low + high) // 2
        if target < data[mid]:
            high = mid 
        elif target > data[mid]:
            low = mid 
        else:  # if target is equal to data[mid]
            return mid
    return low if data[low] == target else None

# Let's say we want to find out what position a 30-year-old holds in our sorted list of ages
age_query = 30
result = binary_search_iterative(ages, age_query)

if result is not None:
    print(f"Age of {age_query} is found at position {result} in the age list.")
else:
    print(f"No profile is found with age {age_query}.")