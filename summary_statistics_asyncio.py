
import asyncio
import time
import numpy as np
from math import sqrt

async def calculate_number_observation(one_dimensional_array):    
    print('start calculate_number_observation() procedure')   
    await asyncio.sleep(0)
    number_observation = one_dimensional_array.size
    print("Number of Observation: {} ".format(number_observation))    
    await calcuate_arithmetic_mean(one_dimensional_array, number_observation)
#     await calculate_median(one_dimensional_array, number_observation)
    print("finished calculate_number_observation() procedure")   
    
async def calcuate_arithmetic_mean(one_dimensional_array, number_observation):    
    print('start calcuate_arithmetic_mean() procedure')   
    await calculate_median(one_dimensional_array, number_observation)
    sum_result = 0.0
    await asyncio.sleep(0)
    for i in range(number_observation):       
        sum_result += one_dimensional_array[i]    
    arithmetic_mean = sum_result / number_observation
    print("Arithmetic Mean: {} ".format(arithmetic_mean))    
    await calculate_sample_standard_deviation(one_dimensional_array, number_observation, arithmetic_mean)
    print("finished calcuate_arithmetic_mean() procedure")   
    
async def calculate_median(one_dimensional_array, number_observation):      
    print('starting calculate_median()')   
    await asyncio.sleep(0)
    one_dimensional_array.sort()    
    half_position = number_observation // 2
    if not number_observation % 2:
        median = (one_dimensional_array[half_position - 1] + one_dimensional_array[half_position]) / 2.0
    else:
        median = one_dimensional_array[half_position]        
    print("Median: {} ".format(median))
    print("finished calculate_median() procedure")   

async def calculate_sample_standard_deviation(one_dimensional_array, number_observation, arithmetic_mean):    
    print('start calculate_sample_standard_deviation() procedure')   
    await asyncio.sleep(0)
    sum_result = 0.0
    for i in range(number_observation):                   
        sum_result += pow((one_dimensional_array[i] - arithmetic_mean), 2)            
    sample_variance = sum_result / (number_observation - 1)            
    sample_standard_deviation = sqrt(sample_variance)        
    print("Sample Standard Deviation: {} ".format(sample_standard_deviation))
    print("finished calculate_sample_standard_deviation() procedure")   
    
def main(one_dimensional_array):    
    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(calculate_number_observation(one_dimensional_array))]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()
      
if __name__ == '__main__':
    start_time = time.clock()  
    one_dimensional_array = np.arange(1000000, dtype=np.float64)        
    main(one_dimensional_array)
    end_time = time.clock()
    print("Program Runtime: {} seconds".format(round(end_time - start_time, 1)))

    