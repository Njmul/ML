import time

def fibonacci():

    a= 0
    b= 1
    while True:
        yield a
        a,b = b, a+b

g = fibonacci()

while True:
    print(next(g))
    time.sleep(0.5)