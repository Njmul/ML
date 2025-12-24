initial_string = "n"*10000 # initializing a string with n value

insert = "xy"
pos = 2345
new_string = insert.join([initial_string[:pos],initial_string[pos:]])
  
print(new_string[pos:pos+len(insert)])