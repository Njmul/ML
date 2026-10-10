

#Concession stand program


menu = {"pizza": 3.00,
        "nachos": 4.45,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "lemonade": 4.25}

cart = []
total = 0


print("-------MENU------")
for key, value in manu.items():
    print(f"{key:10}: ${value:.2f}")

print("------------------")

while True:
    food = input("Select a item (q to quit)").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)


print("-------Your Order------")
for food in cart:
    total = total + menu.get(food)
    print(food, end="")


print()
print(f"Total is : ${total:.2f}")
