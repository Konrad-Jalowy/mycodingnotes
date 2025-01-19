import os
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# Define the Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    roll_number = Column(Integer, unique=True, nullable=False)
    grade = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.first_name} {self.last_name}, roll_number={self.roll_number}, grade={self.grade})>"

# Database setup
def initialize_database(db_path):
    engine = create_engine(f'sqlite:///{db_path}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session

def main_menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Edit Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_student(session):
    print("\nAdd a New Student")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    roll_number = int(input("Roll Number: "))
    grade = float(input("Grade: "))

    student = Student(first_name=first_name, last_name=last_name, roll_number=roll_number, grade=grade)
    session.add(student)
    session.commit()
    print("Student added successfully!")

def view_students(session):
    print("\nList of Students")
    students = session.query(Student).all()
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(student)

def edit_student(session):
    print("\nEdit a Student")
    roll_number = int(input("Enter the roll number of the student to edit: "))
    student = session.query(Student).filter_by(roll_number=roll_number).first()

    if not student:
        print("Student not found.")
        return

    print("Editing Student:", student)
    student.first_name = input(f"First Name ({student.first_name}): ") or student.first_name
    student.last_name = input(f"Last Name ({student.last_name}): ") or student.last_name
    student.grade = float(input(f"Grade ({student.grade}): ") or student.grade)

    session.commit()
    print("Student updated successfully!")

def delete_student(session):
    print("\nDelete a Student")
    roll_number = int(input("Enter the roll number of the student to delete: "))
    student = session.query(Student).filter_by(roll_number=roll_number).first()

    if not student:
        print("Student not found.")
        return

    session.delete(student)
    session.commit()
    print("Student deleted successfully!")

def main():
    db_path = input("Enter the database file name (it will be created if it doesn't exist): ")
    session_maker = initialize_database(db_path)
    session = session_maker()

    while True:
        choice = main_menu()
        if choice == "1":
            add_student(session)
        elif choice == "2":
            view_students(session)
        elif choice == "3":
            edit_student(session)
        elif choice == "4":
            delete_student(session)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
