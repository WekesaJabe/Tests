def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

example_list = [1, 2, 3, 2, 1, 4, 5]
print(remove_duplicates(example_list))  # Output: [1, 2, 3, 4, 5]
