from time import time
from time import sleep
from time import perf_counter

  
def calculate_time(func):
    def inner(*args, **kwargs):
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print('Total time '+ execution_time)
        return to_execute
    return inner
   

