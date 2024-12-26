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

curr.execute('''INSERT INTO people VALUES (NULL, 'Jane', 'Doe', '20')''')
curr.execute('''INSERT INTO people VALUES (NULL, 'Jim', 'Doe', '25')''')
curr.execute('''INSERT INTO people VALUES (NULL, 'John', 'Doe', '35')''')

conn.commit()