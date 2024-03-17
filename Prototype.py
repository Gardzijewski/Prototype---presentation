import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attrs):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj

class Car:
    def __init__(self):
        self.make = "Default Make"
        self.model = "Default Model"
        self.year = "Default Year"

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

prototype = Prototype()

car = Car()
prototype.register_object("Car", car)

car1 = prototype.clone("Car", make="Toyota", model="Camry", year="2022")
car2 = prototype.clone("Car", make="Honda", model="Civic", year="2023")

print(car1)
print(car2)
