#add extra functionality to the existing function
# we can use it in logging or in authentication purpose

import inspect

def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("after calling the function")
    return wrapper


@decorator
def greet():
    print("hello kshit")
greet()

print(inspect.signature(decorator))