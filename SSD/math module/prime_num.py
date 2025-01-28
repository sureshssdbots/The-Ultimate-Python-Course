
def is_prime(num):
    if num < 2:  # 0 और 1 प्राइम नहीं होते
        return False
    for i in range(2, int(num ** 0.5) + 1):  # √num तक चेक करना efficient है
        if num % i == 0:
            return False  # अगर कोई भी संख्या इसे पूरी तरह से divide कर रही है, तो ये प्राइम नहीं है
    return True  # अगर loop पूरा हो गया और कोई भी फैक्टर नहीं मिला, तो ये प्राइम है

n = int(input('Enter the number: '))
print(f"Prime numbers from 1 to {n}:")

for i in range(1, n + 1):
    if is_prime(i):  # अगर `is_prime(i)` True है तो ही print करो
        print(i, end=' ')











