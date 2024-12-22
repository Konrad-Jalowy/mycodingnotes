from tkinter import *

def callback(name, mode, sv):
    print(name, mode, sv.get())

root = Tk()
sv = StringVar()
sv.trace("w", lambda name, _, mode, sv=sv: callback(name, mode, sv))
e = Entry(root, textvariable=sv)
e.pack()
root.mainloop()  