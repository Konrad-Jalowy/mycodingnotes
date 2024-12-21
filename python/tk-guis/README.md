# tkinter-GUIs Python
Notes on creating tkinter GUIs in Python

## test your tkinter
self-explanatory
```python
import tkinter

tkinter._test()
```

## mainloop
```python
import tkinter as tk

root = tk.Tk()

root.mainloop()
```

## window title
its a **function**
```python
import tkinter as tk

root = tk.Tk()
root.title("My tkinter App")

root.mainloop()
```

## window minsize
```python
import tkinter as tk

root = tk.Tk()
root.title("My tkinter App")
root.minsize(250, 250)

root.mainloop()
```

## Simple ttk label
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My tkinter App")
root.minsize(250, 250)

ttk.Label(root, text="Hello World").pack()

root.mainloop()
```

## Simple button with simple action
```python
import tkinter as tk
from tkinter import ttk

def greet():
    print("Hello world")

root = tk.Tk()
root.title("My tkinter App")
root.minsize(250, 250)

greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack()

root.mainloop()
```

## exit tk window
**Always use root.destroy, quit still runs in the background!!!**
```python
import tkinter as tk
from tkinter import ttk

def greet():
    print("Hello world")

root = tk.Tk()
root.title("My tkinter App")
root.minsize(250, 250)

greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack()

exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack()

root.mainloop()
```


## window geometry
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My tkinter App")
root.geometry("800x600")

root.mainloop()
```

## side
Either lowercase strings:
```python
import tkinter as tk
from tkinter import ttk

def greet():
    print("Hello world")

root = tk.Tk()
root.title("My tkinter App")
root.geometry("800x600")


greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack(side="left")

exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(side="right")

root.mainloop()
```
Or tk.CONSTS such as LEFT, RIGHT, BOTTOM, TOP (uppercase, in tkinter module, here imported as tk)
```python
import tkinter as tk
from tkinter import ttk

def greet():
    print("Hello world")

root = tk.Tk()
root.title("My tkinter App")
root.geometry("800x600")


greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack(side=tk.LEFT)

exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(side=tk.RIGHT)

root.mainloop()
```

## side and anchor
You can combine them if you must, but anchor has all 8 directions, so it shouldnt be necessary:
```python
import tkinter as tk
from tkinter import ttk

def greet():
    print("Hello world")

root = tk.Tk()
root.title("My tkinter App")
root.geometry("800x600")


greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack(side=tk.LEFT, anchor="n")

exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(side=tk.RIGHT, anchor="s")

root.mainloop()
```

## anchor (8 directions) and expand true
If you plan to use just anchor with its directions remember about expand, sometimes its needed (youll see)
```python
import tkinter as tk
from tkinter import ttk

def greet():
    print("Hello world")

root = tk.Tk()
root.title("My tkinter App")
root.geometry("800x600")


greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack(anchor="nw")

exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(anchor="se", expand=True)

root.mainloop()
```

## Entry widget and string var
```python
import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello {user_name.get() or 'World'}")

root = tk.Tk()

user_name = tk.StringVar()

root.title("My tkinter App")
root.geometry("800x600")

name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(anchor="nw", fill="x")

greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack(anchor="n")

exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(anchor="se", expand=True)

root.mainloop()
```

## pack items side by side
If we want to use pack to put items side by side, we must use both anchor and side
```python
import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello {user_name.get() or 'World'}")

root = tk.Tk()

user_name = tk.StringVar()

root.title("My tkinter App")
root.geometry("800x600")

name_entry = ttk.Entry(root,  textvariable=user_name)
name_entry.pack(anchor="nw", side=tk.LEFT, fill="x", expand=True)

greet_btn = ttk.Button(root, text="Greet", command=greet)
greet_btn.pack(anchor="n", side=tk.LEFT, expand=False)

exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(anchor="ne", side=tk.LEFT, expand=False)

root.mainloop()
```
Advice: you can understand how it works, but still you need to mess around with it, get a feeling of it, trial and error just like in CSS.

## ttk.Label (ttk widgets), background, foreground
**Its background and foreground for ttk widgets!**
```python
import tkinter as tk
from tkinter import ttk


root = tk.Tk()

root.title("My tkinter App")
root.geometry("800x600")

rect_1 = ttk.Label(root, text="Rectangle 1", background="green", foreground="white")
rect_1.pack()

rect_2 = ttk.Label(root, text="Rectangle 2", background="red", foreground="white")
rect_2.pack()

root.mainloop()
```

## tk.Label (tk widgets), bg and fg
**Its bg and fg for tk widgets!**
```python
import tkinter as tk

root = tk.Tk()

root.title("My tkinter App")
root.geometry("800x600")

rect_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rect_1.pack()

rect_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rect_2.pack()

root.mainloop()
```

## ipadx ipady padding in tkiner
**Supposedly ipad stands for internal padding...**
```python
import tkinter as tk

root = tk.Tk()

root.title("My tkinter App")
root.geometry("800x600")

rect_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rect_1.pack(ipadx=10, ipady=10)

rect_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rect_2.pack(ipadx=10, ipady=10)

root.mainloop()
```

## margin called pad
For whatever reason margin-block is called pady and margin-inline padx.  
**Watch out: no margin collapsing in tkinter. So two elements with pady 10 its not the same as one with. They all add up, thats it**
```python
import tkinter as tk

root = tk.Tk()

root.title("My tkinter App")
root.geometry("800x600")

rect_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rect_1.pack(ipadx=10, ipady=10, pady=10)

rect_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rect_2.pack(ipadx=10, ipady=10, pady=10)

root.mainloop()
```

## pack default side is top, fill x
**default side for pack (you dont have to write it) is top. elements with side top get all x space allocated and only as much of y as they need and are sticked to the top**
Fill x makes element use all x space it has been allocated
```python
import tkinter as tk

root = tk.Tk()

root.title("My tkinter App")
root.geometry("800x600")

rect_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rect_1.pack(ipadx=10, ipady=10, side="top", fill="x")

rect_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rect_2.pack(ipadx=10, ipady=10, side="top", fill="x")

root.mainloop()
```
In this example you:
- dont need to specify side top, its default
- since side top, it has as much y as it needs and is sticked to top
- since side top, it has all y space allocated
- since fill x, it uses all that x space

## side top expand
what do we have here:
```python
import tkinter as tk

root = tk.Tk()

root.title("My tkinter App")
root.geometry("800x600")

rect_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rect_1.pack(ipadx=10, ipady=10, fill="x", side="top", expand=True)

rect_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rect_2.pack(ipadx=10, ipady=10, fill="x", side="top")

root.mainloop()
```
Well:
- elements have side top so they use only as much y as they need and have allocated all x space
- fill x makes those elements use all x space theyve been allocated
- expand true makes first element been allocated more y space than it needs, basically y space is divided now between those two elements
- the element is not on the top anymore but it started there

## fill both expand true
fill both means element will use all x and y space it has been allocated.
expand true means it will expand. like element with side top has all x space allocated, but it can expand in terms of y space.
example
```python
import tkinter as tk

root = tk.Tk()

root.title("My tkinter App")
root.geometry("800x600")

rect_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rect_1.pack(ipadx=10, ipady=10, fill="both", side="top", expand=True)

rect_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rect_2.pack(ipadx=10, ipady=10, fill="both", side="top", expand=True)

root.mainloop()
```
So they both take all width and they share heigth (they each occupy 50%). 