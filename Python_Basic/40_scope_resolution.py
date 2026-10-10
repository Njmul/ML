

# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Local Variable
def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()

# Enclosed variable

def func1(): # enclosed variable x = 1
    x = 1
    
    def func2(): # local variable x = 2
        x = 2
        print(x)
    func2()

# local first then enclosed
func1()



# Global Variable
def func1():
    print(x)

def func2():

    print(x)

x = 3
func1()
func2()

# Built in variables

from math import e

def func1():
    print(e)

e = 3
func1() # Global variable will be shown