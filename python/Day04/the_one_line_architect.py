data = list(range(1,11,1))
print(data)

squares = [x**2 for x in data if x%2 ==0]
print(squares)