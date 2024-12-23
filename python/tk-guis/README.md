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

## grid and weight
Just remember there is such thing as column and row weight and you can set it like that
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Greeter")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

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
Super easy to use and seems intuitive...

## sticky in grid
again, it is intuitive
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Greeter")

root.columnconfigure(1, weight=1)

first_name = tk.StringVar()
last_name = tk.StringVar()
user_age = tk.StringVar()

first_label = ttk.Label(root, text="First Name:").grid(row=0, column=0, padx=(0, 10))
first_entry = ttk.Entry(root, width=15, textvariable=first_name).grid(row=0, column=1, padx=(0, 10), sticky="we")

last_label = ttk.Label(root, text="Last Name:").grid(row=1, column=0, padx=(0, 10))
last_entry = ttk.Entry(root, width=15, textvariable=last_name).grid(row=1, column=1, padx=(0, 10), sticky="we")

age_label = ttk.Label(root, text="First Name:").grid(row=2, column=0, padx=(0, 10))
age_entry = ttk.Entry(root, width=15, textvariable=user_age).grid(row=2, column=1, padx=(0, 10), sticky="we")

root.mainloop()
```

## centered with frame
just check this out
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Greeter")

main = ttk.Frame(root, padding=(20, 10, 20, 0))
main.grid(row=0, column=0)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

first_name = tk.StringVar()
last_name = tk.StringVar()
user_age = tk.StringVar()

first_label = ttk.Label(main, text="First Name:").grid(row=0, column=0, padx=(0, 10))
first_entry = ttk.Entry(main, width=15, textvariable=first_name).grid(row=0, column=1, padx=(0, 10))

last_label = ttk.Label(main, text="Last Name:").grid(row=1, column=0, padx=(0, 10))
last_entry = ttk.Entry(main, width=15, textvariable=last_name).grid(row=1, column=1, padx=(0, 10))

age_label = ttk.Label(main, text="First Name:").grid(row=2, column=0, padx=(0, 10))
age_entry = ttk.Entry(main, width=15, textvariable=user_age).grid(row=2, column=1, padx=(0, 10))

root.mainloop()
```

## "margin auto" (centered in margin-inline)
here
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Greeter")

main = ttk.Frame(root, padding=(20, 10, 20, 0))
main.grid(row=0, column=0, sticky="n")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

first_name = tk.StringVar()
last_name = tk.StringVar()
user_age = tk.StringVar()

first_label = ttk.Label(main, text="First Name:").grid(row=0, column=0, padx=(0, 10))
first_entry = ttk.Entry(main, width=15, textvariable=first_name).grid(row=0, column=1, padx=(0, 10))

last_label = ttk.Label(main, text="Last Name:").grid(row=1, column=0, padx=(0, 10))
last_entry = ttk.Entry(main, width=15, textvariable=last_name).grid(row=1, column=1, padx=(0, 10))

age_label = ttk.Label(main, text="First Name:").grid(row=2, column=0, padx=(0, 10))
age_entry = ttk.Entry(main, width=15, textvariable=user_age).grid(row=2, column=1, padx=(0, 10))

root.mainloop()
```

## grid, frames, column weights, sticky
Check this out
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Greeter")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main = ttk.Frame(root, padding=(20, 10, 20, 0))
main.grid(row=0, column=0, sticky="nwe")

main.columnconfigure(1, weight=2)

first_name = tk.StringVar()
last_name = tk.StringVar()
user_age = tk.StringVar()

first_label = ttk.Label(main, text="First Name:").grid(row=0, column=0, padx=(0, 10))
first_entry = ttk.Entry(main, width=15, textvariable=first_name).grid(row=0, column=1, padx=(0, 10), sticky="we")

last_label = ttk.Label(main, text="Last Name:").grid(row=1, column=0, padx=(0, 10))
last_entry = ttk.Entry(main, width=15, textvariable=last_name).grid(row=1, column=1, padx=(0, 10), sticky="we")

age_label = ttk.Label(main, text="First Name:").grid(row=2, column=0, padx=(0, 10))
age_entry = ttk.Entry(main, width=15, textvariable=user_age).grid(row=2, column=1, padx=(0, 10), sticky="we")

root.mainloop()
```
Basically you need to get used to tkinter, its intuitive when you just use it. Either this or you can always use C# or Java and click your way throuh interface creation.

## Fixed size, no resizing
Its very simple
```python
root = tk.Tk()
root.title("My App")
root.geometry("800x600")
root.resizable(False, False)
```

## No fluent interfaces in methods like .grid, disabled entry
**We must remember, methods like .grid dont use fluent interfaces, they dont ***return this*** if you know what i mean**
Check this out:
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Greeter")
root.geometry("800x600")
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main = ttk.Frame(root, padding=(20, 10, 20, 0))
main.grid(row=0, column=0, sticky="nwe")

main.columnconfigure(1, weight=2)

first_name = tk.StringVar()
last_name = tk.StringVar()
user_age = tk.StringVar()

first_label = ttk.Label(main, text="First Name:").grid(row=0, column=0, padx=(0, 10))
first_entry = ttk.Entry(main, width=15, textvariable=first_name).grid(row=0, column=1, padx=(0, 10), sticky="we")
#FIRST ENTRY IS NONE, WE SHOULDNT EVEN CREATE VARIABLE, IF THATS HOW WE PLAY

last_label = ttk.Label(main, text="Last Name:").grid(row=1, column=0, padx=(0, 10))

last_entry = ttk.Entry(main, width=15, textvariable=last_name)
last_entry.grid(row=1, column=1, padx=(0, 10), sticky="we")
last_entry["state"] = "disabled"

age_label = ttk.Label(main, text="First Name:").grid(row=2, column=0, padx=(0, 10))

age_entry = ttk.Entry(main, width=15, textvariable=user_age)
age_entry.grid(row=2, column=1, padx=(0, 10), sticky="we")
age_entry.configure(state='disabled')

root.mainloop()
```

We split it like that not only to make our code more readable... For some reason first_entry is a variable that has None (grid method doesnt implement fluent interface, why idk, but we need to watch out)

## Separator (pack)
Fill x is crucial plus you must set orient (why not orientation if colspan is columnspan? such things are annoying)
Code
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Separator")

label1 = ttk.Label(root, text="Hello, World!", padding=20)

label1.pack()

ttk.Separator(root, orient="horizontal").pack(fill="x")

label2 = ttk.Label(root, text="Hello, World!", padding=20)

label2.pack()

ttk.Separator(root, orient="horizontal").pack(fill="x")

root.mainloop()
```

## Separator (grid)
In grid you need to have sticky we (or ne if orient vertical) or else your separator will be one pixel wide/tall
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Separator")

label1 = ttk.Label(root, text="First Label", padding=20)

label1.grid(row=0, column=0)

ttk.Separator(root, orient="horizontal").grid(row=1, column=0, sticky="we")

label2 = ttk.Label(root, text="Second Label", padding=20)

label2.grid(row=2, column=0)

ttk.Separator(root, orient="horizontal").grid(row=3, column=0, sticky="we")

root.mainloop()
```
Annoying, but if you know whats going on and where to find help, then not that annoying.

## Spinbox
Heres spinbox
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#(...)

main = ttk.Frame(root, padding=(20, 10, 20, 0))
main.grid(row=0, column=0, sticky="nwe")

main.columnconfigure(1, weight=2)

#(...)

user_age = tk.StringVar(value=18)

#(...)
age_label = ttk.Label(main, text="Age:").grid(row=2, column=0, padx=(0, 10))
age_entry = tk.Spinbox(main, from_=18, to=100, textvariable=user_age, wrap=False)
age_entry.grid(row=2, column=1, padx=(0, 10), sticky="we")

root.mainloop()
```
So from_ is minimum, to is maximum, textvariable points to variable (we have default value set to that varialbe), wrap false is normal behavior, wrap true would mean, that if your on minimum and click arrow down you get maximum (and the other way around).

## font-size
Example of font size btw note that entries ignore ipadx (there is a way around that)
```python
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

root = tk.Tk()
root.title("Greeter")
root.geometry("800x600")
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

fontApp = tkFont.Font(size=16)

main = ttk.Frame(root, padding=(20, 10, 20, 0))
main.grid(row=0, column=0, sticky="nwe")

main.columnconfigure(1, weight=2)

first_name = tk.StringVar()
last_name = tk.StringVar()
user_age = tk.StringVar(value=18)

first_label = ttk.Label(main, text="First Name:", font=fontApp)
first_label.grid(row=0, column=0, padx=(0, 10))

first_entry = ttk.Entry(main, width=15, textvariable=first_name, font=fontApp)
first_entry.grid(row=0, column=1, padx=(0, 10), ipady=5, sticky="we")


last_label = ttk.Label(main, text="Last Name:", font=fontApp)
last_label.grid(row=1, column=0, padx=(0, 10))

last_entry = ttk.Entry(main, width=15, textvariable=last_name, font=fontApp)
last_entry.grid(row=1, column=1, padx=(0, 10), ipady=5, sticky="we")


age_label = ttk.Label(main, text="Age:", font=fontApp)
age_label.grid(row=2, column=0, padx=(0, 10))

age_entry = tk.Spinbox(main, from_=18, to=100, textvariable=user_age, wrap=False, font=fontApp)
age_entry.grid(row=2, column=1, padx=(0, 10), ipady=5, sticky="we")


root.mainloop()
```

## bind onclick event and focus the widget
just check this code
```python
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

root = tk.Tk()
root.title("Greeter")
root.geometry("800x600")
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

fontApp = tkFont.Font(size=16)

main = ttk.Frame(root, padding=(20, 10, 20, 0))
main.grid(row=0, column=0, sticky="nwe")

main.columnconfigure(1, weight=2)

first_name = tk.StringVar()
last_name = tk.StringVar()
user_age = tk.StringVar(value=18)

first_label = ttk.Label(main, text="First Name:", font=fontApp)
first_label.grid(row=0, column=0, padx=(0, 10))
first_label.bind("<Button-1>", lambda _: first_entry.focus())

first_entry = ttk.Entry(main, width=15, textvariable=first_name, font=fontApp)
first_entry.grid(row=0, column=1, padx=(0, 10), ipady=5, sticky="we")


last_label = ttk.Label(main, text="Last Name:", font=fontApp)
last_label.grid(row=1, column=0, padx=(0, 10))
last_label.bind("<Button-1>", lambda _: last_entry.focus())

last_entry = ttk.Entry(main, width=15, textvariable=last_name, font=fontApp)
last_entry.grid(row=1, column=1, padx=(0, 10), ipady=5, sticky="we")


age_label = ttk.Label(main, text="Age:", font=fontApp)
age_label.grid(row=2, column=0, padx=(0, 10))
age_label.bind("<Button-1>", lambda _: age_entry.focus())

age_entry = tk.Spinbox(main, from_=18, to=100, textvariable=user_age, wrap=False, font=fontApp)
age_entry.grid(row=2, column=1, padx=(0, 10), ipady=5, sticky="we")


root.mainloop()
```

## input (entry) with numbers only
heres the code
```python
import tkinter as tk
from tkinter import ttk

def callback(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False


root = tk.Tk()
root.title("Validate ipt")
root.geometry("800x600")
root.resizable(False, False)

vcmd = root.register(callback)

some_entry = ttk.Entry(root, validate='all', validatecommand=(vcmd, '%P'))
some_entry.pack(side="left", expand=True, fill="x")

root.mainloop()
```
most examples show this in oop. in oop self is root (or self.root) and there we register, usually object method (that takes self as first argument and its self.callback).  
If you do such validations its a sign its time to switch to OOP, it gets complicated. But the bottom line is we register to the root element callback function.

## trace variable
Super simple variable tracing
```python
from tkinter import *

def callback(name, mode, sv):
    print(name, mode, sv.get())

root = Tk()
sv = StringVar()
sv.trace("w", lambda name, _, mode, sv=sv: callback(name, mode, sv))
e = Entry(root, textvariable=sv)
e.pack()
root.mainloop()  
```
_ is idx, ignore if the variable is scalar. all we basically care is variable.

## trace variable again
Idk i find this example more clear
```python
from tkinter import *

def callback(_var, _idx, _mode, variable):
    print(variable.get())

root = Tk()
sv = StringVar()
sv.trace_add("write", lambda name, index, mode, variable=sv : callback(name, index, mode, variable))
e = Entry(root, textvariable=sv)
e.pack()
root.mainloop()  
```

## tkinter oop
How to start writing OOP code in tkinter:
```python
import tkinter as tk
from tkinter import ttk


class HelloWorld(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Hello World!")

        ttk.Label(self, text="Hello, World!").pack()


root = HelloWorld()
root.mainloop()
```

## tkinter oop frame
code
```python
import tkinter as tk
from tkinter import ttk


class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.user_input = tk.StringVar()

        label = ttk.Label(self, text="Enter your name: ")
        entry = ttk.Entry(self, textvariable=self.user_input)
        button = ttk.Button(self, text="Greet", command=self.greet)

        label.pack(side="left")
        entry.pack(side="left")
        button.pack(side="left")
    
    def greet(self):
        print(f"Hello, {self.user_input.get()}!")



root = tk.Tk()
frame = UserInputFrame(root)
frame.pack()

root.mainloop()
```

## tk oop frame and root
good pattern
```python
import tkinter as tk
from tkinter import ttk

class HelloWorld(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Hello World!")

        frame = UserInputFrame(self)
        frame.pack()

class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.user_input = tk.StringVar()

        label = ttk.Label(self, text="Enter your name: ")
        entry = ttk.Entry(self, textvariable=self.user_input)
        button = ttk.Button(self, text="Greet", command=self.greet)

        label.pack(side="left")
        entry.pack(side="left")
        button.pack(side="left")
    
    def greet(self):
        print(f"Hello, {self.user_input.get()}!")



root = HelloWorld()
root.mainloop()
```

## grid sticky columnspan columnconfigure example
Example i found somewhere but its great. Copy paste and then do the following:
- change sticky from EW to W in right widgets
- remove sticky W from left widgets
- remove columnconfigure 0 weight 1
- add rowconfigure 0 weight 1
- change columnspan from 2 to 1 (or remove)
And youll get a feeling of it. Heres code:
```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Distance Converter")

root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30, 15))
main.grid()  # column=0 row=0 by default

# -- Widgets --

metres_label = ttk.Label(main, text="metres")
metres_input = ttk.Entry(main, width=10)
feet_label = ttk.Label(main, text="feet")
feet_display = ttk.Label(main, text="Feet shown here")
calc_button = ttk.Button(main, text="Calculate")

# -- Layout --

metres_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
metres_input.grid(column=1, row=0, sticky="EW", padx=5, pady=5)
metres_input.focus()

feet_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
feet_display.grid(column=1, row=1, sticky="EW", padx=5, pady=5)

calc_button.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5)

root.mainloop()
```

## widget children
dynamic work with all children of a widget (here - a frame called main)
```python
# winfo_children stands for "widget info children", and gets all the children of a widget.
for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)
```

## binding enter key to action
bidning enter key to some callback
```python
root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)
```

## Stacking frames and switching
Heres the code, in order to stack frames you must give them same grid position (and it must be explicit)
```python
import tkinter as tk
from tkinter import ttk


def clickhandler():
    second_active = is_second.get()
    if second_active:
        is_second.set(False)
        frame_1.tkraise()
    else:
        is_second.set(True)
        frame_2.tkraise()

root = tk.Tk()
root.title("App")

is_second =  tk.BooleanVar(value=True)

root.columnconfigure(0, weight=1)

frame_1 = ttk.Frame(root, padding=(30, 15))
frame_1.grid(column=0, row=0)  # column=0 row=0 by default

frame_2 = ttk.Frame(root, padding=(30, 15))
frame_2.grid(column=0, row=0)  # column=0 row=0 by default

btns = ttk.Frame(root, padding=(30, 15))
btns.grid(column=0, row=1)  # column=0 row=0 by default

# -- Widgets --

frame1_label = ttk.Label(frame_1, text="Frame1")
frame2_label = ttk.Label(frame_2, text="Frame2")
btn = ttk.Button(btns, text="Switch frame", command=clickhandler)
btn.grid(columnspan=2)

frame1_label.grid()
frame2_label.grid()

root.mainloop()
```
frame.tkraise() is responsible for showing given frame on top.

## OOP switching frames
Switching frames in OOP, good patterns
```python
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
```

## tkinter tabs
Thats how we create tabs in tkinter:
```python
import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title("Tabs App")
root.geometry("800x600")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

frame1 = tk.Frame(notebook)
ttk.Label(frame1, text="Frame 1").pack()
frame2 = tk.Frame(notebook)
ttk.Label(frame2, text="Frame 2").pack()
frame3 = tk.Frame(notebook)
ttk.Label(frame3, text="Frame 3").pack()

frame1.pack()
frame2.pack()
frame3.pack()

notebook.add(frame1, text="Tab 1")
notebook.add(frame2, text="Tab 2")
notebook.add(frame3, text="Tab 3")

root.mainloop()
```

## basic file sending
heres the code
```python
import tkinter as tk
import os
from tkinter import ttk 
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

main_directory = os.path.dirname(os.path.realpath(__file__))

def clickhandler():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=main_directory,
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

root = tk.Tk()
root.title("File Dialog App")
root.geometry("800x600")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame = tk.Frame(root)
main_frame.grid()

btn = ttk.Button(main_frame,text="Upload File", command=clickhandler)
btn.grid()
           

root.mainloop()
```