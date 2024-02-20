class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def __str__(self):
        return super().__str__() + f", {self.doors}-door"

class Boat(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type

    def __str__(self):
        return super().__str__() + f", {self.type}"

class Plane(Vehicle):
    def __init__(self, make, model, year, engines):
        super().__init__(make, model, year)
        self.engines = engines

    def __str__(self):
        return super().__str__() + f", {self.engines}-engine"

car1 = Car("Toyota", "Corolla", 2020, 4)
car2 = Car("Ford", "Mustang", 2021, 2)
boat1 = Boat("Yamaha", "242X", 2019, "Speedboat")
boat2 = Boat("Bayliner", "Element E16", 2022, "Bowrider")
plane1 = Plane("Boeing", "747", 2016, 4)
plane2 = Plane("Airbus", "A320", 2018, 2)

vehicles = [car1, car2, boat1, boat2, plane1, plane2]
for vehicle in vehicles:
    print(vehicle)
