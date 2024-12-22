import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

def cel_to_fahr(cel):
    return (cel * 1.8) + 32

def click_handler():
    _cel = float(cel_text.get())
    _fahr = cel_to_fahr(_cel)
    converted_text.set(f"{_fahr}")


root = tk.Tk()
root.title("Cel to Fahr Converter")
root.geometry("800x600")
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

fontApp = tkFont.Font(size=16)

cel = tk.DoubleVar(value=0)
cel_text = tk.StringVar(value="")
converted_text = tk.StringVar(value="")

main_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
main_frame.grid(row=0, column=0)

input_label = ttk.Label(main_frame, text="Cel:", font=fontApp)
input_label.grid(row=0, column=0, padx=(0, 10))

input_entry = ttk.Entry(main_frame, textvariable=cel_text)
input_entry.grid(row=0, column=1, padx=(0, 10), ipady=5)

output_label = ttk.Label(main_frame, text="Fahr:", font=fontApp)
output_label.grid(row=1, column=0, padx=(0, 10))

output_entry = ttk.Entry(main_frame, textvariable=converted_text, state="readonly")
output_entry.grid(row=1, column=1, padx=(0, 10), ipady=5)

btn = tk.Button(main_frame, text="Convert", font=fontApp, command=click_handler)
btn.grid(row=2, column=0, columnspan=2, padx=(0, 10), sticky="ew")

root.mainloop()