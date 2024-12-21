import tkinter as tk

root = tk.Tk()

root.title("My tkinter App")
root.geometry("800x600")

rect_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rect_1.pack(ipadx=10, ipady=10, fill="both", side="left", expand=True)

rect_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rect_2.pack(ipadx=10, ipady=10, fill="both", side="left", expand=True)

root.mainloop()