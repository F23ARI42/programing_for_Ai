from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("calculator")
mylabel = Label(window, text="Calculator")
mylabel.pack()
window.minsize(400, 400)
input1=Entry(window)
input1.pack()
input2=Entry(window)
input2.pack()
def get_plus():
    input4=int(input1.get())+int(input2.get())
    messagebox.showinfo("Msg",f"result: {input4}")
    return input1.get(), input2.get()
plus=Button(window, text="+",command=get_plus,)
plus.place(x=100, y=300)  # Set x and y coordinates
def get_mius():
    input4=int(input1.get())-int(input2.get())
    messagebox.showinfo("Msg",f"result: {input4}")
    return input1.get(), input2.get()
minus=Button(window, text="-",command=get_mius)
minus.place(x=5,y=300)  # Set x and y coordinates
def get_multiple():
    input4=int(input1.get())*int(input2.get())
    messagebox.showinfo("Msg",f"result: {input4}")
    return input1.get(), input2.get()
multiply=Button(window, text="*",command=get_multiple)
multiply.pack()
def get_division():
    input4=int(input1.get())/int(input2.get())
    messagebox.showinfo("Msg",f"result: {input4}")
    return input1.get(), input2.get()
divide=Button(window, text="/",command=get_division)
divide.pack()
window.mainloop()
