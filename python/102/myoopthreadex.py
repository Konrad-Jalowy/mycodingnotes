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