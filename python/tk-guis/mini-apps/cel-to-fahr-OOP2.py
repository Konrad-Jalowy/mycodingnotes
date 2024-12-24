import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class CelToFahrConverter(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Cel to Fahr Converter")
        self.geometry("800x600")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.fontApp = tkFont.Font(size=16)

        frame = UserInputFrame(self)
        frame.grid()
        
        for child in frame.winfo_children():
            child.configure(font=self.fontApp)
            

class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.cel_text = tk.StringVar(value="")
        self.converted_text = tk.StringVar(value="")

        self.label_input = ttk.Label(self, text="Temperature in Celsius: ")
        self.entry_input = ttk.Entry(self, textvariable=self.cel_text)

        self.label_output = ttk.Label(self, text="Temperature in Fahr: ")
        self.entry_output = ttk.Entry(self, textvariable=self.converted_text, state="readonly")
        
        self.btn = tk.Button(self, text="Convert", command=self.clickhandler)

        self.label_input.grid(row=0, column=0, sticky="W")
        self.entry_input.grid(row=0, column=1)

        self.label_output.grid(row=1, column=0, sticky="W")
        self.entry_output.grid(row=1, column=1)

        self.btn.grid(row=2, column=0, columnspan=2, sticky="ew")
    
    def clickhandler(self):
        _cel = float(self.cel_text.get())
        _fahr = self.cel_to_fahr(_cel)
        self.converted_text.set(f"{_fahr}")

    def cel_to_fahr(self, cel):
        return (cel * 1.8) + 32
    
root = CelToFahrConverter()
root.mainloop()