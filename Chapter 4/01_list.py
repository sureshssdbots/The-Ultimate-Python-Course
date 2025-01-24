# friends नामक लिस्ट बनाई जा रही है जिसमें विभिन्न प्रकार के डेटा हैं
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

# लिस्ट के पहले तत्व को प्रिंट कर रहे हैं (यह "Apple" होगा)
print(friends[0])

# लिस्ट के पहले तत्व को बदल रहे हैं, अब यह "Grapes" हो जाएगा
friends[0] = "Grapes"  # Unlike Strings, lists are mutable

# लिस्ट के पहले तत्व को फिर से प्रिंट कर रहे हैं (अब यह "Grapes" होगा)
print(friends[0])

# लिस्ट के 1 से 3 तक के तत्वों को प्रिंट कर रहे हैं (यह "Orange", 5, 345.06 होगा)
print(friends[1:4])
