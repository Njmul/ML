
import time


def wrapper(func):
    def inner(*args, **kwargs):
        print("Fist")

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"{func.__name__} took {(end - start):.6f} seconds")
        
        return result 
    return inner

@wrapper
def multiply(a, b):
    time.sleep(0.5)
    return a*b

# add(2, 3)
print(multiply(2, 3))