import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12, use_digits=True, use_symbols=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_click():
    name = name_entry.get()
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for password length.")
        return

    password = generate_password(length)
    messagebox.showinfo("Generated Password", f"Hi {name}, your generated password is: {password}")

def reset_button_click():
    name_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)

app = tk.Tk()
app.title("Password Generator")
app.geometry("400x200") 

name_label = tk.Label(app, text="Enter your name:")
name_label.pack()
name_entry = tk.Entry(app)
name_entry.pack()

length_label = tk.Label(app, text="Enter password length:")
length_label.pack()
length_entry = tk.Entry(app)
length_entry.pack()

generate_button = tk.Button(app, text="Generate Password", command=generate_button_click)
generate_button.pack()

reset_button = tk.Button(app, text="Reset", command=reset_button_click)
reset_button.pack()

app.mainloop()
