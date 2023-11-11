import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()

    if complexity == "Low":
        characters = string.ascii_letters
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated_password)

def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)

root = tk.Tk()
root.title("Advanced Password Generator")
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

length_label = ttk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
length_entry = ttk.Entry(frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)
length_entry.insert(0, "12")

complexity_label = ttk.Label(frame, text="Complexity:")
complexity_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
complexity_var = tk.StringVar()
complexity_combobox = ttk.Combobox(frame, textvariable=complexity_var, values=["Low", "Medium", "High"])
complexity_combobox.grid(row=1, column=1, padx=5, pady=5)
complexity_combobox.current(1)

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

password_entry = ttk.Entry(frame, show='*')
password_entry.grid(row=3, column=0, padx=5, pady=5, columnspan=2, sticky='we')
copy_button = ttk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=4, column=0, columnspan=2, pady=10)

for child in frame.winfo_children():
    child.grid_configure(padx=10, pady=5)

root.mainloop()

