

def wrapper(function):
    
    def inner():
        print("Fist")

        function()

        print("Third")

    return inner

@wrapper  # this is as same as "second_func = wrapper(second_func)"

def second_func():
    print("Second")


second_func()

