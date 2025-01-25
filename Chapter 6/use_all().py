# Example 1
my_list = [True, True, True]
print(all(my_list))  # Output: True (Because all elements are True)

# Example 2
my_list = [True, False, True]
print(all(my_list))  # Output: False (Because one element is False)

# Example 3
my_list = [0, 1, 2, 3]
print(all(my_list))  # Output: False (Because 0 is considered as False)

# Example 4
my_list = [1, 2, 3, 4]
print(all(my_list))  # Output: True (All non-zero numbers are treated as True)


data = [True, True, False]
if all(data):
    print("All validations passed")
else:
    print("Some validations failed")
