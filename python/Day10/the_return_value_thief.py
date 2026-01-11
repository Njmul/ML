

def wrapper(func):
    def inner(*args, **kwargs):
        print("Fist")

        result = func(*args, **kwargs)

        print("Third")
        
        return result # this line conform the return of the args.
    return inner

@wrapper
def multiply(a, b):
    return a*b

# add(2, 3)
print(multiply(2, 3))