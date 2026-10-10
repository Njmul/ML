

# Membership operator = used to test whether a value or variable is found in a sequence
# (string, list, tuple, set, or dictionary)
# 1. in
# 2. not in

# Example 1
word = "APPLE"

letter = input("Guess a letter in teh secret word: ")

if letter not in word:
    print(f"{letter} was not found")
else:
    print(F"There is a {letter}")


# Example 2
email = "BroCode@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")


# List comprehension = A concise way to create lists in Python 
    # Compact and easier to read than traditional loops 
    # [expression for value in iterable condition]



# Example 1
doubles =[]
for x in range(1, 11):
    doubles.append(x*2)
print(doubles)



# Example 2, List Comprehension

doubles = [x*2 for x in range(1, 11)]
print(doubles)


# Example 3, List Comprehension

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(doubles)
print(triples)
print(squares)


# Example 4, List Comprehension

fruits = ["apple", "orange", "banana", "coconut"]

fruits = [fruit.upper() for fruit in fruits]
print(fruits)

# Example 4, List Comprehension

fruits = ["apple", "orange", "banana", "coconut"]

fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]
print(fruits)


# Example 5, List Comprehension

fruits = ["apple", "orange", "banana", "coconut"]

fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)


# Example 6, List Comprehension


numbers = [1, -2, 3, 4, 5, 6]
    # [expression for value in iterable condition]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]


print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)





# Example 7, List Comprehension

grades = [86, 42, 79, 76, 98, 54]
positive_grades = [grade for grade in grades if grade >= 60]

print(positive_grades)