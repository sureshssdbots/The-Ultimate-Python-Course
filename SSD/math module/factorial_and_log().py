import math

def factorial_and_log():
    num = int(input("Enter a number to find factorial: "))
    if num >= 0:
        print(f"Factorial of {num} is {math.factorial(num)}")
    else:
        print("Factorial is not defined for negative numbers!")

    base = float(input("Enter the base for logarithm: "))
    value = float(input("Enter the number for logarithm: "))
    if value > 0:
        print(f"log({value}, base={base}) = {math.log(value, base):.2f}")
    else:
        print("Logarithm is not defined for zero or negative numbers!")

factorial_and_log()
