import math

def convert_angle():
    print("1. Degree to Radian")
    print("2. Radian to Degree")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        degree = float(input("Enter angle in degrees: "))
        radian = math.radians(degree)
        print(f"{degree}° = {radian:.2f} radians")
    elif choice == 2:
        radian = float(input("Enter angle in radians: "))
        degree = math.degrees(radian)
        print(f"{radian:.2f} radians = {degree}°")
    else:
        print("Invalid choice!")

convert_angle()
