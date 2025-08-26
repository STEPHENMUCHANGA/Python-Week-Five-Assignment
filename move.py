# Part 2: Polymorphism 

# Base class
class Vehicle:
    def move(self):
        """Default movement (to be overridden by subclasses)"""
        print("This vehicle moves...")

# Subclass 1: Car
class Car(Vehicle):
    def move(self):
        print("Car is driving on the road 🚗")

# Subclass 2: Helicopter
class Helicopter(Vehicle):
    def move(self):
        print("Helicopter is flying in the sky ✈️")

# Subclass 3: Ship
class Ship(Vehicle):
    def move(self):
        print("Ship is sailing on the water 🚤")

# Subclass 4: Train
class Train(Vehicle):
    def move(self):
        print("Train is chugging along the tracks 🚆")

# Subclass 5: Submarine
class Submarine(Vehicle):
    def move(self):
        print("Submarine is diving underwater 🌊")

# Subclass 6: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Bicycle is pedaling on the path 🚴")

# Polymorphism shown in various vehicle types
vehicles = [Car(), Helicopter(), Ship(), Train(), Submarine(), Bicycle()]

for v in vehicles:
    v.move()   # Each object or vehicle uses its own move() method
