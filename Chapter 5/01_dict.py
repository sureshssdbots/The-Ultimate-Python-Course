# Creating an empty dictionary
d = {}  # Empty dictionary
print(type(d))  # Prints: <class 'dict'>

# Creating a dictionary with some data
marks = {
    "Suresh": 100,
    "Shubham": 56,
    "Sohan": 23
}

# Accessing elements
print(marks["Suresh"])  # Access value for key "Suresh"

# Safely accessing elements using get() (avoids KeyError)
print(marks.get("Harry", "Key not found"))  # Outputs: Key not found

# Adding a new key-value pair
marks["Harry"] = 78  # Adds 'Harry' with value 78
print(marks)  # Prints updated dictionary

# Updating an existing key's value
marks["Suresh"] = 95  # Updates value for key 'Suresh'
print(marks)  # Prints updated dictionary

# Removing an element using pop()
removed_value = marks.pop("Sohan")  # Removes 'Sohan' and returns its value
print(f"Removed value: {removed_value}")  # Outputs: 23
print(marks)  # Updated dictionary after removal

# Removing the last inserted item using popitem()
last_removed = marks.popitem()  # Removes the last inserted key-value pair
print(f"Last removed item: {last_removed}")  # Outputs: ('Harry', 78)
print(marks)  # Updated dictionary

# Adding multiple key-value pairs using update()
marks.update({"Amit": 88, "Raj": 65})  # Adds new key-value pairs
print(marks)  # Prints updated dictionary

# Clearing the dictionary (removes all elements)
marks.clear()
print(marks)  # Outputs: {}

# Recreating dictionary for further operations
marks = {
    "Suresh": 100,
    "Shubham": 56,
    "Sohan": 23
}

# Checking if a key exists using 'in' operator
if "Suresh" in marks:
    print("Suresh is in the dictionary")

# Iterating through keys
print("Keys in the dictionary:")
for key in marks.keys():
    print(key)  # Prints each key

# Iterating through values
print("Values in the dictionary:")
for value in marks.values():
    print(value)  # Prints each value

# Iterating through key-value pairs
print("Key-Value pairs in the dictionary:")
for key, value in marks.items():
    print(f"{key}: {value}")  # Prints each key-value pair

# Copying the dictionary
new_marks = marks.copy()  # Creates a copy of the dictionary
print("Copied dictionary:", new_marks)

# Getting the length of the dictionary
print("Length of dictionary:", len(marks))  # Outputs: 3 (number of key-value pairs)

# Deleting a key-value pair using del
del marks["Shubham"]  # Deletes the key 'Shubham'
print(marks)  # Updated dictionary

# Nested dictionary example
nested_dict = {
    "Class1": {"Student1": "Suresh", "Student2": "Amit"},
    "Class2": {"Student1": "Raj", "Student2": "Shubham"}
}
print(nested_dict)  # Prints the nested dictionary
print(nested_dict["Class1"]["Student1"])  # Accessing nested dictionary value



