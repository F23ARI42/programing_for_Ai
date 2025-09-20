from tkinter import *
window = Tk()
#task1
window.geometry("300x300")
window.title("Miles to Kilometer Conversion:")
#Label(window, text="Miles to Kilometer").grid(column=2, row=2)
input = Entry(window)
input.grid(column=1, row=1)
Label(window, text="miles").grid(column=2, row=1)
Label(window, text="Kilometer").grid(column=2, row=2)
Label(window, text="is equal to").grid(column=0, row=2)
label_entry=Label(window,text="0")
label_entry.grid(column=1, row=2)
def kilometer():
    miles = float(input.get())
    km=miles*1.609344
    label_entry.config(text=f"{km}")
button = Button(window, text="Convert", command=kilometer)
button.grid(column=1, row=3)
window.mainloop()

