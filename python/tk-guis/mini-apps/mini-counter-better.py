import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

def clickHandler():
    click_number = clicked_counter.get()
    click_number += 1
    clicked_counter.set(click_number)
    clicked_text.set(f"Clicked: {clicked_counter.get()}")

root = tk.Tk()
root.title("Greeter")
root.geometry("800x600")
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

fontApp = tkFont.Font(size=16)

main = ttk.Frame(root, padding=(20, 10, 20, 0))
main.grid(row=0, column=0)

clicked_counter = tk.IntVar(value=0)
clicked_text = tk.StringVar(value="")
clicked_text.set(f"Clicked: {clicked_counter.get()}")


click_label = ttk.Label(main, textvariable=clicked_text, font=fontApp)
click_label.grid(row=0, column=0, padx=(0, 10))

btn = tk.Button(main, text="Click me", command=clickHandler, font=fontApp)
btn.grid(row=1, column=0, padx=(0, 10))

root.mainloop()

