

def cache(func):
    memo = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in memo:
            return memo[key]
        result = func(*args, **kwargs)
        memo[key] = result
        return result
    return wrapper

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(4))  # fast because of caching

