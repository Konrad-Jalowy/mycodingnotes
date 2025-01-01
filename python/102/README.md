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