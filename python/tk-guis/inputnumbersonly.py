import tkinter as tk
from tkinter import ttk

def callback(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False


root = tk.Tk()
root.title("Validate ipt")
root.geometry("800x600")
root.resizable(False, False)

vcmd = root.register(callback)

some_entry = ttk.Entry(root, validate='all', validatecommand=(vcmd, '%P'))
some_entry.pack(side="left", expand=True, fill="x")

root.mainloop()
