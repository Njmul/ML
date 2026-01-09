



def running_average():
    total = 0.0
    count = 0

    while True:
        x = yield (total / count) if count else 0.0
        if x is not None:
            total += x
            count += 1
avg = running_average()
print(next(avg))        
print(avg.send(23))     
print(avg.send(45))     

