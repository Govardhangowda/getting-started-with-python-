def allow_only(func):
    def wrapper(name):
        func(name) 
        if name=='admin':
            print("Access granted")
        else:
            print("Access denied")
    return wrapper

@allow_only
def access_control(name):
    print(f"User: {name}")

access_control(input("Enter your name: "))
