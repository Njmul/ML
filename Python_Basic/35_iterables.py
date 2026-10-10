

# Iterables = An object/ collection that can return its elements one at a time,
#     
#           allowing it to be iterated over in a loop


# List
number = [1, 2, 3, 4, 5]

for number in numbers:
    print(number) 

for number in reversed(numbers):
    print(number, end=" - ")

# Tuple
number = (1, 2, 3, 4, 5)

for number in numbers:
    print(number, end=" - ") 

# Sets , not reverse
    
fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit)

name = "Bro Code"

for character in name:
    print(character, end=" ")

#Dictionary
    
my_dictionary = {"A": 1, "B": 2, "C": 3}

for key, value in my_dictionary.values():
    print(f"{key} = {value}")

