
import pickle

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

u1 = User("Najmul", 32)

with open("user.pkl", "wb") as f: # Save serializer by name user.pkl
    pickle.dump(u1, f)

with open("user.pkl", "rb") as f: # Deserialize the file by loading
    u2 = pickle.load(f)

print(u2.name, u2.age)
