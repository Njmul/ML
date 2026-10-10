


# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class


class Student:
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidert", 34)
student4 = Student("Sanady", 25)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")


# Access a class variable by instance name
print(student2.name)
print(student2.age)
print(student2.class_year)

# Access a class variable by class name
print(Student.name) 
print(Student.age)
print(Student.class_year)