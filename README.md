# 📘 Python OOP Assignment

This project demonstrates fundamental Object-Oriented Programming (OOP) concepts in Python, including classes, constructors, inheritance, encapsulation, and polymorphism. The project is divided into two parts:

# Part 1: Designing a Gaming Smartphone (Class & Inheritance)
🔹 Description

This section defines a Smartphone class and a GamingSmartphone subclass that inherits from it. The aim is to demonstrate:

How constructors initialize attributes.

How methods define class behaviours.

How subclasses extend parent functionality.

How objects can be created and interacted with.

🔹 Features

Smartphone Class

Attributes: brand, model, storage, battery life.

Methods:

make_call(number) → Simulates making a call.

browse_internet(hours) → Reduces battery life when browsing.

charge() → Recharges the battery to full.

GamingSmartphone Subclass

Inherits all features of Smartphone.

Adds attributes: cooling system, bigger RAM, rotate screen.

New Method:

play_game(game, hours) → Drains battery faster than browsing.

🔹 Example Usage
phone1 = Smartphone("Samsung", "Galaxy S23", 128, 24)
phone1.make_call("+254712345678")
phone1.browse_internet(5)
phone1.charge()

gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 256, 20)
gaming_phone.play_game("PUBG", 3)
gaming_phone.browse_internet(2)

# Part 2: Polymorphism with Vehicles
🔹 Description

This section demonstrates polymorphism, where multiple classes inherit from a base class but implement their own version of a shared method (move()).

🔹 Features

Vehicle Base Class

Method: move() → Generic movement method (intended to be overridden).

Subclasses (Car, Helicopter, Ship, Train, Submarine, Bicycle)

Each subclass overrides move() with a unique implementation:

Car.move() → "Car is driving 🚗"

Helicopter.move() → "Helicopter is flying ✈️"

Ship.move() → "Ship is sailing 🚤"

Train.move() → "Train is chugging 🚆"

Submarine.move() → "Submarine is diving 🌊"

Bicycle.move() → "Bicycle is pedaling 🚴"

🔹 Example Usage
vehicles = [Car(), Helicopter(), Ship(), Train(), Submarine(), Bicycle()]

for v in vehicles:
    v.move()

# 🎯 Learning Outcomes

By completing this project, we have demonstrated:

✅ Defining and instantiating classes.

✅ Using constructors (__init__) to initialize object attributes.

✅ Applying inheritance to extend functionality.

✅ Demonstrating polymorphism by overriding methods in subclasses.

✅ Writing clean, scalable, and well-documented Python code.
