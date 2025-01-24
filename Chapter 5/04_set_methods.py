s = {1, 5, 32, 54,5, 5, 5, "suresh"}

print(s, type(s))

s.add(77)
print(s)


s.remove(1)
print(s)


A = {1, 2, 3}
B = {3, 4, 5}


print(A | B)  # Union: {1, 2, 3, 4, 5}
print(A & B)  # Intersection: {3}
print(A - B)  # Difference: {1, 2}
print(A ^ B)  # Symmetric Difference: {1, 2, 4, 5}

