# Create a set with unique elements. Duplicate values like 5 will only be stored once.
s = {1, 5, 32, 54, 5, 5, 5, "suresh"}
print(s, type(s))  # Output: {1, 32, 5, 54, 'suresh'} <class 'set'>

# Add a new element to the set
s.add(77)  # Adds 77 to the set
print(s)  # Output: {1, 32, 5, 54, 'suresh', 77}

# Remove an element from the set
s.remove(1)  # Removes 1 from the set. If the element is not found, it raises a KeyError.
# Example: s.remove(9) would throw an error since 9 is not in the set.
print(s)  # Output: {32, 5, 54, 'suresh', 77}

# Discard an element from the set (no error if the element is not found)
s.discard(32)  # Removes 32 from the set
print(s)  # Output: {5, 54, 'suresh', 77}

s.discard(9)  # No error even if 9 is not present in the set

# Remove a random element from the set using pop()
print(s.pop())  # Removes and returns a random element from the set
print(s)  # Remaining set after a random element is removed

# Clear the entire set
s.clear()  # Removes all elements from the set
print(s)  # Output: set() (an empty set)

# ________________________________

# Create two sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Copy the set
s1_copy = s1.copy()  # Creates a shallow copy of s1
print(s1_copy)  # Output: {1, 2, 3}

# Union: Combine all elements from both sets
print(s1.union(s2))  # Output: {1, 2, 3, 4, 5}
print(s1 | s2)  # Output: {1, 2, 3, 4, 5} (alternate syntax)

# Intersection: Find common elements between both sets
print(s1.intersection(s2))  # Output: {3}
print(s1 & s2)  # Output: {3} (alternate syntax)

# Difference: Find elements in s1 but not in s2
print(s1.difference(s2))  # Output: {1, 2}
print(s1 - s2)  # Output: {1, 2} (alternate syntax)

# Symmetric Difference: Elements in either set, but not both
print(s1.symmetric_difference(s2))  # Output: {1, 2, 4, 5}
print(s1 ^ s2)  # Output: {1, 2, 4, 5} (alternate syntax)

# Update s1 with the union of s1 and s2
s1.update(s2)  # Adds elements of s2 to s1
print(s1)  # Output: {1, 2, 3, 4, 5}

# ________________________________

# Create two new sets for further operations
s3 = {1, 2, 3, 4, 5}
s4 = {3, 4, 5, 6, 7}

# Intersection Update: Keep only elements also found in s4
s3.intersection_update(s4)
print("After intersection_update:", s3)  # Output: {3, 4, 5}

# Reset s3
s3 = {1, 2, 3, 4, 5}

# Difference Update: Remove elements found in s4
s3.difference_update(s4)
print("After difference_update:", s3)  # Output: {1, 2}

# Check if two sets are disjoint (no common elements)
print(s3.isdisjoint(s4))  # Output: True (no common elements after difference update)

# Check if one set is a superset of another
print(s3.issuperset(s4))  # Output: False (s3 does not contain all elements of s4)

