


# function = A block of reusable code
#   place () after the function name to invoke it.

#Example 1

# def happy_birthday():
#     print("Happy Birthday to You!")

# for x in range(3):
#     happy_birthday()



#Example 2

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")


# display_invoice("Joe Smith", 100.23, "01/03")




#Example 3
# return = statement used to end a function 
# and send a result back to the caller


# def add(x, y):
#     z = x + y
#     return z
    
# print(add(3, 1))


# def subtract(x, y):
#     z = x - y
#     return z
    
# print(subtract(3, 1))

# def multiply(x, y):
#     z = x * y
#     return z
    
# print(multiply(3, 1))


# def divide(x, y):
#     z = x / y
#     return z
    
# print(divide(3, 1))




#Example 4

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + "  " + last


full_name = create_name("rubina", "farhana")

print(full_name)


