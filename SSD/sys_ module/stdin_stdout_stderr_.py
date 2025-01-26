#sys.stdin: इनपुट पढ़ने के लिए।

#sys.stdout: प्रोग्राम का आउटपुट डिस्प्ले करने के लिए।

#sys.stderr: एरर मैसेज को डिस्प्ले करने के लिए।



import sys
sys.stdout.write("Hello, this is stdout!\n")
sys.stderr.write("Hello, this is stderr!\n")



#______________________________________
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    sys.stderr.write("Error: Invalid input! Please enter a valid number.\n")
