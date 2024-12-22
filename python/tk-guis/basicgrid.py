import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Greeter")

first_name = tk.StringVar()
last_name = tk.StringVar()
user_age = tk.StringVar()

first_label = ttk.Label(root, text="First Name:").grid(row=0, column=0, padx=(0, 10))
first_entry = ttk.Entry(root, width=15, textvariable=first_name).grid(row=0, column=1, padx=(0, 10))

last_label = ttk.Label(root, text="Last Name:").grid(row=1, column=0, padx=(0, 10))
last_entry = ttk.Entry(root, width=15, textvariable=last_name).grid(row=1, column=1, padx=(0, 10))

age_label = ttk.Label(root, text="First Name:").grid(row=2, column=0, padx=(0, 10))
age_entry = ttk.Entry(root, width=15, textvariable=user_age).grid(row=2, column=1, padx=(0, 10))

root.mainloop()