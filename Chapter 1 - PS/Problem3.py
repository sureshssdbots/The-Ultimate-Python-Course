import pyttsx3          # Text-to-Speech लाइब्रेरी इंपोर्ट की
engine = pyttsx3.init() # pyttsx3 का एक इंजन ऑब्जेक्ट बनाया
engine.say("Hey I am good")  # जो टेक्स्ट बोलना है, वह पास किया
engine.runAndWait()     # ऑडियो को प्ले करने के लिए यह कमांड जरूरी है



