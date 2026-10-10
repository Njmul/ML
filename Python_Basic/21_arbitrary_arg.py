
# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#              1. positional 2. default 3. keyword 4. arbitrary


# Only two parameters
# def add(a, b):
#     return a + b


# print(add(1, 2))


# More then two parameters and *args works as tuple
def add(*args): # * is an unpacking operator
    total = 0
    for arg in args:
        total += arg


    return total


print(add(1, 2, 3, 4, 5))



# **kwargs works as a dictionary

def print_address(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(street = "123",
      city= "Detroit",
      state="MI",
      zip="3456")

# *args and **kwargs together

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end= " ")
    print()
    for value in kwargs.values():
        print(value, end= " ")    

shipping_label("Dr", "Spongebob", "Square", "III",
               street = "123 Fake st",
               apt = "100",
               city = "Detroit",
               state = "Mi",
               zip = "2345")

# Another way of representation:

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end= " ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.ge('street')} {kwargs.ge('apt')}")
    else:
        print(f"{kwargs.ge('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr", "Spongebob", "Square", "III",
               street = "123 Fake st",
               apt = "#100",
               city = "Detroit",
               state = "Mi",
               zip = "2345")