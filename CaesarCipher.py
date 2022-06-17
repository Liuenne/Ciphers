import string

alpha = string.ascii_uppercase

def encrypt (key, msg):
    '''
    
    This function takes a message and moves each letter based on a static key

    Parameters:
        key: the integer key used to move each letter of the cipher
        msg: the user's message they desire to be encrypted
    
    Return:
        the ciphertext of the message from the player using the key
    '''
    msg = msg.upper() #convert each letter to an uppercase version
    cipher = ""
    for letter in msg:
        if letter in alpha: 
            letterind = (alpha.find(letter) + key) % len(alpha) #
            cipher = cipher + alpha[letterind]
        else:
            cipher = cipher + letter
    return cipher

def decrypt(key,ciphertext):
    '''
    
    This function takes the ciphertext of the previous function as well as the key to return the user's message

    Parameters:
        key: the static key used to reverse the encryption of the encrypt function
        ciphertext: the encrypted string for the function to decode

    Return:
        The original message that was inputed by the user
    '''
    ciphertext = ciphertext.upper()
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