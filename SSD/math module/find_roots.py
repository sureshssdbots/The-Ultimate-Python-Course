import math

def solve_quadratic():
    print("For a quadratic equation ax^2 + bx + c = 0")
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))

    discriminant = math.pow(b, 2) - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"The roots are {root1:.2f} and {root2:.2f}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"The root is {root:.2f}")
    else:
        print("No real roots exist.")

solve_quadratic()
