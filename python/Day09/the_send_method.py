def accumulator():
    total = 0
    while True:
        x = yield total         
        if x is not None:
            total += x

generator = accumulator()

print(next(generator))        
print(generator.send(43))    
print(generator.send(28))    
print(generator.send(None)) 
