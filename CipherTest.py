import random as ran
import string
#This function is similar to the Caesar cipher but with a random key for each letter
def encrypt(msg):
    '''
    
    This function functions similarly to the caesar cipher however with a non-static key for each letter

    Parameters:
        msg: The user's message for the function to encrypt

    Return: 
        The ciphertext of the message from the user
    '''
    text = msg.upper()
    alpha = string.ascii_uppercase
    ciphertxt = ''
    for letter in text:
        key = ran.randint(-26,26)
        if key == 0:
            key += ran.randint(1,26)
        if letter in alpha:
            letind = (alpha.find(letter) + key) % len(alpha)
            ciphertxt += alpha[letind]
        else:
            ciphertxt += letter
    return ciphertxt