def largest_in_tuple(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

numbers_tuple = (10, 20, 30, 40, 50)
print(largest_in_tuple(numbers_tuple))  # Output: 50
