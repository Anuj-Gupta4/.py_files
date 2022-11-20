from re import T
from tkinter import N


class Car:
    wheels=4

    def __init__(self, owner, model, color = "Red"): #init means initialze and its a constructor ,color = red is default param
        self.model = model
        self.color = color
        self.owner = owner

    def drive(self):
        print("My " + self.model + " is driving")

your_car = Car("Bharat", "Maruti")
print(your_car.owner)
print(your_car.color + "\n")

my_car = Car("Anuj", "Maruti", "Blue")
print(my_car.color)
print(my_car.owner)
print(my_car.wheels)
my_car.drive()