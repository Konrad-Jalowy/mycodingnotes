import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Greeter")
root.geometry("800x600")
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main = ttk.Frame(root, padding=(20, 10, 20, 0))
main.grid(row=0, column=0, sticky="nwe")

main.columnconfigure(1, weight=2)

first_name = tk.StringVar()
last_name = tk.StringVar()
user_age = tk.StringVar()

first_label = ttk.Label(main, text="First Name:").grid(row=0, column=0, padx=(0, 10))
first_entry = ttk.Entry(main, width=15, textvariable=first_name).grid(row=0, column=1, padx=(0, 10), sticky="we")
#FIRST ENTRY IS NONE, WE SHOULDNT EVEN CREATE VARIABLE, IF THATS HOW WE PLAY

last_label = ttk.Label(main, text="Last Name:").grid(row=1, column=0, padx=(0, 10))

last_entry = ttk.Entry(main, width=15, textvariable=last_name)
last_entry.grid(row=1, column=1, padx=(0, 10), sticky="we")
last_entry["state"] = "disabled"

age_label = ttk.Label(main, text="First Name:").grid(row=2, column=0, padx=(0, 10))

age_entry = ttk.Entry(main, width=15, textvariable=user_age)
age_entry.grid(row=2, column=1, padx=(0, 10), sticky="we")
age_entry.configure(state='disabled')

root.mainloop()