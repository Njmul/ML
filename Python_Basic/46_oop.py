

#Object = A "bundle" pf related attributes (variables) and methods (functions)
#       Ex. phone, cup, book
#       You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object



class Car:
    def __init__(self, model, year, color, for_sale): # dander method, constructive
        self.model = model
        self.year = year 
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print("You drive the car {self.model}")
    def stop(self):
        print("You stop the car {self.model}")

car1 = Car("Mustang", 2024, "red", False)
car1 = Car("Corvette", 2025, "blue", True)
car1 = Car("Charger", 2026, "yellow", False)



car1.drive()
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
