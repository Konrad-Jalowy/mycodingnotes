import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

root = tk.Tk()
root.title("Greeter")
root.geometry("800x600")
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

fontApp = tkFont.Font(size=16)

main = ttk.Frame(root, padding=(20, 10, 20, 0))
main.grid(row=0, column=0, sticky="nwe")

main.columnconfigure(1, weight=2)

first_name = tk.StringVar()
last_name = tk.StringVar()
user_age = tk.StringVar(value=18)

first_label = ttk.Label(main, text="First Name:", font=fontApp)
first_label.grid(row=0, column=0, padx=(0, 10))
first_label.bind("<Button-1>", lambda _: first_entry.focus())

first_entry = ttk.Entry(main, width=15, textvariable=first_name, font=fontApp)
first_entry.grid(row=0, column=1, padx=(0, 10), ipady=5, sticky="we")


last_label = ttk.Label(main, text="Last Name:", font=fontApp)
last_label.grid(row=1, column=0, padx=(0, 10))
last_label.bind("<Button-1>", lambda _: last_entry.focus())

last_entry = ttk.Entry(main, width=15, textvariable=last_name, font=fontApp)
last_entry.grid(row=1, column=1, padx=(0, 10), ipady=5, sticky="we")


age_label = ttk.Label(main, text="Age:", font=fontApp)
age_label.grid(row=2, column=0, padx=(0, 10))
age_label.bind("<Button-1>", lambda _: age_entry.focus())

age_entry = tk.Spinbox(main, from_=18, to=100, textvariable=user_age, wrap=False, font=fontApp)
age_entry.grid(row=2, column=1, padx=(0, 10), ipady=5, sticky="we")


root.mainloop()