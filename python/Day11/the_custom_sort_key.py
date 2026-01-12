

data = ["100px", "20px", "3px"]

sorted_data = sorted(data, key=lambda x: int(x[:-2]))
print(sorted_data)  
