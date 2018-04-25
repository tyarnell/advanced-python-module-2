
import time
import numpy as np
from class_summary_statistics_asyncio import SummaryStatisticsAsyncio

def main(one_dimensional_array):
    
#     create summary statistics asyncio class object
    summary_statistics_asyncio = SummaryStatisticsAsyncio()

#     call main function
    summary_statistics_asyncio.main(one_dimensional_array)

if __name__ == '__main__':
    start_time = time.time()  
    one_dimensional_array = np.arange(1000000, dtype=np.float)        
    main(one_dimensional_array)
    end_time = time.time()
    print("Program Runtime: {} seconds".format(round(end_time - start_time, 1)))
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                     
                                                    