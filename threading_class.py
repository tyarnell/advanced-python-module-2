
from threading import Thread
import time

exit_flag = 0

class myThread (Thread):
   
    def __init__(self, thread_id, thread_name, counter):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.counter = counter

    def run(self):
        print("Starting " + self.thread_name)
        self.print_time(self.thread_name, 5, self.counter)
        print("Exiting " + self.thread_name)

    def print_time(self, thread_name, counter, delay):
        while counter:
            if exit_flag:
                thread_name.exit()
            time.sleep(delay)
            print('%s: %s' % (thread_name, time.ctime(time.time())))
            counter -= 1

if __name__ == '__main__':

    thread1 = myThread(1, 'Thread-1', 1)
    thread2 = myThread(2, 'Thread-2', 2)
    thread3 = myThread(3, 'Thread-3', 3)
    thread4 = myThread(4, 'Thread-4', 4)
    thread5 = myThread(5, 'Thread-5', 5)
    thread6 = myThread(6, 'Thread-6', 6)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    
    print('Exiting main thread...')