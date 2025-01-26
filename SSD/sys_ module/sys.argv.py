import sys
print("Command line arguments are:", sys.argv)   #sys.argv  



print("Script Name:", sys.argv[0])  #sys.argv[0] Script का नाम batata hai

# आर्ग्युमेंट्स की संख्या चेक करें
if len(sys.argv) > 1:
    print("First Argument:", sys.argv[1])  # पहला argument
else:
    print("No First Argument Passed!")

if len(sys.argv) > 2:
    print("Second Argument:", sys.argv[2])  # दूसरा argument
else:
    print("No Second Argument Passed!")
    
    
    


