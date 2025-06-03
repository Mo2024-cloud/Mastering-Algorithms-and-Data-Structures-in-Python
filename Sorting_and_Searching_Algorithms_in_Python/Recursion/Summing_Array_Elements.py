# Problem 2: Summing Array Elements
# Solved Using an auxiliary index

def sumArr(arr, index=0):
    if index == len(arr):
        return 0
    else:
        return arr[index] + sumArr(arr, index + 1)
    
print(sumArr([1,2,3]))