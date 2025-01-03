# Python 102
More advanced Python notes

## Simple thread
```python
import _thread, time

def printTime( threadName, sleepTime ):
    num = 0
    max = 6
    while num < max:
        localTime = time.localtime()

        print(threadName, time.strftime( "%H %M %S" ,localTime))
        time.sleep( sleepTime )

        num += 1
    print(threadName, " ended")

_thread.start_new_thread( printTime, ("thread 1", 0.5) )
_thread.start_new_thread( printTime, ("THREAD 2", 0.3) )

time.sleep(4)
```

## Threading - join
threading returns thread object, lets you use join to wait for finish and so on...
```python
import threading, time

def printTime( threadName, sleepTime ):
    num = 0
    max = 6
    while num < max:
        localTime = time.localtime()

        print(threadName, time.strftime( "%H %M %S" ,localTime))
        time.sleep( sleepTime )

        num += 1
    print(threadName, " ended")

t1 = threading.Thread( target = printTime, args = ("thread 1", 0.5) )
t2 = threading.Thread( target = printTime, args = ("THREAD 2", 0.2) )
t3 = threading.Thread( target = printTime, args = ("T3", 0.4) )

t1.start()
t2.start()
t3.start()

t1.join()
print("T1 ended for main thread")
t2.join()
print("T2 ended for main thread")
t3.join()
print("T3 ended for main thread")

print("Threads ended")
```
## Threading - OOP
Example how to do that
```python
import threading, time

class someThread(threading.Thread):
    def __init__(self, threadName, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.sleepTime = sleepTime

    def run(self):
        num = 0
        max = 6
        while num < max:
            localTime = time.localtime()

            print(self.threadName, time.strftime( "%H %M %S" ,localTime))
            time.sleep( self.sleepTime )

            num += 1
        print(self.threadName, " ended")


t1 = someThread("T1", 0.1)
t2 = someThread("THREAD 2", 0.3)
t3 = someThread("thread 3", 0.4)

t1.start()
t2.start()
t3.start()

time.sleep(1)
print( "-- Thread 2 status: ", t2.is_alive() )

t1.join()
t2.join()
t3.join()

print("All threads ended")
```

## Lock example
Example of lock i found. Here
- Lock - global object to stop/start threads using it
- lock.aquire() - all threads using this lock will wait till this thread uses release
- lock.release() - thread released
```python
import threading, time

data = ["Adam", "Ola", "Kasia", "Daniel", "Rafał"]
dataLock = threading.Lock()

class someThread(threading.Thread):
    def __init__(self, threadName, dataLen, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.dataLen = dataLen
        self.sleepTime = sleepTime

    def run(self):
        num = 0
        while num < self.dataLen:

            dataLock.acquire()
            data[num] = data[num] + " " + str(num)
            print( self.threadName, data[num] )
            dataLock.release()

            time.sleep( self.sleepTime )

            num += 1
        print(self.threadName, " ended")


t1 = someThread("T1", len(data) , 0.1)
t2 = someThread("THREAD 2", len(data) , 0.3)
t3 = someThread("thread 3", len(data) , 0.4)

t1.start()
t2.start()
t3.start()

time.sleep(1)
print( "-- Thread 2 status: ", t2.is_alive() )

t1.join()
t2.join()
t3.join()

print("All threads ended")
```

## My example of OOP threads
watch out not to overwrite some important variables of thread class
```python
import threading


class someThread(threading.Thread):
    def __init__(self, start, stop):
        threading.Thread.__init__(self)
        self._startVal = start
        self._stopVal = stop

    def run(self):
        while self._startVal < self._stopVal:
            print(self._startVal)
            self._startVal +=1


t1 = someThread(1,10)
t2 = someThread(1,5)
t3 = someThread(10,20)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All threads ended")
```

## My OOP example of lock, aquire, release
```python
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
```

## Decorator example 1
```python
def starDecorator(func):
    def wrap_func():
        print("************")
        func()
        print("************")
    return wrap_func

@starDecorator
def say_hello():
    print("hello")

say_hello()
```

## Decorator for funcs with arguments
```python
def starDecorator(func):
    def wrap_func(*args, **kwargs):
        print("************")
        func(*args, **kwargs)
        print("************")
    return wrap_func

@starDecorator
def say_hello(name):
    print("hello " + name)

say_hello("john")
say_hello("jane")
```