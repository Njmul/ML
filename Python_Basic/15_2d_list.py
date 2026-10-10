

# Different Representation 1

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]


groceries = [fruits, vegetables, meats]

# For access of 2D list you need two dimensional index.
print(groceries[2][2])



# Different Representation 2

# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]


groceries = [["apple", "orange", "banana", "coconut"], 
             ["celery", "carrots", "potatoes"], 
             ["chicken", "fish", "turkey"]]

# fruits[0] = 

# For access of 2D list you need two dimensional index.
print(groceries[2][2])


for collection in groceries:
    for food in collection:
        print(food, end= " ")
    print()



# Different Representation 3
    
groceries = [("apple", "orange", "banana", "coconut"), 
             ("celery", "carrots", "potatoes"), 
             ("chicken", "fish", "turkey")]


# Different Representation 4
groceries = (("apple", "orange", "banana", "coconut"), 
             ("celery", "carrots", "potatoes"), 
             ("chicken", "fish", "turkey"))

# Different Representation 5

num_pad = ((1, 2, 3),
            (4, 5, 6),
            (7, 8, 8),
            ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")

    print()
    

