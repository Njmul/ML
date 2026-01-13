class User:
    def __init__(self, name):
        self.name = name

    def login(self):
        return f"{self.name} logged in"

class Admin(User):
    def delete_db(self):
        return "Database changed!"

u = User("Alice")
a = Admin("Root")

print(u.login())
print(a.login()) # this executed because of inheritance
print(a.delete_db())

