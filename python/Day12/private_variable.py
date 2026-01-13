


class User:
    def __init__(self, password):
        self.password = password

    def check__password(self, private):
        return private == self.password

u = User(123455)
print(u.check__password(123455))

