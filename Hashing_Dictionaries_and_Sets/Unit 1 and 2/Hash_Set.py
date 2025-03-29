"""
 A hash set uses (hash functions) to point directly to the location of the interaction
 making operations efficient and timely
"""
# quick retrieval

hash_set = set()

hash_set.add(123)
hash_set.add(456)
hash_set.add(789)

print(123 in hash_set)  # True
print(333 in hash_set)  # False


"""
Essential Characteristics of Hash Set :-

1- Uniqueness of Elements
- Every Elemnt added to the Hash Set is Unique.
- if you Try to add a duplicate element, it didi't give you an error 
but when you tring to print the set that you added a duplicate element
that will give you (One Element Only).

2- Inherent Unordered Property
- the Hash Set don't respect the Order of Element
"""
