

while True:
    password  = input("Set your password with at least 5 character : \n If you want to discontinue, write 'quit' ")

    if password == "quit":
        print("Exit from the loop, Done!")
        break

    elif len(password) >= 5:
        print("Password Set, Done!")
        break

    else:
            print("Too short password, Please try again ! ")
        

