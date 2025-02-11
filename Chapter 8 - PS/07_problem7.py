def rem(l, word):
    n = []  # एक नई खाली सूची बनाएंगे (यह वह सूची होगी जिसमें से शब्द हटा दिया गया है)
    for item in l:  # सूची `l` में से हर आइटम को एक-एक करके लेंगे
        if item != word:  # अगर वर्तमान आइटम `word` के बराबर नहीं है
            n.append(item)  # तो उसे नई सूची `n` में जोड़ देंगे
    return n  # नई सूची `n` को वापस करेंगे

l = ["Harry", "Rohan", "Shubham", "an"]  # यह वह मूल सूची है
print(rem(l, "an"))  # "an" को सूची से हटाने के लिए `rem()` फंक्शन को कॉल करते हैं
