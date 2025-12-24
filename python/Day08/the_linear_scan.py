
data= list(range(10))
# data[1] = -5

for i in range(len(data)):
  
    if data[i]== -5:
        print("Your data is found!")
        break
    else:
        print("Your data is not found!")
