# Try-except block for handling division by zero and invalid input
try:
    # Taking an integer input from the user
    num = int(input("Enter a number: "))
    print("The number is:", num)

    # Performing division by the entered number
    result = 10 / num
    print('Result is', result)

# Handling ZeroDivisionError if the user enters zero
except ZeroDivisionError:
    print('Can not divide by zero')

# Handling ValueError in case of invalid input (non-integer input)
except ValueError:
    print('Please enter a valid number')

# Uncomment the next line if you want this block to run
#finally:
#    print('This is always executed')

# Example of custom error handling using raise
# Uncomment and test the age validation
# age = int(input("Enter your age: "))
# if age < 0:
#     raise ValueError("Age cannot be negative.")
# print("Your age is:", age)


# Nested try-except example with multiple exception handling
try:
    # Taking two integer inputs from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Trying to divide the numbers
    try:
        result = num1 / num2
        print("Result:", result)

    # Handling ZeroDivisionError inside the nested try block
    except ZeroDivisionError:
        print("Cannot divide by zero.")

# Handling ValueError in case of invalid input (non-integer input)
except ValueError:
    print("Please enter valid integers.")


# Using try-except with else block to check for successful execution
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("The division was successful. Result:", result)


# Try-except-finally block example, where 'finally' executes regardless of success/failure
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("The division was successful. Result:", result)
finally:
    print("This will always execute.")  # This will execute regardless of whether there was an error or not
