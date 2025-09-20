import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.configure(bg='#f0f0f0')

        # Create main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(expand=True, fill='both')

        # Title
        ttk.Label(self.main_frame, text="Password Generator", font=('Arial', 16, 'bold')).pack(pady=10)

        # Length input
        length_frame = ttk.Frame(self.main_frame)
        length_frame.pack(pady=10)
        ttk.Label(length_frame, text="Password Length:").pack(side='left', padx=5)
        self.length_var = tk.StringVar(value="12")
        self.length_entry = ttk.Entry(length_frame, textvariable=self.length_var, width=5)
        self.length_entry.pack(side='left', padx=5)

        # Generate button
        ttk.Button(self.main_frame, text="Generate Password", command=self.generate_password).pack(pady=10)

        # Password display
        self.password_var = tk.StringVar()
        self.password_label = ttk.Label(
            self.main_frame,
            textvariable=self.password_var,
            font=('Courier', 12),
            background='white',
            padding=10,
            width=30,
            anchor='center'
        )
        self.password_label.pack(pady=10)

        # Copy button
        ttk.Button(self.main_frame, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length < 4:
                self.password_var.set("Password length must be at least 4")
                return
            
            # Define character sets
            lowercase = string.ascii_lowercase
            uppercase = string.ascii_uppercase
            digits = string.digits
            symbols = string.punctuation

            # Ensure at least one character from each set
            password = [
                random.choice(lowercase),
                random.choice(uppercase),
                random.choice(digits),
                random.choice(symbols)
            ]

            # Fill the rest with random characters
            all_chars = lowercase + uppercase + digits + symbols
            password.extend(random.choice(all_chars) for _ in range(length - 4))

            # Shuffle the password
            random.shuffle(password)
            
            # Convert to string and display
            self.password_var.set(''.join(password))
        except ValueError:
            self.password_var.set("Please enter a valid number")

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password and password != "Please enter a valid number" and password != "Password length must be at least 4":
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.password_var.set("Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop() 