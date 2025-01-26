n = int(input("Enter the number: "))

if n < 0:
    print('Please Enter positive number')
elif n ==0:
    print('The factorial of 0 is 1')

else:
    product= 1
    for i in range(1, n+1):
        product = product* i
        
print(f"The factorial of {n} is {product}")
