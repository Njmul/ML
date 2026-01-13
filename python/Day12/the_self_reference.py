


class User:
    def __init__(self, name):

        self.name = name
    def login(self):

        return f"{self.name} logged in"


user1 = User("Jim")
print(User.login(user1))
