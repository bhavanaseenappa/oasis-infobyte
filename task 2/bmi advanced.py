import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100
        bmi = weight / (height ** 2)
        result_label.config(text=f'Your BMI is: {bmi:.2f}')
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Label(root, text="Height (cm):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
