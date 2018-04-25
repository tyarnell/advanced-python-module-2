# Hi Yeray!
# 
# This is a very good tutorial. I think, one of the best in asyncio that I know. I have a simple question for you. I would like to control the tasks schedule. For example, I have task1, task2, task3, task4 and task5. Below is the schedule I want:
# 
# Task1 will run independence
# Task2 needs to be run after task1 is complete finish
# Task3 needs to be run after task2 is complete finish
# Taks4 needs to be run after task1 and task3 finish
# Task5 needs to be run independence
# 
# In the sample code you provided, what example is the best to use. Or, do we need other different code for it!
# 
# Thank you for your time,

# How the heck does async/await work in Python 3.5?
# https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/

import asyncio

"""
Task1 will run independence
Task2 will run independence
Task3 will run independence
Taks4 will run independence
Task5 will run independence
"""

async def task1():
    print('Running Task1')
    await  asyncio.sleep(0)  
    print('>> Task1 done!')

async def task2():
    print('Running Task2')
    await asyncio.sleep(2)   
    print('>> Task2 done!')

async def task3():
    print('Running Task3')
    await asyncio.sleep(6)
    print('>> Task3 done!')
    
async def task4():
    print('Running Task4')
    await asyncio.sleep(1)
    print('>> Task4 done!')
    
async def task5():
    print('Running Task5')
    await asyncio.sleep(3)
    print('>> Task5 done!')

if __name__ == '__main__':
    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(task1()), 
             ioloop.create_task(task2()), 
             ioloop.create_task(task3()), 
             ioloop.create_task(task4()), 
             ioloop.create_task(task5())]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()