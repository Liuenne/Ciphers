def genKey(str, keywrd):
    key = list(keywrd)
    if len(str) == len(keywrd):
        return(keywrd)
    else:
        for i in range(len(str)-len(keywrd)):
            key.append(keywrd[i % len(keywrd)])
    return("".join(key))

def cipherText(str, key):
    cipher_Text=[]
    for i in range(len(str)):
        x = (ord(str[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_Text.append(chr(x))
    return("".join(cipher_Text))

def originText(ciphertxt, key):
    origin = []
    for i in range(len(ciphertxt)):
        x = (ord(ciphertxt[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        origin.append(chr(x))
    return("". join(origin))

if __name__ == "__main__":
    str = input("Message = ")
    keywrd = input("Keyword = ")
    key = genKey(str, keywrd)
    ciphertext = cipherText(str, key)
    print("Ciphertext : ", ciphertext)
    print("Decrypted text : ", originText(ciphertext, key))