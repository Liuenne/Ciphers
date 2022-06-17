def genKey(msg, keywrd):
    '''
    This function creates a key to be used for encryption through using the message and keyword given

    Parameters:
        msg: the message desired by the user
        keywrd: the keyword to be used in the encryption process

    Returns:
        a string to be used in the encryption process
    '''
    key = list(keywrd.upper())
    if len(msg) == len(keywrd):
        return(keywrd)
    else:
        for i in range(len(msg)-len(keywrd)):
            key.append(keywrd[i % len(keywrd)])
    return("".join(key))


def cipherText(msg, key):
    '''
    
    This function makes use of the previous key function to encrypt a message securely

    Parameters:
        msg: The message desired by the player
        key: The keyword to be used with the message in the encryption process

    Return:
        The ciphertext of the message given by the user
    '''
    msg = msg.upper()
    cipher_Text=[]
    for i in range(len(msg)):
        #converts the letters to their unicode and adds them together
        index = (ord(msg[i]) + ord(key[i])) % 26
        index += ord('A')
        cipher_Text.append(chr(index))
    return("".join(cipher_Text))


def originText(ciphertxt, key):
    '''
    
    This function uses the provided key to reverse the ciphertext back to the user's message

    Parameters:
        ciphertxt: The ciphertext from the above function to be deciphered
        key: the key used to encrypt the user's message

    Return:
        The message from the user from the ciphertext
    '''
    origin = []
    for i in range(len(ciphertxt)):
        x = (ord(ciphertxt[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        origin.append(chr(x))
    return("". join(origin))

if __name__ == "__main__":
    msg = input("Message = ")
    keywrd = input("Keyword = ")
    key = genKey(msg, keywrd)
    ciphertext = cipherText(msg, key)
    print("Ciphertext : ", ciphertext)
    print("Decrypted text : ", originText(ciphertext, key))