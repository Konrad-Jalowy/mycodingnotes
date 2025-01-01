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