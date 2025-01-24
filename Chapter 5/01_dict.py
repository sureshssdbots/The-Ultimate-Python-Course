d = {}  # Empty dictionary
print(type(d))  # Prints: <class 'dict'>

# Dictionary with initial data
marks = {
    "Suresh": 100,
    "Shubham": 56,
    "Sohan": 23
}

# Accessing a value using a key
print(marks["Suresh"])  # Output: 100

# Using get() method to safely access a value
print(marks.get("Suresh", 'Key not found'))  # Output: 100

# Adding a new key-value pair to the dictionary
marks['Bhawana'] = 99
print(marks)  # Output: {'Suresh': 100, 'Shubham': 56, 'Sohan': 23, 'Bhawana': 99}

# Adding another key-value pair
marks['Dilip'] = 98
print(marks)  # Output: {'Suresh': 100, 'Shubham': 56, 'Sohan': 23, 'Bhawana': 99, 'Dilip': 98}

# Accessing the newly added key
print(marks['Dilip'])  # Output: 98

# Deleting a key-value pair using del
del marks['Shubham']
print(marks)  # Output: {'Suresh': 100, 'Sohan': 23, 'Bhawana': 99, 'Dilip': 98}

# Removing a key-value pair using pop() and storing the removed value
removed = marks.pop('Sohan')
print('removed value is', removed)  # Output: removed value is 23
print(marks)  # Output: {'Suresh': 100, 'Bhawana': 99, 'Dilip': 98}

# Removing the last inserted key-value pair using popitem()
last_removed = marks.popitem()
print('the last value is', last_removed)  # Output: the last value is ('Dilip', 98)
print(marks)  # Output: {'Suresh': 100, 'Bhawana': 99}

# Adding multiple key-value pairs using update()
marks.update({'Rawi': 88, 'Abhijeet': 85})
print(marks)  # Output: {'Suresh': 100, 'Bhawana': 99, 'Rawi': 88, 'Abhijeet': 85}

# Checking if a key exists in the dictionary
if "Suresh" in marks:
    print("Suresh is in the dictionary")  # Output: Suresh is in the dictionary
else:
    print('This key is not in dictionary')

# Iterating through all the keys in the dictionary
print('Keys in the dictionary:')
for key in marks.keys():  
    print(key)  # Prints each key

# Iterating through all the values in the dictionary
print("Values in the dictionary:")
for value in marks.values():  
    print(value)  # Prints each value

# Iterating through all key-value pairs in the dictionary
print("Key-Value pairs in the dictionary:")
for key, value in marks.items():
    print(f"{key}: {value}")  # Prints key-value pairs

# Copying the dictionary to a new dictionary
new_marks = marks.copy()
print(new_marks)  # Output: {'Suresh': 100, 'Bhawana': 99, 'Rawi': 88, 'Abhijeet': 85}

# Getting the length of the dictionary
print('Length of dictionary', len(marks))  # Output: Length of dictionary 4

# Creating and printing a nested dictionary
nested_dict = {
    "Class1": {"Student1": "Suresh", "Student2": "Amit"},
    "Class2": {"Student1": "Raj", "Student2": "Shubham"}
}
print(nested_dict)  # Prints the entire nested dictionary

# Accessing a value from the nested dictionary
print(nested_dict["Class1"]["Student1"])  # Output: Suresh

# Clearing all items from the dictionary
marks.clear()
print(marks)  # Output: {}



