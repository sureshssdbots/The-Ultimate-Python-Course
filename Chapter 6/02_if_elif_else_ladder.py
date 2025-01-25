try:
    a = int(input("Enter your age: "))  # यूज़र से उम्र इनपुट लें और उसे integer में कन्वर्ट करें

    if a >= 18:  # अगर उम्र 18 या उससे अधिक है
        print("You are eligible for voting.")  # वोटिंग के लिए योग्य
    else:  # अगर उम्र 18 से कम है
        print("You are not eligible for voting. Wait", 18 - a, "year(s).")  # वोटिंग के लिए इंतजार

except ValueError:  # अगर यूज़र ने गलत डेटा इनपुट किया (जैसे अक्षर)
    print("Please enter a valid number for age.")  # एरर मैसेज प्रिंट करें)

