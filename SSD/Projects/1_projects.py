import sys
import os
import random

def system_info():
    # सिस्टम की जानकारी दिखाने वाला फंक्शन
    print(" System Information:")
    print(f"Python Version: {sys.version}")
    print(f"Operating System: {sys.platform}")
    print(f"Available Paths: {sys.path}")

def user_input():
    # यूजर से इनपुट लेकर उसका प्रोसेस करने वाला फंक्शन
    name = input("Enter your name: ").capitalize()
    age = int(input("Enter your age: "))
    
    # Age के आधार पर message print करना
    if age < 18:
        print(f"Sorry {name}, you are not eligible.")
    else:
        print(f"Welcome {name}, you are eligible!")

def generate_random_numbers():
    # रैंडम नंबर्स जेनरेट करने वाला फंक्शन
    print("Random Numbers (between 1 and 100):")
    for i in range(5):
        print(random.randint(1, 100))

def file_operations():
    print("\n--- File Operations Menu ---")
    print("1. Write data to file")
    print("2. Read data from file")
    print("3. Exit")
    
    filename = input("\nEnter the filename to perform operations: ")

    while True:
        try:
            choice = int(input("Choose an option (1/2/3): "))
            
            if choice == 1:
                # Write data to the file
                data = input("Enter the data you want to write to the file: ")
                with open(filename, "w") as f:
                    f.write(data)
                print(f"Data successfully written to {filename}")
            
            elif choice == 2:
                # Read data from the file
                try:
                    with open(filename, "r") as f:
                        print(f"Data in {filename}:")
                        print(f.read())
                except FileNotFoundError:
                    print("Error: File does not exist! Please write data first.")
            
            elif choice == 3:
                print("Exiting the program. Have a great day!")
                break
            
            else:
                print("Invalid choice! Please choose between 1, 2, or 3.")
        
        except ValueError:
            print("Error: Please enter a valid number!")
            

def main():
    # प्रोग्राम का मुख्य कार्य
    print("Welcome to the Python Practice Tool!")
    while True:
        print(" Choose an option:")
        print("1. Display System Information")
        print("2. User Input and Age Check")
        print("3. Generate Random Numbers")
        print("4. File Operations")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            system_info()
        elif choice == "2":
            user_input()
        elif choice == "3":
            generate_random_numbers()
        elif choice == "4":
            file_operations()
        elif choice == "5":
            print("Exiting the program.")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
