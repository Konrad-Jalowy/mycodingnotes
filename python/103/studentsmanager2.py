import os
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import tkinter as tk
from tkinter import messagebox, simpledialog

Base = declarative_base()

# Define the Class model
class Class(Base):
    __tablename__ = 'classes'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    students = relationship("Student", back_populates="class_")

    def __repr__(self):
        return f"<Class(id={self.id}, name='{self.name}')>"

# Define the Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    roll_number = Column(Integer, nullable=False)
    grade = Column(Float, nullable=False)
    class_id = Column(Integer, ForeignKey('classes.id'))
    class_ = relationship("Class", back_populates="students")

    __table_args__ = (
        UniqueConstraint('roll_number', 'class_id', name='unique_roll_number_per_class'),
    )

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.first_name} {self.last_name}, roll_number={self.roll_number}, grade={self.grade}, class={self.class_.name})>"

# Database setup
def initialize_database(db_path):
    engine = create_engine(f'sqlite:///{db_path}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session

class StudentManagementApp:
    def __init__(self, root, session):
        self.root = root
        self.session = session
        self.root.title("Student Management System")

        self.class_listbox = tk.Listbox(root)
        self.class_listbox.grid(row=0, column=0, rowspan=6, padx=10, pady=10)
        self.class_listbox.bind('<<ListboxSelect>>', self.load_students)

        tk.Button(root, text="Add Class", command=self.add_class).grid(row=6, column=0, pady=5)
        tk.Button(root, text="Delete Class", command=self.delete_class).grid(row=7, column=0, pady=5)

        self.student_listbox = tk.Listbox(root)
        self.student_listbox.grid(row=0, column=1, rowspan=6, padx=10, pady=10)

        tk.Button(root, text="Add Student", command=self.add_student).grid(row=6, column=1, pady=5)
        tk.Button(root, text="Edit Student", command=self.edit_student).grid(row=7, column=1, pady=5)
        tk.Button(root, text="Delete Student", command=self.delete_student).grid(row=8, column=1, pady=5)

        self.load_classes()

    def load_classes(self):
        self.class_listbox.delete(0, tk.END)
        classes = self.session.query(Class).all()
        for cls in classes:
            self.class_listbox.insert(tk.END, cls.name)

    def load_students(self, event):
        selected_class_index = self.class_listbox.curselection()
        if not selected_class_index:
            return

        class_name = self.class_listbox.get(selected_class_index)
        cls = self.session.query(Class).filter_by(name=class_name).first()

        self.student_listbox.delete(0, tk.END)
        for student in cls.students:
            self.student_listbox.insert(tk.END, f"{student.first_name} {student.last_name} (Roll: {student.roll_number})")

    def add_class(self):
        class_name = simpledialog.askstring("Add Class", "Enter class name:")
        if not class_name:
            return

        new_class = Class(name=class_name)
        self.session.add(new_class)
        self.session.commit()
        self.load_classes()

    def delete_class(self):
        selected_class_index = self.class_listbox.curselection()
        if not selected_class_index:
            messagebox.showerror("Error", "No class selected.")
            return

        class_name = self.class_listbox.get(selected_class_index)
        cls = self.session.query(Class).filter_by(name=class_name).first()

        if not cls:
            messagebox.showerror("Error", "Class not found.")
            return

        self.session.delete(cls)
        self.session.commit()
        self.load_classes()
        self.student_listbox.delete(0, tk.END)

    def add_student(self):
        selected_class_index = self.class_listbox.curselection()
        if not selected_class_index:
            messagebox.showerror("Error", "No class selected.")
            return

        class_name = self.class_listbox.get(selected_class_index)
        cls = self.session.query(Class).filter_by(name=class_name).first()

        first_name = simpledialog.askstring("Add Student", "Enter first name:")
        last_name = simpledialog.askstring("Add Student", "Enter last name:")
        roll_number = simpledialog.askinteger("Add Student", "Enter roll number:")
        grade = simpledialog.askfloat("Add Student", "Enter grade:")

        if not (first_name and last_name and roll_number and grade):
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            new_student = Student(first_name=first_name, last_name=last_name, roll_number=roll_number, grade=grade, class_=cls)
            self.session.add(new_student)
            self.session.commit()
            self.load_students(None)
        except Exception as e:
            self.session.rollback()
            messagebox.showerror("Error", f"Failed to add student: {e}")

    def edit_student(self):
        selected_class_index = self.class_listbox.curselection()
        if not selected_class_index:
            messagebox.showerror("Error", "No class selected.")
            return

        selected_student_index = self.student_listbox.curselection()
        if not selected_student_index:
            messagebox.showerror("Error", "No student selected.")
            return

        class_name = self.class_listbox.get(selected_class_index)
        cls = self.session.query(Class).filter_by(name=class_name).first()

        student_info = self.student_listbox.get(selected_student_index)
        roll_number = int(student_info.split("Roll: ")[1][:-1])
        student = self.session.query(Student).filter_by(roll_number=roll_number, class_id=cls.id).first()

        if not student:
            messagebox.showerror("Error", "Student not found.")
            return

        first_name = simpledialog.askstring("Edit Student", "Enter first name:", initialvalue=student.first_name)
        last_name = simpledialog.askstring("Edit Student", "Enter last name:", initialvalue=student.last_name)
        grade = simpledialog.askfloat("Edit Student", "Enter grade:", initialvalue=student.grade)

        if not (first_name and last_name and grade):
            messagebox.showerror("Error", "All fields are required.")
            return

        student.first_name = first_name
        student.last_name = last_name
        student.grade = grade

        self.session.commit()
        self.load_students(None)

    def delete_student(self):
        selected_student_index = self.student_listbox.curselection()
        if not selected_student_index:
            messagebox.showerror("Error", "No student selected.")
            return

        student_info = self.student_listbox.get(selected_student_index)
        roll_number = int(student_info.split("Roll: ")[1][:-1])
        selected_class_index = self.class_listbox.curselection()
        class_name = self.class_listbox.get(selected_class_index)
        cls = self.session.query(Class).filter_by(name=class_name).first()

        student = self.session.query(Student).filter_by(roll_number=roll_number, class_id=cls.id).first()

        if not student:
            messagebox.showerror("Error", "Student not found.")
            return

        self.session.delete(student)
        self.session.commit()
        self.load_students(None)

if __name__ == "__main__":
    db_path = input("Enter the database file name (it will be created if it doesn't exist): ")
    session_maker = initialize_database(db_path)
    session = session_maker()

    root = tk.Tk()
    app = StudentManagementApp(root, session)
    root.mainloop()
