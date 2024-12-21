import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello {user_name.get() or 'World'}")

root = tk.Tk()

user_name = tk.StringVar()

root.title("My tkinter App")
root.geometry("800x600")

name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(anchor="nw", fill="x")

greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack(anchor="n")

exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(anchor="se", expand=True)

root.mainloop()