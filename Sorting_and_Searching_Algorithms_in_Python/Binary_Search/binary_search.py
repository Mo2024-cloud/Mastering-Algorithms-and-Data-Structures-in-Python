def binary_search(data,target):
    low = 0
    high = len(data)

    while high - low > 1:
        mid = (high + low) // 2
        if target < data[mid]:
            high = mid
        else:
            low = mid
    return low if target == data[low] else None

print(binary_search([1,2,3,4,5],1))