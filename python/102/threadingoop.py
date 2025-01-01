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