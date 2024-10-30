def has_pair_with_sum(lst, target_sum):
    seen = set()
    for num in lst:
        if target_sum - num in seen:
            return True
        seen.add(num)
    return False

example_list = [1, 2, 3, 4, 5]
target_sum = 9
print(has_pair_with_sum(example_list, target_sum))  # Output: True (4 + 5)
