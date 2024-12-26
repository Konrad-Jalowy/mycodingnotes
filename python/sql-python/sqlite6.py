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

people_3 = curr.fetchmany(3)
print(len(people_3)) #3
print(people_3[0]) #(1, 'Jane', 'Doe', 20)