

def generator_a():
    for x in [23, 67, 98]:
        yield x

def generator_b():
    for y in [45, 83, 74]:
        yield y

def combined():
    yield from generator_a()
    yield from generator_b()

print(list(combined()))
