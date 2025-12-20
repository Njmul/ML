

while True:
    try:
        x = int(input("Input a integer value : "))
        if x<0:
            raise ValueError("No negatives")
        
        print("Number is positive")
        break
        val = 100 / x
        print(val)
        break

    except ZeroDivisionError:
        print("Can't divided by zero.")
        break
    
    finally:
        print("Execution Complete")



