


#(i) बैकस्लैश और कोट्स का उपयोग:

string1 = 'It\'s a "beautiful" day!'
print(string1)
# Output: It's a "beautiful" day!




#(ii) नई लाइन (\n) और टैब (\t):

message = "Hello,\n\tWelcome to Python programming!"
print(message)
# Output:
# Hello,
#     Welcome to Python programming!




#(iii) बैकस्पेस (\b):

text = "Hello\bWorld"
print(text)
# Output: HellWorld


#---

#(iv) कैरिज रिटर्न (\r):

text = "Hello\rWorld"
print(text)
# Output: World

#> Explanation: \r लाइन की शुरुआत में जाकर पहले की जगह नई स्ट्रिंग डाल देता है।






#(v) फॉर्म फीड (\f) और वर्टिकल टैब (\v):

text2 = "Hello\fWorld"
print(text2)
# Output:
# Hello
#       World

text3 = "Hello\vWorld"
print(text3)
# Output:
# Hello
# World




#(vi) ऑक्टल और हेक्साडेसिमल वैल्यू का उपयोग:

# ऑक्टल वैल्यू
text4 = '\101\102\103'
print(text4)
# Output: ABC

# हेक्साडेसिमल वैल्यू
text5 = '\x41\x42\x43'
print(text5)
# Output: ABC


#3. रॉ स्ट्रिंग (r'') का उपयोग:

#अगर आप एस्केप सीक्वेंस को इग्नोर करना चाहते हैं और उन्हें जस का तस प्रिंट करना चाहते हैं, तो रॉ स्ट्रिंग का उपयोग करें:

text6 = r'Hello\nWorld\t!'
print(text6)
# Output: Hello\nWorld\t!




#4. मल्टीलाइन स्ट्रिंग (''' या """):

#आप मल्टीलाइन स्ट्रिंग बनाने के लिए ट्रिपल कोट्स का उपयोग कर सकते हैं:

text7 = '''Hello,
This is a
multiline string!'''
print(text7)
# Output:
# Hello,
# This is a
# multiline string!



#(i) प्रोग्राम के नाम और नई लाइन:

program1 = "Python\nProgramming"
print(program1)
# Output:
# Python
# Programming

#(ii) स्ट्रिंग को फॉर्मेट करना:

name = "Suresh"
age = 19
info = f"My name is {name} and I am {age} years old."
print(info)
# Output: My name is Suresh and I am 19 years old.




