a = [1,2,3,4,5]

b=a.copy() #In Python, lists are mutable. This means that after a list has been created, you can change its contents—add, remove, or modify elements—without creating a new list object in memory [1]. 
b[0]=99 # Changing the first value of b.
print(b)
print(a)
