from functools import wraps

def repeat(times=3):  #Factory: accepts `times`
    def decorator(func): #Decorator: accepts `func`
        @wraps(func)
        def wrapper(*args, **kwargs): #Wrapper: accepts args/kwargs
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result  # return the last call's result
        return wrapper
    return decorator

@repeat(times=3)
def say(msg):
    print(msg)
    return len(msg)

print("Returned:", say("Hi"))
