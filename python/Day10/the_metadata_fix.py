from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def multiply(a, b):

    return a*b

print(multiply.__name__)
print(multiply.__doc__)


