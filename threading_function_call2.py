
from threading import Thread
import time

def task_1():
    print("task_1 - start")
    time.sleep(5)
    print("task_1 - finish")

def task_2():
    print("task_2 - start")
    time.sleep(10)
    print("task_2 - finish")

def task_3():
    print("task_3 - start")
    time.sleep(5)
    print("task_3 - finish")
    
        
def loop1_10():
    for i in range(1, 11):
        time.sleep(1)
        print(i)
        
def main1():
    my_thead = Thread(target=loop1_10)
    my_thead.start()
    
def main2():
    thead1 = Thread(target=task_1).start()
    thead2 = Thread(target=task_2).start()
    thead3 = Thread(target=task_3).start()
    
if __name__ == '__main__':
#     main1()
    main2()