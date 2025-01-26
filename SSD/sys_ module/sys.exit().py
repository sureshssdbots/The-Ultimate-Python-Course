import sys  # sys module को import करते हैं जिससे sys.exit() function का उपयोग हो सके।

while True:  # यह एक infinite loop है, जो तब तक चलेगा जब तक explicitly break या exit न किया जाए।
    print('exit to exit')  # User को निर्देश देता है कि 'exit' टाइप करके प्रोग्राम को बंद कर सकता है।
    response = input()  # User से input लेता है और उसे response नाम के variable में स्टोर करता है।
    
    if response == 'exit':  # अगर user का response 'exit' है:
        sys.exit()  # तो program को terminate कर दिया जाएगा।
    
    print('you typed', response)  # अगर 'exit' नहीं है, तो user द्वारा टाइप किया गया text प्रिंट करता है।
