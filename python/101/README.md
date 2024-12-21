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
