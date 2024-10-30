def print_even_keys(d):
    for key, value in d.items():
        if value % 2 == 0:
            print(key)

example_dict = {'a': 2, 'b': 3, 'c': 4}
print_even_keys(example_dict)  # Output: 'a', 'c'
