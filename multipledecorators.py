def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("===")
        func(*args, **kwargs)
        print("===")
    return wrapper

def decorator_two(func):
    def wrapper(*args,**kwargs):
        print(">>>")
        func(*args, **kwargs)
    return wrapper
@decorator_two
@decorator_one
def namecall():
    name=input("Enter your name: ")
    print(f"Hello {name}!")

namecall()