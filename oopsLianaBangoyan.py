# 1.  Write a class named Student with two attributes student_id, student_name. Add a new attribute student_class.
#     Create a function to display the entire attribute and their values in Student class.

class Student():

    def __init__(self, name, id):
        print("Called constructor")
        self.name = name
        self.id = id
    def speak(self):
        print("Speaking...")

    def read(self):
        print("Reading...")

    def learn(self):
        print("Learning...")

    def get_personal_information(self):
        print(f"Student's name is: {self.name}")
        print(f"Student's ID is: {self.id}")

student1 = Student("Lily", "007")

# 2. Create a Vehicle class without any variables and methods

class Vehicle ():
    return ()

#
# 3.Write a program to create a Vehicle class with max_speed and mileage instance attributes.


class Vehicle ():
    def __init__(self, name, max_speed, mileage):
        print('Called constructor')
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def get_personal_information(self):
        print(f"Name is: {self.name}")
        print(f"Max_speed is: {self.max_speed}")
        print(f"Mileage is: {self.mileage}")

vehicle1 = Vehicle ("Lamborghini", 300, 2000)


# 4. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Bus (Vehicle):
    def __init__(self, name, max_speed, mileage):
    def super()_init__(name, max_speed, mileage):

bus1 = Bus ("MAN", 150, 300)

#5. Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.