import random as ran

def encrypt(msg):
    text = msg.upper()
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertxt = ''
    for letter in text:
        key = ran.randint(-26,26)
        if key == 0:
            key += ran.randint(0,26)
        if letter in alpha:
            letind = (alpha.find(letter) + key) % len(alpha)
            ciphertxt += alpha[letind]
        else:
            ciphertxt += letter
    return ciphertxt

msg = input("Message = ")
print(encrypt(msg))