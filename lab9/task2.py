import tkinter as tk
from tkinter import messagebox
import requests


# Function to fetch sunrise and sunset data
def get_sun_times(type_):
    country = country_entry.get()
    lat = latitude_entry.get()
    lon = longitude_entry.get()

    if not lat or not lon:
        messagebox.showerror("Error", "Please enter latitude and longitude.")
        return

    try:
        response = requests.get(f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}&formatted=0")
        data = response.json()
        if type_ == "sunrise":
                messagebox.showinfo("Sunrise Time", f"Sunrise Time: {data['results']['sunrise']}")
        else:
                messagebox.showinfo("Sunset Time", f"Sunset Time: {data['results']['sunset']}")
    except Exception:
        messagebox.showerror("Error", "Something went wrong, Please Try Again Later.")
root = tk.Tk()
root.title("Sunrise & Sunset App")
tk.Label(root, text="Country Name:").grid(row=0, column=0, padx=5, pady=5)
country_entry = tk.Entry(root)
country_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Latitude:").grid(row=1, column=0, padx=5, pady=5)
latitude_entry = tk.Entry(root)
latitude_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Longitude:").grid(row=2, column=0, padx=5, pady=5)
longitude_entry = tk.Entry(root)
longitude_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
tk.Button(root, text="Get Sunrise", command=lambda: get_sun_times("sunrise")).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="Get Sunset", command=lambda: get_sun_times("sunset")).grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
