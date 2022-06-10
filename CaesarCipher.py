def encrypt (key, text):
    text = text.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = ""
    for letter in text:
        if letter in alpha:
            letterind = (alpha.find(letter) + key) % len(alpha)

            cipher = cipher + alpha[letterind]
        else:
            cipher = cipher + letter
    return cipher

def decrypt(key,ciphertext):
    ciphertext = ciphertext.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = ""
    for letter in ciphertext:
        if letter in alpha:
            letterind = (alpha.find(letter) - key) % len(alpha)
            message = message + alpha[letterind]
        else:
            message = message + letter
    return message

def main():
    word = input("Message = ")
    key = int(input("Key = "))

    encrypted = encrypt(key,word)
    print(encrypted)

    decrypted = decrypt(key,encrypted)
    print(decrypted)

if __name__ == "__main__":
    main()