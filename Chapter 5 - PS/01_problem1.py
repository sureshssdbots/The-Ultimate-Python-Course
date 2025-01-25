words = {
    "madad": "Help",
    "kursi": "Chair",
    "billi": "Cat"
}

word = input("Enter the word you want meaning of: ")

# अगर शब्द डिक्शनरी में नहीं है तो 'Not found' प्रिंट होगा
print(words.get(word, "Word not found in the dictionary"))
