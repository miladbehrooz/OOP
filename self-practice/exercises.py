# exercises from following webpage:
# https://pynative.com/python-object-oriented-programming-oop-exercise/#h-oop-exercise-1-create-a-class-with-instance-attributes

# 1. Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle():
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage


car = Vehicle(120,50000)
print(car.max_speed, car.mileage)


# 2.Create a Vehicle class without any variables and methods

class Vehicle():
    pass


# 3.Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# Given

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.
# Expected Output:
# Vehicle Name: School Volvo Speed: 180 Mileage: 12
class Bus(Vehicle):
    pass

school_bus = Bus('School Volvo', 180, 12)
print(f'Vehicle Name: {school_bus.name} Speed: {school_bus.max_speed} Mileage: {school_bus.mileage}')


# 4. Class Inheritance

# Given:
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
# Use the following code for your parent Vehicle class.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

# Expected Output:
# The seating capacity of a bus is 50 passengers

# Hints:
#First, use method overriding.
# Next, use default method argument in the seating_capacity() method definition of a bus class.

class Bus(Vehicle):

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

school_bus = Bus("bus",180,12)
print(school_bus.seating_capacity())


# 5. Define a property that must have the same value for every class instance (object)
# Define a class attribute ”color” with a default value white. I.e., Every Vehicle should be white.
# Use the following code for this exercise.

class Vehicle:
    COLOR = "white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def __repr__(self):
        return f"Color: {self.COLOR}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"


class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

# Expected Output:
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18
# Hint:
# Define a color as a class variable in a Vehicle class

school_bus = Bus("School Volvo",180 ,12)
car = Car("Audi Q5", 240, 18)


#print(f"Color: {school_bus.COLOR}, Vehicle name: {school_bus.name}, Speed: {school_bus.max_speed}, Mileage: {school_bus.mileage}")
#print(f"Color: {car.COLOR}, Vehicle name: {car.name}, Speed: {car.max_speed}, Mileage: {car.mileage}")
print(school_bus)
print(car)


# 6. Class Inheritance

# Given:
# Create a Bus child class that inherits from the Vehicle class. 
# The default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

# Note: The bus seating capacity is 50. so the final fare amount should be 5500. 
# You need to override the fare() method of a Vehicle class in Bus class.
# Use the following code for your parent Vehicle class.
# We need to access the parent class from inside a method of a child class.


# Expected Output:
# Total Bus fare is: 5500.0

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    
    def fare(self):
        return self.capacity * 110

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())






