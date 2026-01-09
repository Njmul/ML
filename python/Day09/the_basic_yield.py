

def get():

    for i in range(5):
        print("First Time")
        yield
        print("Second Time")
        yield
        print("Third TIme")

get()
