import time
def runtime(func):
    def wrapper(*args, **kwargs):
        start_time=time.perf_counter()
        result = func(*args, **kwargs)
        end_time=time.perf_counter()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@runtime
def example_function(n):
    time.sleep(2)
    total = 0
    for i in range(n):
        total += i
    return total

print(example_function(1000000))