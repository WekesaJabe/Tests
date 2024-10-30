def tuples_to_dict(tuples_list):
    result = {}
    for key, value in tuples_list:
        result[key] = value
    return result

tuples_list = [("apple", 5), ("banana", 3), ("cherry", 7)]
print(tuples_to_dict(tuples_list))  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}

