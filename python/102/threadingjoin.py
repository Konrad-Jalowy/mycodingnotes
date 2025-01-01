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
