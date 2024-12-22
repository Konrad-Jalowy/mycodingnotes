import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Separator")

label1 = ttk.Label(root, text="First Label", padding=20)

label1.grid(row=0, column=0)

ttk.Separator(root, orient="horizontal").grid(row=1, column=0, sticky="we")

label2 = ttk.Label(root, text="Second Label", padding=20)

label2.grid(row=2, column=0)

ttk.Separator(root, orient="horizontal").grid(row=3, column=0, sticky="we")

root.mainloop()