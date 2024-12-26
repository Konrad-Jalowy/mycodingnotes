# Python 101
Python basics

## Not implemented function
Tbh i didnt know there are so many ways, i usually return "not implemented", but hey:
```python
def myway():
    return "not implemented yet"

def pythonway():
    pass

def anotherway():
    ...
```
## Division
There are two types of division
```python
num1 = 5
num2 = 2
print(num1 / num2) #2.5
print(num1 // num2) #2
```

## Global keyword
Self explanatory, heres the code
```python
num = 1

def no_global():
    num = 2
    print("No global running, num is ", num)

def with_global():
    global num
    num = 3
    print("Global running, num is ", num)

no_global() # No global running, num is  2
with_global() # Global running, num is  3
print(num) # 3
```
## Nonlocal keyword
Self explanatory, but in Python even simple things sometimes feel kinda out of place, off. So i always double check if it works as i think it should, heres the code
```python
def create_counter():
    count = 0
    def counter():
        nonlocal count # Access the variable from the parent function scope
        count += 1
        return count
    return counter

counter1 = create_counter()
print(counter1()) #1
print(counter1()) #2
print(counter1()) #3

counter2 = create_counter()
print(counter2()) #1
print(counter2()) #2
print(counter2()) #3
```

## How to create venv without PyCharm
I tend to forget that.  
First command:
```sh
python -m virtualenv venv
```
Venv is the name, it can be anything.  
Then we activate it:
```sh
venv\Scripts\activate 
```
To deactivate, simply use
```sh
deactivate
```

## __name__ main
Ok heres the code
```python
def hello():
    print("Hello World")

if __name__ == "__main__":
    hello()
```
You do that so that nothing in that guard will run if the script is imported


## write to file (overwrites)
Very simple write to file (if not exists then creates, if exists, overwrites)
```python
fh = open("test.txt", "w")
fh.write("hello world")
fh.close()
```

## append to file
Very simple:
```python
fh = open("test.txt", "a")
fh.write("hello world 2")
fh.close()
```

## paths
self-explanatory:
```python
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()

print(__file__) #file path
print(dir_path) #file directory path
print(cwd) # path from which we run the python command 
```

## files in correct place
always make sure they are created in correct place regardless of place that runs the command
```python
import os
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.txt")
print(path)

fh = open(path, "w")
fh.write("hello world 1")
fh.write("hello world 2")
fh.close()

fh = open(path, "a")
fh.write("hello world 3")
fh.close()
```

## reading from a file
code:
```python
import os
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.txt")
print(path)

fh = open(path, "r")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line.rstrip("\n"))
```

## how to list files in dir
**note you can use more powerful methods such as walk...**
```python
import os

main_directory = os.path.dirname(os.path.realpath(__file__))
files_and_folders = os.listdir(main_directory)

for _file in files_and_folders:
    _path = os.path.join(main_directory, _file)
    if os.path.isfile(_path):
        print(_file)
```

## Writing to file with proper encoding
encoding UTF-8 default is ascii i guess, anyways default is not enough for all characters
```python
import os
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test2.txt")
print(path)

fh = open(path, "w", encoding="utf-8")
fh.write("hello world ąęśćżczź")
fh.close()
```

## While reading file encoding is also important
using default works only for ASCII i guess, i checked and utf-8 is not default (idk why).
```python
import os
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test2.txt")
print(path)

fh = open(path, "r", encoding="utf-8")
lines = fh.readlines()
fh.close()

for line in lines:
    print(line.rstrip("\n"))
```

## reading file line by line
```python
import os
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.txt")
print(path)

fh = open(path, "r", encoding="utf-8")

while True:
    line = fh.readline()
    if not line:
        break
    print(line, end="")

fh.close()
```

## walrus, while-else, readline
- walrus - assign in condition/assignment for later use
- while-else - else block works when no breaks occurred (thats why we need walrus)
- readline - read line by line from file handle
```python
import os
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test.txt")
print(path)

fh = open(path, "r", encoding="utf-8")

while line := fh.readline():
    print(line, end="")
else:
    print()
    print("Finished reading")

fh.close()
```

## Walrus example
Btw answers are stored in set literal (not a dictionary its set literal in Python)
```python
question = "Do you use the walrus operator?"
valid_answers = {"yes", "Yes", "y", "Y", "no", "No", "n", "N"}

while (user_answer := input(f"\n{question} ")) not in valid_answers:
    print(f"Please answer one of {', '.join(valid_answers)}")
```

## Walrus useful example
And here youve got dictionary literal (as opposed to set literal in prev ex)
```python
numbers = [2, 8, 0, 1, 1, 9, 7, 7]

description = {
"length": (num_length := len(numbers)),
"sum": (num_sum := sum(numbers)),
"mean": num_sum / num_length,
}

print(description)
```

## chr ord
- **ord(letter)** - letter to number
- **chr(num)** - number to letter
```python
msg = "hello world"
msg_numbers = []
msg_again = ""

for letter in msg:
    print(ord(letter))
    msg_numbers.append(ord(letter))
else:
    print(msg_numbers)

for letter in msg_numbers:
    print(chr(letter))
    msg_again += chr(letter)
else:
    print(msg_again)
```

## list comprehension
usually theres no point in using map/filter in Python unless you cannot get this done using list comprehension.  
example:
```python
msg = "hello world"
msg_numbers = [ord(letter) for letter in msg]
print(msg_numbers)
#[104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]
```

## another walrus example
idk if a good one, but you can do that:
```python
msg = "hello world! hi!"
results = [value for char in msg if (value := ord(char)) >= 97 and value <= 122]
print(results)
```

## args
filename is first arg
```python
import sys
print("Number of arguments: ", len(sys.argv))
print("Arguments list: ", sys.argv)
```
## download website and save
```python
#pip install requests
import requests

url = "https://www.google.com"
response = requests.get(url, allow_redirects=True)

if response.ok:
    fh = open("myfile.html", "wb")
    fh.write(response.content)
    fh.close()
```

## validators in python
```python
# pip install validators
import validators

print(validators.url("http://www.google.com")) #True
flag = validators.url("www.google.com")
print(flag) #ValidationError(func=url, args={'value': 'www.google.com'})
print(validators.email('someone@example.com')) #True
```

## simple argparse use
```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", action="store")

args = parser.parse_args()

print(args.url)
```