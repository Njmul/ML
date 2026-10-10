



import random

low = 1
high = 100
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

options = ("rock", "paper", "scissors")
print(options)


# For random integer number
number = random.randint(low, high)
print(number)


#For random floating number
number = random.random()
print(number)


random.shuffle(cards)
print(cards)