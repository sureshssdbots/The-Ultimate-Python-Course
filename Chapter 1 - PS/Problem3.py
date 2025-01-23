import pyttsx3          # Text-to-Speech लाइब्रेरी इंपोर्ट की
engine = pyttsx3.init() # pyttsx3 का एक इंजन ऑब्जेक्ट बनाया
engine.say("Hey I am good")  # जो टेक्स्ट बोलना है, वह पास किया
engine.runAndWait()     # ऑडियो को प्ले करने के लिए यह कमांड जरूरी है


engine.setProperty('rate', 150)  # आवाज़ की गति
engine.setProperty('volume', 0.9)  # आवाज़ का स्तर



#This is 1st speed तेज करने के लिए।
engine = pyttsx3.init()

# Speaking rate (डिफॉल्ट 200 होता है)
rate = engine.getProperty('rate')
print(f"Default Speaking Rate: {rate}")  # चेक करें कि डिफॉल्ट क्या है
engine.setProperty('rate', 150)  # स्पीड कम (धीमे बोलने के लिए)
# engine.setProperty('rate', 250)  # स्पीड तेज

engine.say("Hey, I am speaking slower than usual.")
engine.runAndWait()




#This is 2nd volume बदलने के लिए ।
engine = pyttsx3.init()

# Volume सेट करना (डिफॉल्ट 1.0)
volume = engine.getProperty('volume')
print(f"Default Volume: {volume}")  # चेक करें कि डिफॉल्ट वॉल्यूम कितना है
engine.setProperty('volume', 0.5)  # वॉल्यूम 50% पर सेट

engine.say("This is 50% volume.")
engine.runAndWait()



#This is 3rd voice change code male, female 
engine = pyttsx3.init()

# उपलब्ध आवाज़ें प्राप्त करें
voices = engine.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} ({voice.languages})")

# पुरुष आवाज़
engine.setProperty('voice', voices[0].id)  # Index 0: Male voice
engine.say("This is a male voice.")

# महिला आवाज़
engine.setProperty('voice', voices[1].id)  # Index 1: Female voice
engine.say("This is a female voice.")

engine.runAndWait()






#This is 4th save ऑडियो to file
engine = pyttsx3.init()

engine.save_to_file("Hey, I am saving this text to an audio file.", "output.mp3")
engine.runAndWait()



#all फीचर in one code
#all फीचर in one code
#all फीचर in one code
#all फीचर in one code
#all फीचर in one code
#all फीचर in one code
#all फीचर in one code
import pyttsx3

engine = pyttsx3.init()

# आवाज़ की स्पीड और वॉल्यूम सेट करें
engine.setProperty('rate', 150)  # स्पीड
engine.setProperty('volume', 0.8)  # वॉल्यूम

# आवाज़ बदलें (पुरुष या महिला)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # महिला आवाज़

# टेक्स्ट बोलें
engine.say("Hello, I am a female voice. This is an example of pyttsx3.")
engine.runAndWait()

