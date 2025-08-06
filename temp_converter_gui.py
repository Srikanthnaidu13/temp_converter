import tkinter as tk
from tkinter import ttk, messagebox

# Conversion functions
def convert():
    try:
        temp = float(entry.get())
        scale_from = combo_from.get()
        scale_to = combo_to.get()

        if scale_from == scale_to:
            result.set(f"Result: {temp:.2f} {scale_to}")
            return

        # Convert from any scale to Celsius first
        if scale_from == "Celsius":
            c = temp
        elif scale_from == "Fahrenheit":
            c = (temp - 32) * 5/9
        elif scale_from == "Kelvin":
            c = temp - 273.15

        # Convert from Celsius to target scale
        if scale_to == "Celsius":
            final = c
        elif scale_to == "Fahrenheit":
            final = (c * 9/5) + 32
        elif scale_to == "Kelvin":
            final = c + 273.15

        result.set(f"Result: {final:.2f} {scale_to}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number!")

# Create the main window
root = tk.Tk()
root.title("🌡️ Temperature Converter")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Widgets
title = tk.Label(root, text="Temperature Converter", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify='center')
entry.pack(pady=10)

scales = ["Celsius", "Fahrenheit", "Kelvin"]

combo_from = ttk.Combobox(root, values=scales, state="readonly")
combo_from.set("Celsius")
combo_from.pack(pady=5)

combo_to = ttk.Combobox(root, values=scales, state="readonly")
combo_to.set("Fahrenheit")
combo_to.pack(pady=5)

btn = tk.Button(root, text="Convert", font=("Arial", 12), command=convert, bg="#007acc", fg="white")
btn.pack(pady=10)

result = tk.StringVar()
output = tk.Label(root, textvariable=result, font=("Arial", 14), bg="#f0f0f0")
output.pack(pady=10)

# Start the app
root.mainloop()
