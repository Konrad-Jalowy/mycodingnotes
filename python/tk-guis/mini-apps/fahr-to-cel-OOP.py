import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class FahrToCelConverter(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Fahr to Cel Converter")
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

        self.vcmd = self.register(self.input_callback)

        self.fahr_text = tk.StringVar(value="")
        self.fahr_text.trace_add("write", self.on_input_change)
        self.converted_text = tk.StringVar(value="")

        self.label_input = ttk.Label(self, text="Temperature in Fahr: ")
        self.entry_input = ttk.Entry(self, textvariable=self.fahr_text, validate='all', validatecommand=(self.vcmd, '%P'))

        self.label_output = ttk.Label(self, text="Temperature in Cel: ")
        self.entry_output = ttk.Entry(self, textvariable=self.converted_text, state="readonly")
        
        self.btn = tk.Button(self, text="Convert", command=self.clickhandler)

        self.label_input.grid(row=0, column=0, sticky="W")
        self.entry_input.grid(row=0, column=1)

        self.label_output.grid(row=1, column=0, sticky="W")
        self.entry_output.grid(row=1, column=1)

        self.btn.grid(row=2, column=0, columnspan=2, sticky="ew")
    
    def clickhandler(self):
        if self.fahr_text.get() == "":
            return
        _fahr = float(self.fahr_text.get())
        _cel = self.fahr_to_cel(_fahr)
        self.converted_text.set(f"{_cel}")

    def fahr_to_cel(self, fahrenheit): 
        celsius = (fahrenheit - 32) * 5 / 9 
        return celsius 

    def on_input_change(self, *args):
        self.converted_text.set(f"")

    def input_callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False
    
root = FahrToCelConverter()
root.mainloop()