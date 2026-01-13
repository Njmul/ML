
class User:
    def __init__(self, name):
        self.name = name
        self.is_active = True

class Admin(User):
    def __init__(self, name, role="admin"):
        super().__init__(name) # This will work as parent constructor
        self.role = role



a = Admin("Root")
print(a.name)
print(a.is_active)
print(a.role)
