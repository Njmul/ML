

def wrapper(function):
    
    def inner():
        print("Fist")

        function()

        print("Third")

    return inner

def second_func():
    print("Second")


second_func = wrapper(second_func)
second_func()
