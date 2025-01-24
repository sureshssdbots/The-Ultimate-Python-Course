
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






#This is for sefty parpach 
#from string import Template

#name = "Suresh"
#date = "24 September 2050"
#letter_template = Template('''Dear $name,
#You are selected!
#$date''')

#print(letter_template.substitute(name=name, date=date))
