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

## expand vs fill
- **fill** - tells element if it should use allocated space that is left or not (and which one, x space, y space or both)
- **expand** - take side top for example. it has all x allocated, but the question is whats with the opposite axis. if false/no expand, then it takes as much as it needs and is not allocated more. if true, it takes as much as it needs but is allocated more (and it can take more if you set fill to y or both)
Example:
```python
import tkinter as tk

root = tk.Tk()

root.title("My tkinter App")
root.geometry("800x600")

rect_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rect_1.pack(ipadx=10, ipady=10, fill="both", side="top", expand=True)

rect_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rect_2.pack(ipadx=10, ipady=10, side="top", expand=True)

root.mainloop()
```
So here we have 2 elements side top. So they all take 100% width, like block elements in css they are put one below the other.  
Then, they all expand, so they will share y space between them (they get 50-50).  
First one have fill both, so it has size 100% width and 50% heigth.  
Second doesnt have fill, so technically it has width 100% and height 50%, but the visible part doesnt have that and is centered.  
Tbh not so complicated.

## side left vs side top
As you know, side top gets all x space allocated and can expand in terms of y space.  
With side left its the opposite.
Here we have 2 rectangles, both have height 100% and width 50%:
```python
import tkinter as tk

root = tk.Tk()

root.title("My tkinter App")
root.geometry("800x600")

rect_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rect_1.pack(ipadx=10, ipady=10, fill="both", side="left", expand=True)

rect_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rect_2.pack(ipadx=10, ipady=10, fill="both", side="left", expand=True)

root.mainloop()
```
Ok so basically in pack we have 2 types of sides:
- main axis is x (side top)
- main axis is y (side left)

On main axis element is allocated 100% space (but if the visible part uses it depends on fill attribute).  
On cross axis (speaking flexbox) element is allocated the same space as its content, but it with expand true it can expand, sharing space with other elements with expand true and same side.  
I know it sounds complicated but tbh tkinter pack is easier than many CSS layout techniques. Its simple and with windows, frames and so on you can really create layouts you need once you figure out how it works, you dont have to use grid or place (but you can).  

So yeah, fill both, side left, takes 100% height and expand true, expands in terms of width, since 2 elements are side left expand true they share width 50-50 since 100% height 50% width each. Fill both means visible part is stretched in x and y, if not, they would be centered withing allocated space and have "fit-content" kind of size, if you know what i mean (if not, try it out...)

## Frames
Take a look what weve got here (it wasnt my example by the way):
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)

tk.Label(main, text="Label top left", bg="red").pack(side="top", expand=True, fill="both")
tk.Label(main, text="Label bottom left", bg="red").pack(side="top", expand=True, fill="both")
tk.Label(root, text="Label right", bg="green").pack(
    side="left", expand=True, fill="both"
)

root.mainloop()
```
So its divided 50-50 (the width). Label right has 50% width (if you maximize) and 100% height. Labels inside frame have height 50% each and the frame has width 50%.  
Frame is side left so it is allocated 100% heigth and it expands there. Frame children are side top so they are allocated all width (of its parent) and they expand.  
Label added to root is the same side that frame (left) and has 100% heigth and they share width 50-50.  Its actually very easy to get while coding and seems like fun, you can layout the GUI using pack any way you like.  
Most people hate pack because they think gird or place are proper ways and pack is for demo purposes, but honestly, you can do much with pack. And if you care that much about how your app looks like, why use tkiner in the first place? Its great for creating GUIs with Python but its not used for great UI/UX...

## Stacking content in tkiner
Heres example of how to stack content in tkinter using pack (also note ttk.Entry focus method, nice to know)
```python
import tkinter as tk
from tkinter import ttk


def greet():
    print(f"Hello, {user_name.get() or 'World'}!")


root = tk.Tk()
root.title("Greeter")

user_name = tk.StringVar()


input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.pack(fill="both")

name_label = ttk.Label(input_frame, text="Name: ")
name_label.pack(side="left", padx=(0, 10))

name_entry = ttk.Entry(input_frame, textvariable=user_name)
name_entry.pack(side="left", expand=True, fill="both")
name_entry.focus()

buttons_frame = ttk.Frame(root, padding=(20, 10))
buttons_frame.pack(fill="both")

greet_button = ttk.Button(buttons_frame, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True)
quit_button = ttk.Button(buttons_frame, text="Quit", command=root.destroy)
quit_button.pack(side="right", fill="x", expand=True)

root.mainloop()
```
For simple apps theres no need to use grid or place. I feel kinda dumb, because i always used grid thinking pack is good only for "demo apps" (i used to write GUIs in tkinter, now im re-visiting the topic)

## Basic grid in tkinter
Long time no see:
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Greeter")

first_name = tk.StringVar()
last_name = tk.StringVar()
user_age = tk.StringVar()

first_label = ttk.Label(root, text="First Name:").grid(row=0, column=0, padx=(0, 10))
first_entry = ttk.Entry(root, width=15, textvariable=first_name).grid(row=0, column=1, padx=(0, 10))

last_label = ttk.Label(root, text="Last Name:").grid(row=1, column=0, padx=(0, 10))
last_entry = ttk.Entry(root, width=15, textvariable=last_name).grid(row=1, column=1, padx=(0, 10))

age_label = ttk.Label(root, text="First Name:").grid(row=2, column=0, padx=(0, 10))
age_entry = ttk.Entry(root, width=15, textvariable=user_age).grid(row=2, column=1, padx=(0, 10))

root.mainloop()
```