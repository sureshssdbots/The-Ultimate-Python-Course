# first method 

d = {}
name = input('Enter your name, ')
age = int(input('Enter your age, '))
d.update({name : age })

name = input('Enter your name, ')
age = int(input('Enter your age, '))
d.update({name : age })

name = input('Enter your name, ')
age = int(input('Enter your age, '))
d.update({name : age })


name = input('Enter your name, ')
age = int(input('Enter your age, '))
d.update({name : age })


print(d)

# second method 
d = {}
for I in range(4):
    name = input('Enter your name, ')
    age = int(input('Enter your age, '))
    d.update({name : age })
    
    
print(d)



#third method 

a = {}  # Empty dictionary

while True:
    name = input('Enter your name: ')  # User से नाम इनपुट लें
    age = int(input('Enter your age: '))  # User से उम्र इनपुट लें
    a.update({name: age})  # डिक्शनरी को अपडेट करें

    # User से पूछें कि वह और डेटा जोड़ना चाहता है या नहीं
    choice = input('Do you want to add another entry? (yes/no): ').lower()
    
    if choice == 'no':  # अगर उपयोगकर्ता 'no' टाइप करता है, तो लूप खत्म करें
        break

print('Final dictionary:', a)  # पूरी डिक्शनरी प्रिंट करें

