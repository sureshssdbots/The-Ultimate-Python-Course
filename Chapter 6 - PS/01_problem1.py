a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))
a4 = int(input("Enter number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1:", a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2:", a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3:", a3)

elif(a4>a1 and a4>a2 and a4>a3):
    print("Greatest number is a4:", a4)
    
  

# Using max() function to find the greatest number
greatest = max(a1, a2, a3, a4)
print("The greatest number is:", greatest)

#min() is use for find the smallest number 
smallest = min(a1, a2, a3, a4)
print("The smallest number is:", smallest)


# using sum() function to find all number sum
total = sum([a1,a2,a3,a4])
print('The sum of all number is', total)


sorted_number =sorted([a1,a2,a3,a4])
print('acsending oder', sorted_number)

numbers = [a1,a2,a3,a4]
numbers.reverse()
print('Reverse oder', numbers)
