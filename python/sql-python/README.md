# sql-python
notes on python and sql

## sqlite connect
```python
import sqlite3
import os

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

db_name = "mydb1.db"
conn = sqlite3.connect(db_name)
```

## sqlite cursor, create table (if not exists)
basics of sqlite
```python
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
```

## inserting with auto incrementing id
remember, pass null to id. also, curr.execute returns cursor object.
```python
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
```

## always remember to commit
always remember about calling commit
```python
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
```

## sqlite fetchone
```python
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
```

## sqlite fetchmany
```python
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
```

## sqlite fetchall
```python
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

people = curr.fetchall()

for person in people:
    print(person)

# (1, 'Jane', 'Doe', 20)
# (2, 'Jim', 'Doe', 25)
# (3, 'John', 'Doe', 35)
```