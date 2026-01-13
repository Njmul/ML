


from datetime import date

class User:
    def __init__(self, birth_year):
        self.birth_year = birth_year

    @property  # this is called encapsulation
    def age(self):
        current_year = date.today().year
        return current_year - self.birth_year

u = User(2000)
print(u.age)
