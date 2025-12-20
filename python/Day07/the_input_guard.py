

while True:
    try:
        val = int(input("Enter your age : "))
        print(f"Your age is {val}")
        break

    except ValueError:
        print("Numbers Only ! ")
