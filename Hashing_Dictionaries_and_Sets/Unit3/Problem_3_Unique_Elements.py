"""
The third problem compels us to find elements unique to each of the two given lists,
i.e. given two lists, list1 and list2,
we need to find elements that exist only in list1 and elements that exist only in list2, respectively.

Such a task might be beneficial if you possess two lists of employees
from different company departments and you wish to identify the employees unique to each department.
"""


def exclusive_products(inventory1, inventory2):
    set1 = set([string.upper() for string in inventory1])
    set2 = set([string.upper() for string in inventory2])
    Space_Threads = list(set1 - set2)
    Galaxy_Garments = list(set2 - set1)
    return Space_Threads, Galaxy_Garments


inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
print(exclusive_products(inventory1, inventory2))
# Expected output: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

inventory1 = ["T-Shirt", "hoodie", "Backpack"]
inventory2 = ["Backpack", "Hoodie", "t-shirt"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], [])

inventory1 = []
inventory2 = ["Dress", "Skirt", "Coat"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], ['COAT', 'DRESS', 'SKIRT'])
