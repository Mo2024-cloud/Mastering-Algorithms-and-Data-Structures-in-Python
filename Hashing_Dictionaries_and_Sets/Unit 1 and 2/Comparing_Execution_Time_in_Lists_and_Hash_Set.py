import time

def excution_function():
    hash_set = set()
    list = []

    items_in_database = 10**6

    for i in range(items_in_database):
        hash_set.add(i)
        list.append(i)

    test_element = items_in_database + 1

    compile_time = time.time()
    # Searching 100 Times in hash_set in Vertual DataBase
    for i in range(100):
        if test_element in hash_set:
            True
        else:
            False
    print(f"The time For Searching in hash_set is {time.time() - compile_time}")

    compile_time = time.time()
    # Searching 100 Times in list in Vertual DataBase
    for i in range(100):
        if test_element in list:
            True
        else:
            False
    print(f"The time For Searching in list is {time.time() - compile_time}")

excution_function()