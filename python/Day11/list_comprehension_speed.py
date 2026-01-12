

nums = list(range(1000000))

squares_map = list(map(lambda x: x * x, nums)) # map + lambda

squares_comp = [x * x for x in nums] # list comprehension mostly preferred as they avoid the overhead of calling a python function frame for every single item.
