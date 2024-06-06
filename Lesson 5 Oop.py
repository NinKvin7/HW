
# class Human:
#     weight = 60
#     height = 170
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def sleeping():
#         print("ZZZZZZzzzzzZZzzz...")
#
# human1 = Human("Levani")
#
# class Georgian(Human):
#
#     def __init__(self, name, age):
#         # Human.__init__(self, name)
#         super().__init__(name)
#         self.age = age
#
#     @staticmethod
#     def drinking():
#         print("I want to say ...")
#
# human2 = Georgian("Nika", 24)
# print(human2.name)




# class Animals:
#     age = 5
#     height = 100
#
#     def __init__(self, which):
#         self.which = which
#
#     @staticmethod
#     def sleeping():
#         print("ZZZZZZzzzzzZZzzz...")


class Cats(Animals):

    def __init__(self, name, weight):
        Cats.__init__(self, name)
        self.weight = weight

    @staticmethod
    def drinking():
        print("I love milk")

cats(Animals) = cats('fiso', 24)
print(cats(Animals))





class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod
    def move():
        print("I am Moving...")


class Car(Vehicle):
    pass

class Ship(Vehicle):
    @staticmethod
    def move():
        print("I am Swimming...")


class Airplane(Vehicle):
    @staticmethod
    def move():
        print("I am Flying...")


car = Car("BMW", "X5")
ship = Ship("SomeCompany", "dasdasds")
plane = Airplane("Boing", "sasdads")

car.move()



from abc import ABC, abstractmethod

class Figures(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Cycle(Figures):
    def __init__(self, r):
        self.radius = r

    def area(self):
        print(3.14 * self.radius * self.radius)

    def area(self):
        print(2 * 3.14 * self.radius)





