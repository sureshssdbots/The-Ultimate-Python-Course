l = ["Suresh", "Dilip", "Bhawana", "Rawi"]

name = input("Enter your name: ").lower()  # .lower() को कॉल करना जरूरी है

if name in [i.lower() for i in l]:  # लिस्ट के सभी नामों को lowercase में बदलकर चेक करें
    print("Your name is in the list")
else:
    print("Your name is not in the list")
