import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Separator")

label1 = ttk.Label(root, text="Hello, World!", padding=20)

label1.pack()

ttk.Separator(root, orient="horizontal").pack(fill="x")

label2 = ttk.Label(root, text="Hello, World!", padding=20)

label2.pack()

ttk.Separator(root, orient="horizontal").pack(fill="x")

root.mainloop()