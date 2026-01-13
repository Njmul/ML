class User:
    species = "Human" # Public variable

    def __init__(self, name):
        self.name = name # instance variable

u1 = User("A")

print(u1.name, u1.species)

User.species = "Alien" # Change public variable value
print(u1.species)

u1.species = "Robot" # Change the instance variable value
print(u1.species)

