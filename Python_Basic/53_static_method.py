


# Static methods = A method that belong to a class rather than any object from that class (instance)
#                   Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)

# def get_info(self):
#     return f"{self.name} = {self.position}"


# # Static methods = Best for utility functions that do not need access to class data

# @staticmethod
# def km_to_miles(kilometers):
#     return kilometers * 0.621371

# Example 


class Employee:
    def __init__(self, name, position) -> None:
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    

   

    @staticmethod   # Decorator
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]

        return position in valid_positions



employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Spongbob", "Cook")


print(Employee.is_valid_position("Scientist"))

print(employee1.get_info())
print(employee2.get_info())