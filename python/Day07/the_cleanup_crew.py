
while True:
    try:
        x = 6
        val = 100 / x
        print(val)
        break

    except ZeroDivisionError:
        print("Can't divided by zero.")
        break
    
    finally:
        print("Execution Complete")

