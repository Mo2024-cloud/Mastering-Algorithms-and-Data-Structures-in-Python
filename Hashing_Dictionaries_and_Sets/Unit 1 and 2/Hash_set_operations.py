def hash_set_operations():
    import time

    hash_set = set()
    list = []

    data = 10**7

    for i in range(data):
        hash_set.add(i)
        list.append(i)

    test_element = data + 1

# Time for Search for the test_element in hash_set
    start_time = time.time()
    print(f"is {test_element} in Hash Set? {test_element in hash_set}")
    print(f"The time that Hash set is {time.time() - start_time}")

# Time for Search for the test_element in list
    start_time = time.time()
    print(f"is {test_element} in Hash Set? {test_element in list}")
    print(f"The time that List is {time.time() - start_time}")


hash_set_operations()
