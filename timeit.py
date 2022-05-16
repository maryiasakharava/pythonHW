from time import time
from time import sleep
from functools import wraps

#function to gerate execution time
def calculate_time(func):
    @wraps(func)
    def _give_time(*args, **kwargs):
        start_time = int((round(time() * 1000)/1000)%60)
        try:
            return func(*args, **kwargs)
        finally:
            end_time = int((round(time() * 1000)/1000)%60)
            execution_time=end_time-start_time
            print(f"EXACTLY  {execution_time if execution_time > 0 else 0} second")
    return _give_time



