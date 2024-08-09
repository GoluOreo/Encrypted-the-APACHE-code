'''Encrypted: the APACHE code
Anchit
Python
ASCII
Cybersecurity/Cipher/Coding/Computer Programming
Hexadecimal
Encryption'''

from tkinter import *
from ast import literal_eval
import random

root = Tk()
root.title('ASCII')
root.geometry('5000x5000')
root.configure(bg = 'black')

label = Label(root, text='...',bg='red',fg='dark blue')

label.place(relx=0.5,rely=0.6,anchor=CENTER)

e = Entry(root)
e.place(relx=0.5,rely=0.4,anchor=CENTER)



def encrypt():
    label['text'] = ''
    r = random.randint(0, 16)
    rlist = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e','f']
    label['text'] += str(rlist[(r-1)]) + str(rlist[random.randint(0, 16)])
    w = e.get()
    o = ''
    for c in range(r):
        for letter in w:
            string = str(hex(ord(letter)))
            o += string.replace('','',1) + ' '
        w = o
        o = ''
    label['text'] = w
        

btn = Button(root,text='ENCRYPT',command=encrypt,bg='sky blue',fg='maroon')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)



root.mainloop()