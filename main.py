from tkinter import *
from random import randrange

root = Tk()
root.title("RSA by MathWave")
root.geometry('300x300')
root.resizable(width=False, height=False)

label_private = Label(root, text='Закрытый ключ: ')
label_private.place(x=10, y=10)
label_public = Label(root, text='Открытый ключ: ')
label_public.place(x=10, y=40)

canvas_private = Canvas(root, width=120, height=20, bg='black')
canvas_private.place(x=120, y=10)
canvas_public = Canvas(root, width=120, height=20, bg='black')
canvas_public.place(x=120, y=40)

label_key = Label(root, text='Ключ:')
label_key.place(x=10, y=100)
label_text = Label(root, text='Сообщение:')
label_text.place(x=10, y=130)

entry_key = Entry(root)
entry_text = Entry(root)
entry_key.place(x=100, y=100)
entry_text.place(x=100, y=130)

canvas_text = Canvas(root, width=290, height=130, bg='black')
canvas_text.pack(side='bottom')

def IsPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)

def FindExp(phi):
    return e

def FindSecretExp(phi, e):
    for d in range(phi):
        if (d * e) % phi == 1:
            return d

def CreateKey():
    p = 10
    q = 10
    while not IsPrime(p):
        p = randrange(500, 1000)
    while not IsPrime(q) or p == q:
        q = randrange(500, 1000)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = randrange(2, phi)
    while NOD(e, phi) != 1:
        e = (e + 1)
    d = FindSecretExp(phi, e)
    canvas_private.delete('all')
    canvas_public.delete('all')
    canvas_private.create_text(10, 12, anchor=W, fill='white', text=(str(d) + " " + str(n)))
    canvas_public.create_text(10, 12, anchor=W, fill='white', text=(str(e) + " " + str(n)))

def Encrypt():
    coms = entry_key.get().split()
    message = entry_text.get()
    ord_letters = []
    for letter in message:
        ord_letters.append(ord(letter))
    new_text = ""
    for number in ord_letters:
        new_text += (str((number ** int(coms[0])) % int(coms[1])) + " ")
    canvas_text.delete('all')
    canvas_text.create_text(145, 65, width=250, fill='white', text=new_text)

def Decrypt():
    coms = entry_key.get().split()
    message = entry_text.get().split()
    int_message = []
    for i in message:
        int_message.append(int(i))
    new_text = ""
    for number in int_message:
        new_text += chr((number ** int(coms[0])) % int(coms[1]))
    canvas_text.delete('all')
    canvas_text.create_text(145, 65, width=250, fill='white', text=new_text)

btn_generate = Button(root, text="Сгенерировать!")
btn_generate.bind('<Button-1>', lambda event: CreateKey())
btn_generate.place(x=10, y=70)

btn_crypt = Button(root, text="->")
btn_crypt.bind('<Button-1>', lambda event: Encrypt())
btn_crypt.place(x=150, y=70)

btn_crypt = Button(root, text="<-")
btn_crypt.bind('<Button-1>', lambda event: Decrypt())
btn_crypt.place(x=200, y=70)

root.mainloop()
