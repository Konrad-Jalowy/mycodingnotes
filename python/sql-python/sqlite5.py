import sqlite3
import os

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

db_name = "mydb1.db"
conn = sqlite3.connect(db_name)

curr = conn.cursor()
curr.execute('''CREATE TABLE IF NOT EXISTS people (
                id integer primary key autoincrement,
                first text,
                last text,
                age integer)''')

curr.execute("SELECT * FROM people")

one = curr.fetchone()
two = curr.fetchone()
three = curr.fetchone()
_ = curr.fetchone()

print(one) #(1, 'Jane', 'Doe', 20)
print(two) #(2, 'Jim', 'Doe', 25)
print(three) #(3, 'John', 'Doe', 35)
print(_) #None