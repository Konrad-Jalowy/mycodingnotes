import tkinter as tk
from tkinter import ttk

def greet():
    print("Hello world")

root = tk.Tk()
root.title("My tkinter App")
root.geometry("800x600")


greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack(anchor="nw")

exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(anchor="se", expand=True)

root.mainloop()