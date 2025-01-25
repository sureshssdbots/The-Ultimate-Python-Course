age = int(input('Enter your age: '))  # यूज़र से उम्र इनपुट लें

if age >= 18:  # अगर उम्र 18 या उससे अधिक है
    print('You are eligible to vote.')  # वोटिंग के लिए योग्य
else:
    print('You are not eligible to vote. Wait', 18 - age, 'years.')  # वोटिंग के लिए कितने साल इंतजार करना होगा
