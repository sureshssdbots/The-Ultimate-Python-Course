'''
For n = 3
  *
 ***
*****

For n = 5
    *
   ***
  *****
 ********
**********

'''

n = int(input("Enter the number: "))

for i in range(1, n+1):
    print(" " * (n - i), end="")  # Spaces before stars
    print("*" * (2 * i - 1), end="")  # Stars for the current row
    print("")  # Move to the next line
   

