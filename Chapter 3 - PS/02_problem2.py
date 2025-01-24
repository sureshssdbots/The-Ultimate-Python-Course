
# place holder use 
letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

# जब आपको यह संदेश किसी को भेजना हो, तो आप नाम और तारीख को बदल सकते हैं।
print(letter.replace("<|Name|>", "Suresh").replace("<|Date|>", "24 September 2050"))



# f'' string use 
name = "Suresh"
date = "24 September 2050"
letter = f'''Dear {name}, 
You are selected! 
{date}'''

print(letter)



letter = '''Dear {name}, 
You are selected! 
{date}'''

print(letter.format(name="Suresh", date="24 September 2050"))



letter = "Hello, {user_name}! Welcome to {place}."

# कस्टम प्लेसहोल्डर्स को बदलें
letter = letter.format(user_name="Suresh", place="Python World")

print(letter)


#This is for sefty parpach 
#from string import Template

#name = "Suresh"
#date = "24 September 2050"
#letter_template = Template('''Dear $name,
#You are selected!
#$date''')

#print(letter_template.substitute(name=name, date=date))
