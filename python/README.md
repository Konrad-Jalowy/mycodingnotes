# Python
Some Python notes

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
