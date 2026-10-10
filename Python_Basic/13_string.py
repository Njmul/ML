# you can use help() to know any function in details
#    print(help(str))

name = input("Enter your full name: ")


result = len(name)
print(result)


result = name.find(" ") # find the index of the space
print(result)


result = name.rfind(" ") # find the index of the space from reverse
print(result)

name = name.capitalize()
print(name)

name = name.upper()
print(name)

name = name.lower()
print(name)

result = name.isdigit() # boolean output, True only all are digits
print(result)


result = name.isalpha() # boolean output, True only contain alphabatic character
print(result)


phone_number = 293-3443-24432
result = phone_number.count("-")
print(result)


result = phone_number.replace("-", "")
print(result)


