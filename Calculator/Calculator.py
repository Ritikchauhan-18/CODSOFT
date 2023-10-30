import tkinter as tk
from tkinter import ttk

def update_input(number):
    current_input = input_box.get()
    updated_input = current_input + str(number)
    input_box.delete(0, tk.END)
    input_box.insert(0, updated_input)

def clear_input():
    input_box.delete(0, tk.END)
    output_box.delete(0, tk.END)

def backspace():
    current_input = input_box.get()
    updated_input = current_input[:-1]
    input_box.delete(0, tk.END)
    input_box.insert(0, updated_input)

def calculate():
    expression = input_box.get()
    try:
        result = eval(expression)
        output_box.configure(state="normal")
        output_box.delete(0, tk.END)
        output_box.insert(0, f"Result: {result}")
        output_box.configure(state="readonly")
    except Exception as e:
        output_box.configure(state="normal")
        output_box.delete(0, tk.END)
        output_box.insert(0, "Error")
        output_box.configure(state="readonly")

root = tk.Tk()
root.title("Calculator")
root.geometry("500x450")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 14))
style.configure("TEntry", font=("Helvetica", 12))

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=20, pady=20)

input_box = ttk.Entry(frame)
output_box = ttk.Entry(frame)
input_box.grid(row=0, column=0, columnspan=4, pady=10)
output_box.grid(row=1, column=0, columnspan=4, pady=10)
output_box.configure(state="readonly")

# Number Buttons
for i in range(1, 10):
    ttk.Button(frame, text=str(i), command=lambda num=i: update_input(num)).grid(row=(i-1)//3+2, column=(i-1)%3, pady=5)

# Operations Buttons
ttk.Button(frame, text='+', command=lambda: update_input('+')).grid(row=2, column=3, pady=5)
ttk.Button(frame, text='-', command=lambda: update_input('-')).grid(row=3, column=3, pady=5)
ttk.Button(frame, text='*', command=lambda: update_input('*')).grid(row=4, column=3, pady=5)
ttk.Button(frame, text='/', command=lambda: update_input('/')).grid(row=5, column=3, pady=5)

# Backspace and Clear Buttons
ttk.Button(frame, text="Backspace", command=backspace).grid(row=6, column=0, pady=5)
ttk.Button(frame, text="Clear", command=clear_input).grid(row=6, column=1, pady=5)

# Equal Button
ttk.Button(frame, text="=", command=calculate).grid(row=6, column=3, pady=5)

root.mainloop()
