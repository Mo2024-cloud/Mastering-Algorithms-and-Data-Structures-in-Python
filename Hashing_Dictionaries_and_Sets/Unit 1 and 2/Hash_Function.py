# We need to Create a Function That Hash Strings and Return Decimal Or Unicode Character
def simple_hash(string):
    summition = sum(ord(ch) for ch in string)
    return summition % 10


print(simple_hash("Hello"))


"""
for ch in string => Will hash the String Passing throW argumment 
H
e
l
l
o

ord(ch) => Will catch every Character then Transform Every Character to Unicode or Decimal code 
H -> 72
e -> 101
l -> 108
l -> 108
o -> 111

sum() => Will Sum all of these => 500

return summition % 10 => 0
"""
