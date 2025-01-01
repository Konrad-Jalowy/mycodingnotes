import threading

data = ["john", "jane", "jim", "janet"]
dataLock = threading.Lock()

class makeUppercase(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        num = 0
        while num < len(data):
            dataLock.acquire()
            name = data[num]
            data[num] = name[0].upper() + name[1:]
            dataLock.release()
            num += 1

class addDoe(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        num = 0
        while num < len(data):
            dataLock.acquire()
            name = data[num]
            data[num] = name + " Doe"
            dataLock.release()
            num += 1


t1 = makeUppercase()
t2 = addDoe()

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads ended")
print(data) #['John Doe', 'Jane Doe', 'Jim Doe', 'Janet Doe']