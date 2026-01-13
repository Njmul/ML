
class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Wallet(self.amount + other.amount)

    def __repr__(self):
        return f"Wallet(amount={self.amount})"

w1 = Wallet(50)
w2 = Wallet(70)

w3 = w1 + w2
print(w3)
