from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
from CaesarCipher import encrypt as c_enc
from VignereCipher import cipherText as V_enc
from VignereCipher import genKey as G_key
from CipherTest import encrypt as R_enc
from Amoog import encrypt as enc
import sys

#Main Frame
frame = Tk()
frame.title("Ciphers")

#Tabs
tabCont = ttk.Notebook(frame)
t1 = ttk.Frame(tabCont)
t2 = ttk.Frame(tabCont)
t3 = ttk.Frame(tabCont)
t4 = ttk.Frame(tabCont)
#adding the tabs to the frame with labels for each cipher
tabCont.add(t1, text="Casear Cipher")
tabCont.add(t2, text="Vignere Cipher")
tabCont.add(t3, text="Random Casear Cipher")
tabCont.add(t4, text="Amoog (Inspried by Vishal Thilak) Cipher")
tabCont.pack(fill = 'both')

def Caesar_cipher():
    '''
    
    A function to be used by the Caesar Cipher tab to run the cipher and display the output. 

    '''
    inp = casaerInp.get(1.0, "end-1c")
    lbl1.config(text = "Ciphertext: " + c_enc(3,inp))

def Vignere_cipher():
    '''

    A function to be used by the Vigenere Cipher tab to run the cipher and display the output.

    '''
    inp = vigInp.get(1.0,"end-1c")
    key = Vkey.get(1.0, "end-1c")
    key = G_key(inp, key)
    lbl2.config(text="Ciphertext: " + V_enc(inp,key))

def Random_cipher():
    '''
    
    A function to be used by the Random Cipher tab to run the cipher and display the output.
    
    '''
    inp = rInp.get(1.0, "end-1c")
    lbl3.config(text = "Ciphertext: " + R_enc(inp))

def Amoog_cipher():
    '''
    
    A function to be used by the Amoog (Inspired by Vishal Thilak) Cipher tab to run the cipher and display the output.

    '''
    inp = Einp.get(1.0, "end-1c")
    lbl4.config(text="Ciphertext: " + enc(inp))

#takes in inputs for each tab to be used in cipher functions
casaerInp = Text(t1, height=20, width= 50)
casaerInp.pack()
Vl1 = Label(t2, text="Type you message here:").pack() 
vigInp = Text(t2, height = 10, width = 50)
vigInp.pack()
Vl2 = Label(t2, text="Type the keyword here:").pack()
Vkey = Text(t2, height = 10, width = 50)
Vkey.pack()
rInp = Text(t3, height = 20, width = 50)
rInp.pack()
Einp = Text(t4, height=20, width=50)
Einp.pack()

#Creates buttons for the tabs to encrypt the given message
b1 = Button(t1, text="Encrypt", command=Caesar_cipher).pack()
b2 = Button(t2, text="Encrypt", command=Vignere_cipher).pack()
b3 = Button(t3, text="Encrypt", command=Random_cipher).pack()
b4 = Button(t4, text="Encrypt", command=Amoog_cipher).pack()

#temporary empty labels to dispay the ciphertext
lbl1 = Label(t1, text="")
lbl1.pack()
lbl2 = Label(t2, text="")
lbl2.pack()
lbl3 = Label(t3, text="")
lbl3.pack()
lbl4 = Label(t4, text="")
lbl4.pack()


def close(event):
    '''
    
    This function makes use of the sys import to perform an exit of the program. (Close the window)

    '''
    sys.exit()
frame.bind("<Escape>", close) #binds the Escape key to the above close function to allow for the function to be used
frame.mainloop()