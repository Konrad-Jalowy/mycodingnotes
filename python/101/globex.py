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