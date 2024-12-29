import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

root = tk.Tk()
root.title("My tkinter App")
root.geometry("800x600")


def selectfile():
    _filename = askopenfilename(filetypes=[("Text files", "*.txt")])
    file_name.set(_filename)

def readfile():
    _filename = file_name.get()
    with open(_filename, 'r') as file:
        for line in file:
            Text.insert(tk.INSERT, line)


file_name = tk.StringVar()

label = ttk.Label(root, text="Filename")
label.pack()

filename_entry = ttk.Entry(root, state="readonly", textvariable=file_name)
filename_entry.pack(ipadx=55)

btn = ttk.Button(root, text="Choose file", command=selectfile)
btn.pack()

Text = tk.Text(root, height=20, width=40)
Text.pack()

btn2 = ttk.Button(root, text="Read", command=readfile)
btn2.pack()

root.mainloop()