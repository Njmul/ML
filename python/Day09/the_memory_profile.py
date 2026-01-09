import sys
list_comp = [i for i in range(1000000)]
gen_exp = (i for i in range(1000000))

print(f"List comprehension size: {sys.getsizeof(list_comp)} bytes")
print(f"Generator expression size: {sys.getsizeof(gen_exp)} bytes")


# Use a list if you need to access items multiple times, sort them, or jump around (index) data data.
# Use a generator if you are just iterating through the data once (e.g summing number, writing to a file, or filtering data)
