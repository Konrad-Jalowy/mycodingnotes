import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class Helper:
    def __init__(self, parent):
        parent.vcmd = parent.register(self.input_callback)
        self.converted_text = parent.converted_text
        
    def fahr_to_cel(self, fahrenheit): 
        celsius = (fahrenheit - 32) * 5 / 9 
        return celsius 
    def cel_to_fahr(self, cel):
        return (cel * 1.8) + 32
    def input_callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False
    def on_input_change(self, *args):
        self.converted_text.set(f"")

class TemperatureConverter(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Temperature Converter")
        self.geometry("800x600")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.fontApp = tkFont.Font(size=16)
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid()
        
        for FrameClass in (CelToFahrFrame, FahrToCelFrame):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")
            for child in frame.winfo_children():
                child.configure(font=self.fontApp)
        

        self.show_frame(FahrToCelFrame)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()        

class CelToFahrFrame(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.converted_text = tk.StringVar(value="")
        self.helper = Helper(self)

        self.cel_text = tk.StringVar(value="")
        self.cel_text.trace_add("write", self.helper.on_input_change)
        

        self.label_input = ttk.Label(self, text="Temperature in Celsius: ")
        self.entry_input = ttk.Entry(self, textvariable=self.cel_text, validate='all', validatecommand=(self.vcmd, '%P'))

        self.label_output = ttk.Label(self, text="Temperature in Fahr: ")
        self.entry_output = ttk.Entry(self, textvariable=self.converted_text, state="readonly")
        
        self.btn = tk.Button(self, text="Convert", command=self.clickhandler)
        self.btn2 = tk.Button(self, text="Fahr to Cell", command=lambda: controller.show_frame(FahrToCelFrame))

        self.label_input.grid(row=0, column=0, sticky="W")
        self.entry_input.grid(row=0, column=1)

        self.label_output.grid(row=1, column=0, sticky="W")
        self.entry_output.grid(row=1, column=1)

        self.btn.grid(row=2, column=0, columnspan=2, sticky="ew")
        self.btn2.grid(row=3, column=0, columnspan=2, sticky="ew")
    
    def clickhandler(self):
        _cel = float(self.cel_text.get())
        _fahr = self.helper.cel_to_fahr(_cel)
        self.converted_text.set(f"{_fahr}")

    
class FahrToCelFrame(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.converted_text = tk.StringVar(value="")
        self.helper = Helper(self)

        self.fahr_text = tk.StringVar(value="")
        self.fahr_text.trace_add("write", self.helper.on_input_change)
        

        self.label_input = ttk.Label(self, text="Temperature in Fahr: ")
        self.entry_input = ttk.Entry(self, textvariable=self.fahr_text, validate='all', validatecommand=(self.vcmd, '%P'))

        self.label_output = ttk.Label(self, text="Temperature in Cel: ")
        self.entry_output = ttk.Entry(self, textvariable=self.converted_text, state="readonly")
        
        self.btn = tk.Button(self, text="Convert", command=self.clickhandler)
        self.btn2 = tk.Button(self, text="Cel to fahr", command=lambda: controller.show_frame(CelToFahrFrame))

        self.label_input.grid(row=0, column=0, sticky="W")
        self.entry_input.grid(row=0, column=1)

        self.label_output.grid(row=1, column=0, sticky="W")
        self.entry_output.grid(row=1, column=1)

        self.btn.grid(row=2, column=0, columnspan=2, sticky="ew")
        self.btn2.grid(row=3, column=0, columnspan=2, sticky="ew")
    
    def clickhandler(self):
        if self.fahr_text.get() == "":
            return
        _fahr = float(self.fahr_text.get())
        _cel = self.helper.fahr_to_cel(_fahr)
        self.converted_text.set(f"{_cel}")


root = TemperatureConverter()
root.mainloop()