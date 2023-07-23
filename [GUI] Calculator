import tkinter as tk
from tkinter import messagebox
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate_percentage():
    num = float(entry_num.get())
    percent = float(entry_percent.get())
    result = (num * percent) / 100
    result_label_percentage.config(text=f"The percentage is: {result}")

def perform_calculations():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        result = "Invalid operation"

    result_label_calculator.config(text=f"The result is: {result}")

def sort_numbers():
    numbers = entry_numbers.get().split(",")
    numbers = [float(num.strip()) for num in numbers if num.strip()]

    if len(numbers) > 0:
        sorted_numbers = sorted(numbers, reverse=True)
        result_label_sorting.config(text=f"The sorted numbers (highest to lowest) are: {sorted_numbers}")
    else:
        result_label_sorting.config(text="No numbers to sort.")

def calculate_exponentiation():
    base = float(entry_base.get())
    exp = float(entry_exp.get())
    result = base ** exp
    result_label_exponentiation.config(text=f"The exponentiation result is: {result}")

def show_calculator():
    frame_start.pack_forget()
    frame_calculator.pack()

def show_sorting():
    frame_start.pack_forget()
    frame_sorting.pack()

def show_percentage():
    frame_start.pack_forget()
    frame_percentage.pack()

def show_exponentiation():
    frame_start.pack_forget()
    frame_exponentiation.pack()

def go_back(frame):
    frame.pack_forget()
    frame_start.pack()

window = tk.Tk()
window.title("Calculator Program")

frame_start = tk.Frame(window)

label_start = tk.Label(frame_start, text="Select an option:")
label_start.pack()

button_calculator = tk.Button(frame_start, text="Calculator", command=show_calculator)
button_calculator.pack()

button_sorting = tk.Button(frame_start, text="Sorting", command=show_sorting)
button_sorting.pack()

button_percentage = tk.Button(frame_start, text="Percentage", command=show_percentage)
button_percentage.pack()

button_exponentiation = tk.Button(frame_start, text="Exponentiation", command=show_exponentiation)
button_exponentiation.pack()

frame_calculator = tk.Frame(window)

label_num1 = tk.Label(frame_calculator, text="Number 1:")
label_num1.pack()
entry_num1 = tk.Entry(frame_calculator)
entry_num1.pack()

label_num2 = tk.Label(frame_calculator, text="Number 2:")
label_num2.pack()
entry_num2 = tk.Entry(frame_calculator)
entry_num2.pack()

operation_var = tk.StringVar()
operation_var.set("+")
label_operation = tk.Label(frame_calculator, text="Operation:")
label_operation.pack()
radio_add = tk.Radiobutton(frame_calculator, text="+", variable=operation_var, value="+")
radio_add.pack()
radio_subtract = tk.Radiobutton(frame_calculator, text="-", variable=operation_var, value="-")
radio_subtract.pack()
radio_multiply = tk.Radiobutton(frame_calculator, text="*", variable=operation_var, value="*")
radio_multiply.pack()
radio_divide = tk.Radiobutton(frame_calculator, text="/", variable=operation_var, value="/")
radio_divide.pack()

button_calculate = tk.Button(frame_calculator, text="Calculate", command=perform_calculations)
button_calculate.pack()

result_label_calculator = tk.Label(frame_calculator, text="")
result_label_calculator.pack()

button_back_calculator = tk.Button(frame_calculator, text="Go Back", command=lambda: go_back(frame_calculator))
button_back_calculator.pack()

frame_sorting = tk.Frame(window)

label_numbers = tk.Label(frame_sorting, text="Enter numbers (comma-separated):")
label_numbers.pack()
entry_numbers = tk.Entry(frame_sorting)
entry_numbers.pack()

button_sort = tk.Button(frame_sorting, text="Sort", command=sort_numbers)
button_sort.pack()

result_label_sorting = tk.Label(frame_sorting, text="")
result_label_sorting.pack()

button_back_sorting = tk.Button(frame_sorting, text="Go Back", command=lambda: go_back(frame_sorting))
button_back_sorting.pack()

frame_percentage = tk.Frame(window)

label_num = tk.Label(frame_percentage, text="Number:")
label_num.pack()
entry_num = tk.Entry(frame_percentage)
entry_num.pack()

label_percent = tk.Label(frame_percentage, text="Percentage:")
label_percent.pack()
entry_percent = tk.Entry(frame_percentage)
entry_percent.pack()

button_calculate_percentage = tk.Button(frame_percentage, text="Calculate", command=calculate_percentage)
button_calculate_percentage.pack()

result_label_percentage = tk.Label(frame_percentage, text="")
result_label_percentage.pack()

button_back_percentage = tk.Button(frame_percentage, text="Go Back", command=lambda: go_back(frame_percentage))
button_back_percentage.pack()

frame_exponentiation = tk.Frame(window)

label_base = tk.Label(frame_exponentiation, text="Base:")
label_base.pack()
entry_base = tk.Entry(frame_exponentiation)
entry_base.pack()

label_exp = tk.Label(frame_exponentiation, text="Exponent:")
label_exp.pack()
entry_exp = tk.Entry(frame_exponentiation)
entry_exp.pack()

button_calculate_exponentiation = tk.Button(frame_exponentiation, text="Calculate", command=calculate_exponentiation)
button_calculate_exponentiation.pack()

result_label_exponentiation = tk.Label(frame_exponentiation, text="")
result_label_exponentiation.pack()

button_back_exponentiation = tk.Button(frame_exponentiation, text="Go Back", command=lambda: go_back(frame_exponentiation))
button_back_exponentiation.pack()

frame_start.pack()

window.mainloop()
