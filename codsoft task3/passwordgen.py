import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        password = generate_password(length)
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for password length.")

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Label and entry for password length
length_label = tk.Label(app, text="Enter password length:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(app)
length_entry.grid(row=0, column=1, padx=5, pady=5)

# Button to generate password
generate_button = tk.Button(app, text="Generate Password", command=generate)
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Label to display generated password
password_var = tk.StringVar()
password_label = tk.Label(app, text="Generated Password:")
password_label.grid(row=2, column=0, padx=5, pady=5)
password_display = tk.Label(app, textvariable=password_var, relief="solid")
password_display.grid(row=2, column=1, padx=5, pady=5)

# Run the application
app.mainloop()
