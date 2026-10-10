

# Duck typing = Another way to achieve polymorphism besides Inheritance
#                  Object must have the minimum necessary attributes/ methods
#                   "If it looks like a duck and quarks like a duck, it must be a duck "




class Animal:
    alive = True 

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")



class Car:
    alive = False   # This is like duck typing to have the attribute of animals in the Car
    def speak(self):
        print("HONK!")



animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)