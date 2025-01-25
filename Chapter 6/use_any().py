# Example 1
my_list = [False, False, True]
print(any(my_list))  # Output: True (Because one element is True)

# Example 2
my_list = [False, False, False]
print(any(my_list))  # Output: False (Because no element is True)

# Example 3
my_list = [1, 0, 3]
print(any(my_list))  # Output: True (Because 1 is treated as True)

# Example 4
my_list = [0, 0, 0]
print(any(my_list))  # Output: False (Because all elements are False)



input_list = [False, False, True]
if any(input_list):
    print("At least one condition is met")
else:
    print("None of the conditions are met")
