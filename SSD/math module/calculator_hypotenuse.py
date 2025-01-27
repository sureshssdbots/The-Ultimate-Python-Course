import math

def calculate_hypotenuse():
    side1 = float(input("Enter the first side of the triangle: "))
    side2 = float(input("Enter the second side of the triangle: "))

    hypotenuse = math.sqrt(math.pow(side1, 2) + math.pow(side2, 2))
    print(f"The hypotenuse of the triangle is {hypotenuse:.2f}")

calculate_hypotenuse()
