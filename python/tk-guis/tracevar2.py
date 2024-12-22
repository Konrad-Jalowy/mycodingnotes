from tkinter import *

def callback(_var, _idx, _mode, variable):
    print(variable.get())

root = Tk()
sv = StringVar()
sv.trace_add("write", lambda name, index, mode, variable=sv : callback(name, index, mode, variable))
e = Entry(root, textvariable=sv)
e.pack()
root.mainloop()  