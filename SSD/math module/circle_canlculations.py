import math

def circle_calculations():
    radius = float(input("Enter the radius of the circle: "))
    circumference = 2 * math.pi * radius
    area = math.pi * math.pow(radius, 2)

    print(f"Circumference of the circle: {circumference:.2f}")
    print(f"Area of the circle: {area:.2f}")

circle_calculations()
