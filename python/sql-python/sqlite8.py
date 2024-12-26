import sqlite3
import os
from collections import namedtuple

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

people = curr.fetchall()
Person = namedtuple('Person', 'id first last age')

for _person in people:
    person = Person(*_person)
    print(person.id, person.first, person.last, person.age)

# 1 Jane Doe 20
# 2 Jim Doe 25
# 3 John Doe 35
