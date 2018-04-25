
from threading import Thread
import time

def print_thread(i):
    print("sleeping 15 sec from thread %d" % i)
    print()
    time.sleep(15)
    print("finished sleeping from thread %d" % i)
    print()
      
def main():
    try:
        for i in range(10):
            thread = Thread(target=print_thread, args=(i,))
            thread.start()
    except:
        print("An error occurred: unable to start thread.")

if __name__ == '__main__':
    main()