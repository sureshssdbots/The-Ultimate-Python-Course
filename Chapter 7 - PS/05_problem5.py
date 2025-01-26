n = int(input("Enter the number: "))

if n <= 0:
    print("Please enter a positive integer greater than 0.")
else:
    i = 1
    total_sum = 0

    while i <= n:
        total_sum += i  # Add i to total_sum
        i += 1  # Increment i by 1
    
    print(f"The sum of first {n} natural numbers is: {total_sum}")
