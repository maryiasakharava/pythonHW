import time
from functools import wraps

def calculate_time(func):
    @wraps(func)
    def calculate_time_wrapper(*args, **kwargs):
        starting = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        total = end - starting
        print(f'Total time {total:.4f}')
        return result
    return calculate_time_wrapper
