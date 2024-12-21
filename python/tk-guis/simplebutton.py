import tkinter as tk
from tkinter import ttk

def greet():
    print("Hello world")

root = tk.Tk()
root.title("My tkinter App")
root.minsize(250, 250)

greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack()

root.mainloop()