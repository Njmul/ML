

# module = a file containing code you want to include in your program
#           use "import" to include a module (built in or your own)
#           useful to break up a large program reusable separate files



# import math

# import math as m
from math import e
a, b, c = 1, 2, 3

print(e ** a)
print(e ** b)
print(e ** c)


# print(help("modules"))


# How to make and use a module

#example.py

pi = 3.1416

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * pi * radius
def area(radius):
    return pi ** 2

# main.py


import example

result = example.pi
result = example.square(3)
result = example.cube(3)
result = example.circumference(3)
result = example.area(3)

print(result)