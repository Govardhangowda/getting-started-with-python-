
from datetime import datetime
def log_function_call(func):
    def wrapper(a, b):
        print(f"calling {func.__name__}()")
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Time: {time}")
        return func(a, b)
    return wrapper

@log_function_call
def add(a,b):
    return a + b

print(add(2, 3))