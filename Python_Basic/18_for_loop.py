

# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.

# Forward counting
for x in range(1, 11):
    print(x)

# Reverse counting
for x in reversed(range(1, 11)):
    print(x)


# Count with 3 interval
for x in range(1, 11, 3):
    print(x)


# Iterate through a sting
credit_card = "1234-2345-3736-3747"   
for x in credit_card:
    print(x)


# Escaping a iteration (13) in a loop
    
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

# Escaping the loop

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)
        

# while loop is used if you want to run 
        #the loop maximum infinite iteration.
        