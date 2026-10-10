

# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#  print or assign one of two based on a condition
#  X if condition else Y

num = 6
a = 6
b = 7
age = 25
temperature = 35



print("Positive" if num > 0 else "Negative") 

result = "Even" if num % 2 == 0 else "Odd"
print(result)

max_num = a if a > b else b
min_num = a if a < b else b
print(min_num)


status = "Adult"  if age >= 18 else "Child"
print(status)

weather = "Hot" if temperature > 20 else "Cold"
print(weather)


