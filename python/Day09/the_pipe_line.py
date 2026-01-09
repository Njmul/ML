

def square(n):
        for x in n:
            yield x*x



def filter(n):     
      for x in n:
            if x %2 == 0:
                yield x
            
n = range(1,10)
data_pipeline = filter(square(n))

print(list(data_pipeline))