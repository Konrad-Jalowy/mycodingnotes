import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello {user_name.get() or 'World'}")

root = tk.Tk()

user_name = tk.StringVar()

root.title("My tkinter App")
root.geometry("800x600")

name_entry = ttk.Entry(root,  textvariable=user_name)
name_entry.pack(anchor="nw", side=tk.LEFT, fill="x", expand=True)

greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack(anchor="n", side=tk.LEFT, expand=False)

exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(anchor="ne", side=tk.LEFT, expand=False)

root.mainloop()