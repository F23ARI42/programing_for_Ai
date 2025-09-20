from tkinter import *
from tkinter import messagebox
import requests
window = Tk()
window.geometry("600x300")
window.title("quotes app:")
quote_label =Label(window, text="Click the button for a Kanye quote!", font=("Arial", 14), pady=20, justify="center")
quote_label.pack()
def get_quotes():
    try:
        api=requests.get("https://api.kanye.rest")
        response=api.json()["quote"]
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Something went wrong")
    quote_label.config(text=response)
button=Button(window, text="Get Quotes", command=get_quotes)
button.pack()
window.mainloop()