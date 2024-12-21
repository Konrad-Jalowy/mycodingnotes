# Python weird parts
I post weird Python stuff here.

## True + True
Looks like True is just an alias for 1:
```python
print(True + True) #2
```

## True, False
Yes, they are just aliases for 1 and 0 and we can check that
```python
print(10/True) #10.0
print(10-True) #9
print(10-False) #10
print(10/False) #Zero division error
```