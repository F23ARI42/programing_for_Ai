import random as rnd
from tkinter import *
from tkinter import messagebox
#task3
letters=("abcdefghijklmnopqrstuvwxyz").lower()
window = Tk()
window.geometry("300x300")
window.title("password generator")
input1=Entry(window,width=20)
input1.grid(row=2,column=1,padx=10,pady=10)
entry_label=Label(window,text="0")
entry_label.grid(row=2,column=3,padx=20,pady=20)
password=[]
def generate():
    change_input=int(input1.get())
    for i in range(change_input):
        password.append(rnd.choice(letters))
        rnd.shuffle(password)
        entry_label.config(text=password)
button=Button(window,text="generate",command=generate)
button.grid(row=3,column=1)
window.mainloop()

