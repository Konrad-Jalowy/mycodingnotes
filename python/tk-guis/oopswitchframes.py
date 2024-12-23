import tkinter as tk
from tkinter import ttk


class MyApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("My App")
        self.frames = dict()

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        container = ttk.Frame(self)
        container.grid(padx=10, pady=10)

        for FrameClass in (FirstFrame, SecondFrame):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        self.show_frame(FirstFrame)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class FirstFrame(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        frame_label = ttk.Label(self, text="First Frame", anchor="center")
        frame_label.grid(column=0, row=0, sticky="EW", ipadx=5)
        
        switch_page_button = ttk.Button(
            self,
            text="Switch to second frame",
            command=lambda: controller.show_frame(SecondFrame)
        )
        switch_page_button.grid(column=0, row=1, sticky="EW")
       
class SecondFrame(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        frame_label = ttk.Label(self, text="Second Frame", anchor="center")
        frame_label.grid(column=0, row=0, sticky="EW", ipadx=5)

        switch_page_button = ttk.Button(
            self,
            text="Switch to first frame",
            command=lambda: controller.show_frame(FirstFrame)
        )
        switch_page_button.grid(column=0, row=1, sticky="EW")

    
root = MyApp()
root.mainloop()