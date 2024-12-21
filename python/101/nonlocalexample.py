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