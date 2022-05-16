from functools import wraps
from time import time
def calculate_time(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        starttime = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - starttime
            print(f"Total execution time: {end_ if end_ > 0 else 0} ms")
    return calcualte_time


