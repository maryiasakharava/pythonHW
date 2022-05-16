from time import time
from functools import wraps
from time import process_time

  
def calculate_time(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start = int(round(process_time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(process_time() * 1000)) - start
            print(
                f"Total time {end_ if end_ > 0 else 0}"
            )

    return timeit_wrapper
   

