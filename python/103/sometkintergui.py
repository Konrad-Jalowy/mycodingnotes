import tkinter as tk
from tkinter import messagebox, simpledialog, ttk


class UserManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Management App")

        # User list
        self.user_list = []

        # Label Frame for User Form
        self.form_frame = tk.LabelFrame(root, text="Add User", padx=10, pady=10)
        self.form_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(self.form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.form_frame, text="Age:").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(self.form_frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(self.form_frame, text="Add User", command=self.add_user).grid(row=2, column=0, columnspan=2, pady=5)

        # Treeview for displaying users
        self.tree_frame = tk.LabelFrame(root, text="User List", padx=10, pady=10)
        self.tree_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.tree = ttk.Treeview(self.tree_frame, columns=("Name", "Age"), show="headings", height=8)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.column("Name", width=150)
        self.tree.column("Age", width=50)
        self.tree.pack(fill="both", expand=True)

        # Buttons for actions
        self.button_frame = tk.Frame(root)
        self.button_frame.grid(row=2, column=0, pady=10)

        tk.Button(self.button_frame, text="Edit User", command=self.edit_user).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="Delete User", command=self.delete_user).grid(row=0, column=1, padx=5)

    def add_user(self):
        """Add a user to the list and display in Treeview."""
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()

        if not name or not age.isdigit():
            messagebox.showerror("Error", "Invalid input! Please provide a valid name and age.")
            return

        self.user_list.append({"Name": name, "Age": int(age)})
        self.update_treeview()
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)

    def update_treeview(self):
        """Update the Treeview with the current user list."""
        self.tree.delete(*self.tree.get_children())
        for user in self.user_list:
            self.tree.insert("", tk.END, values=(user["Name"], user["Age"]))

    def edit_user(self):
        """Edit the selected user."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No user selected!")
            return

        item = self.tree.item(selected_item)
        name, age = item["values"]

        new_name = simpledialog.askstring("Edit User", "Enter new name:", initialvalue=name)
        new_age = simpledialog.askinteger("Edit User", "Enter new age:", initialvalue=age)

        if new_name and new_age:
            for user in self.user_list:
                if user["Name"] == name and user["Age"] == age:
                    user["Name"] = new_name
                    user["Age"] = new_age
                    break
            self.update_treeview()

    def delete_user(self):
        """Delete the selected user."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No user selected!")
            return

        item = self.tree.item(selected_item)
        name, age = item["values"]

        self.user_list = [user for user in self.user_list if user["Name"] != name or user["Age"] != age]
        self.update_treeview()


if __name__ == "__main__":
    root = tk.Tk()
    app = UserManagementApp(root)
    root.mainloop()
