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

