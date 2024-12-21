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
greet_btn.pack(side=tk.LEFT, anchor="nw")

exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(side=tk.RIGHT, anchor="se")

root.mainloop()
```