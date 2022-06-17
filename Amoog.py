from numpy import save
from CaesarCipher import encrypt as enc
import random as ran
import string

def encrypt(msg):
    '''
    
    This function makes use of the caesar cipher and replaces the letter with a block of text

    Parameters:
        msg: the message desired by the player

    Return:
        The ciphertext of the given message from the player
    '''
    msg = msg.upper() #replace all lower case letters in message w/uppercase
    alpha = string.ascii_uppercase
    tmp = enc(3, msg) #temporary encrypted message using casear cipher
    block=[] #block of letters to hide message within
    ciphertext = ""
    for letter in tmp:
        hid = letter
        ind = tmp.find(letter)
        for i in range(ind+1): 
            #creates a list with a length of the letter's location in the msg
            block = [None] * (ind+1)
            for j in range(len(block)): #populate block with randomized letters
                block[j] = alpha[ran.randint(0,26) % len(alpha)]
                block[i] = hid
        ciphertext += ("".join(block)) #turn block into string and add it into the ciphertext
    ciphertext += str(len(tmp))
    return ciphertext
