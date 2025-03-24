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
