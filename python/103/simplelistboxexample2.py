import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class SimpleListboxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Listbox Example")

        # Listbox
        self.listbox = tk.Listbox(root, height=10, width=40)
        self.listbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Buttons
        tk.Button(root, text="Add Item", command=self.add_item).grid(row=1, column=0, pady=5, padx=5, sticky="ew")
        tk.Button(root, text="Delete Item", command=self.delete_item).grid(row=1, column=1, pady=5, padx=5, sticky="ew")
        tk.Button(root, text="Show Selected", command=self.show_selected).grid(row=1, column=2, pady=5, padx=5, sticky="ew")
        tk.Button(root, text="Random Select", command=self.random_select).grid(row=2, column=0, columnspan=3, pady=5, sticky="ew")

    def add_item(self):
        """Add a new item to the Listbox."""
        item = simpledialog.askstring("Add Item", "Enter the item to add:")
        if item:
            self.listbox.insert(tk.END, item)

    def delete_item(self):
        """Delete the selected item from the Listbox."""
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)
        else:
            messagebox.showerror("Error", "No item selected to delete.")

    def show_selected(self):
        """Show the selected item in a messagebox."""
        selected = self.listbox.curselection()
        if selected:
            item = self.listbox.get(selected)
            messagebox.showinfo("Selected Item", f"You selected: {item}")
        else:
            messagebox.showwarning("Warning", "No item selected.")

    def random_select(self):
        """Randomly select an item in the Listbox."""
        items = self.listbox.size()
        if items == 0:
            messagebox.showerror("Error", "No items in the list to select.")
            return

        random_index = random.randint(0, items - 1)  # Random index
        self.listbox.selection_clear(0, tk.END)      # Clear any existing selection
        self.listbox.selection_set(random_index)    # Set random selection
        self.listbox.activate(random_index)         # Highlight the selected item
        self.show_selected()                        # Optionally show the selected item

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleListboxApp(root)
    root.mainloop()
