import tkinter as tk
from tkinter import ttk

def button_click(symbol):
    if symbol =='C':
        clear_entry()
    elif symbol == '=':
        perform_calculation()
    else:
        current =entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + symbol)

def clear_entry():
    entry.delete(0, tk.END)

def perform_calculation():
    expression =entry.get()
    try:
        result =eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

window =tk.Tk()
window.title("Calculator")

entry = tk.Entry(window, font=("Arial", 21))
entry.grid(row=0,column=0,columnspan=4, ipadx=8, ipady=8)

style = ttk.Style()
style.configure('TButton',foreground='black', background='lightgray', font=('Arial', 18))  

buttons = [
    ('C', 1, 0),('/', 1, 1),('*', 1, 2),('-', 1, 3),
    ('7', 2, 0), ('8', 2, 1),('9', 2, 2),('+', 2, 3),
    ('4', 3, 0),('5', 3, 1), ('6', 3, 2), ('=', 3, 3),
    ('1', 4, 0), ('2', 4, 1),('3', 4, 2), ('0', 4, 3),
    ('.', 5, 0)
]

for (text, row, col) in buttons:
    ttk.Button(window, text=text, command=lambda t=text: button_click(t),style='TButton').grid(row=row, column=col, padx=5, pady=5, ipadx=20, ipady=20)

window.mainloop()
