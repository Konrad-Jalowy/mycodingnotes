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

mr_dict =  {"first": "Jim", "last": "Dictlike", "age": 22}
curr.execute("INSERT INTO people VALUES(NULL, :first, :last, :age)", mr_dict )
conn.commit()