a = "Suresh"


ashort = a[0:3] # start from index 0 all the way till 3 (excluding 3)
print(ashort)
character1 = a[1]
print(character1)



print(a[:])  # पूरी स्ट्रिंग प्रिंट होगी

print(a[:3])  # शुरुआत से तीसरे इंडेक्स (3 एक्सक्लूडेड) तक

print(a[2:])  # दूसरे इंडेक्स से अंत तक


print(a[-3:])  # अंत के  तीसरे अक्षर से लेकर अंत तक.    output esh


print(a[:-2])  # अंत से दो अक्षर छोड़कर बाकी सब.    output sure


name = 'Bhawana'
print(name[0:8:2])  # 0 से 8 तक, हर दूसरे अक्षर को लें
# Output: "Baaa"

print(name[::2])  # पूरी स्ट्रिंग से हर दूसरे अक्षर को लें
# Output: "Baaa"

print(name[::-1])  # स्ट्रिंग को रिवर्स कर देता है
# Output: "anawabB"

print(name.upper())  # सभी अक्षर बड़े अक्षरों में
# Output: "BHAWANA"

print(name.lower())  # सभी अक्षर छोटे अक्षरों में
# Output: "bhawana"

print(name.capitalize())  # पहला अक्षर बड़ा होगा
# Output: "Bhawana"

print(len(name))  # स्ट्रिंग की कुल लंबाई
# Output: 7
print(len(a))#output 6 


print(name.count('a'))  # अक्षर 'r' कितनी बार है?
# Output: 3

print(a.count('s')) # output 1




print(name.find('n'))  # 'n' का पहला स्थान
# Output: 5

print(name.find('u'))  # अगर 'u' नहीं है तो -1 लौटाएगा
# Output: -1


print(name.replace('w', 'v'))  # 'w' को 'v' से बदल दें
# Output: "Bhavana"

print(name.startswith('H'))  # 'Bhawana' H से शुरू होता है?
# Output: False 

print(name.endswith('a')) #Bhawana  a se end hoti hai output ; True 


 
  c = "Suresh Bhawana "
parts = c.split()  # स्पेस के आधार पर विभाजित करें
print(parts)
# Output: ['Suresh', 'Bhawana']






