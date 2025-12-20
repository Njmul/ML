
while True:
    try:
        x = 0
        val = 100 / x
        print(val)
        break

    except ZeroDivisionError:
        print("Can't divided by zero.")
        break
