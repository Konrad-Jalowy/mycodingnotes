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