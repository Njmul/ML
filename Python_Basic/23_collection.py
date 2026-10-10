

# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates ok
# Set = {} unordered and immutable, but Add/Remove ok. Not duplicates
# Tuple = () ordered and unchangeable. Duplicates ok. Faster




# List
fruits =  ["apple", "orange", "banana", "coconut"]

# print(dir(fruits))

# print(help(fruits))

# print("banana" in fruits)

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("apple"))

# print(fruits[0:3])

# for fruit in fruits:
#     print(fruit)


# Set
fruits = {"apple", "orange", "banana", "coconut"}

# print(dir(fruits))

# print(help(fruits))

# print("banana" in fruits)

# fruits.add("pineapple")

# fruits.remove("apple")
# fruits.pop()
# fruits.clear()


# Tuple
fruits = ("apple", "orange", "banana", "coconut")
# print(dir(fruits))

# print(help(fruits))

# print("banana" in fruits)

# fruits.add("pineapple")
#fruits.count("coconuts")

# for fruit in fruits:
#     print(fruit)