

def gen():

    yield 1
    yield 2
    yield 3

g = gen()


for i in range(4):
    print(next(g))  # As this loop will run for four times, what is more then number of yield and that will trigger StopIteration.


    