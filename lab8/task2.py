from tkinter import *
from tkinter import messagebox
window = Tk()
#task2
window.geometry("300x300")
window.title("login page ")
input1 = Entry(window,width=20)
input1.grid(column=5, row=3,padx=40,pady=5)
input2 = Entry(window,width=20)
input2.grid(column=5, row=4,padx=40,pady=5)
def signup():
    username = input1.get()
    password = input2.get()
    if username and password:
         with open("file.txt", "a") as file:
             file.write(f"{username},{password}\n")
             messagebox.showinfo("Success","User created successfully")
    else:
        messagebox.showerror("Error","Please enter both username and password")
button = Button(window,text="signup",command=signup)
button.grid(column=5, row=5)
def login():
    username = input1.get().strip()
    password = input2.get().strip()
    try:
        with open("file.txt", "r") as file:
            users = file.readlines()
            for user in users:
               use= user.strip()
               if not use or "," not in use:  # Skip empty or malformed lines
                   continue
               store_name,store_password = use.split(",",1)
               if username == store_name and password == store_password:
                    window.destroy()  # Close the login windo
                    open_dasboad(username)  # Open new window
                    return
            messagebox.showerror("Login Failed", "Invalid Username or Password!")
    except FileNotFoundError:
        messagebox.showerror("user not found","please sign up first")
def open_dasboad(username):
    window1=Tk()
    window1.geometry("300x300")
    window.mainloop()
button=Button(window,text="login",command=login)
button.grid(column=6, row=5)
window.mainloop()