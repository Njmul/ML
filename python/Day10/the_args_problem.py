def wrapper(func):
    def inner(*args, **kwargs):
        print("Fist")

        result = func(*args, **kwargs)

        print("Third")
        
        return result
    return inner

@wrapper
def add(a, b):
    return a + b

# add(2, 3)
print(add(2, 3))