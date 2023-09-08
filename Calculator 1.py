#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from math import sqrt
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_back():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square_root():
    try:
        value = float(entry.get())
        result = sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def factorial():
    try:
        value = int(entry.get())
        result = 1
        for i in range(1, value + 1):
            result *= i
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create a GUI window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x460")

# Create an entry field
entry = tk.Entry(root, width=49 ,borderwidth=6,font="bold 13")
entry.grid(row=0, column=0, columnspan=4,ipadx=15,ipady=15,pady=10,padx=0)

# Create buttons
buttons = [
    ('C', 1, 0), ('√ ', 1, 1), ('/', 1, 2), ('<-', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('!', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
]

for (text, row, col) in buttons:
    if text == "√ ":
        button = tk.Button(root, text=text,font="bold 12", padx=8, pady=10, command=square_root)
    elif text == "!":
        button = tk.Button(root, text=text,font="bold 12", padx=10, pady=10, command=factorial)
    elif text == "C":
        button = tk.Button(root, text=text,font="bold 12", padx=10, pady=10, command=button_clear)
    elif text == "<-":
        button = tk.Button(root, text=text,font="bold 12", padx=10, pady=10, command=button_back)
    elif text == "=":
        button = tk.Button(root, text=text,font="bold 12", padx=10, pady=10, command=calculate)
    else:
        button = tk.Button(root, text=text, padx=10, pady=10, command=lambda num=text: button_click(num))
    button.grid(row=row, column=col,padx=1,pady=10)

# Start the GUI event loop
root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




