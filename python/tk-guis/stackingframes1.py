import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("App")

root.columnconfigure(0, weight=1)

frame_1 = ttk.Frame(root, padding=(30, 15))
frame_1.grid(column=0, row=0)  # column=0 row=0 by default

frame_2 = ttk.Frame(root, padding=(30, 15))
frame_2.grid(column=0, row=0)  # column=0 row=0 by default

# -- Widgets --

frame1_label = ttk.Label(frame_1, text="Frame1")
frame2_label = ttk.Label(frame_2, text="Frame2")

frame1_label.grid()
frame2_label.grid()

root.mainloop()