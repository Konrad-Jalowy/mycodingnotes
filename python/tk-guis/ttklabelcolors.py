import tkinter as tk
from tkinter import ttk


root = tk.Tk()

root.title("My tkinter App")
root.geometry("800x600")

rect_1 = ttk.Label(root, text="Rectangle 1", background="green", foreground="white")
rect_1.pack()

rect_2 = ttk.Label(root, text="Rectangle 2", background="red", foreground="white")
rect_2.pack()

root.mainloop()