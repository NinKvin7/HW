

#f(x) = 2x+1     g(x)= 3-x    so   f(g(x))=2(3-x)+1=6-2x+1=7-2x

# def f(z):
#     def inner():
#         return 2 * z + 1
#     return inner
#
# def g(x):
#     return 3 - x
#
# result = f(g(5))()
# print(result)

#
# def f(z):
#     return 2 * z + 1
#
#
# def g(x):
#     return 3 - x
#
# result = f(g(5))
# print(result)





# class Human:
#     height = 170
#     eyes_number = 2
#
# print(Human.height)
#
# Human.Head = 1 #დავამატოთ კლასს წევრი
# print(Human.Head)


class Human:
    height = 170
    eyes_number = 2  #ეს არის პარამეტრები

    def __init__ (self, saxeli, asaki):
        self.name = saxeli
        self.age = asaki

    def say_name(self):
        print(f"hi {self.name}, you are, {self.age} years old")
    @staticmethod #ამ მეთოდს ვიყენებთ მაშინ, როდესაც განსაზღვრულ ფუნქციას კლასის პარამეტრები ცვლადად არ სჭირდება
    def sleeping():
        print("Zzz")   #ეს არის მეთოდი

    @classmethod #ეს მეთოდი გვჭირდება მაშინ, როდესაც ინფორმაცია კლასიდან უნდა წამოიღოს
    def say_height(cls): #აქ მიღებულია რო ეს დავწეროთ. თავისი თავის სახელს გადასცემს
        print(f"am saying {cls.height}")

    def __repr__(self):
        return f"Human({self.name}, {self.age})"


Human.sleeping()
Human.say_height()

# human1 = Human()
# print(human1)
#
# human1.name = "nino"
# human1.say_name()

human2 = Human("nini", 24)

human2.say_name()
print(human2)
































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

#
# class Cats(Animals):
#
#     def __init__(self, name, weight):
#         Cats.__init__(self, name)
#         self.weight = weight
#
#     @staticmethod
#     def drinking():
#         print("I love milk")
#
# cats(Animals) = cats('fiso', 24)
# print(cats(Animals))
#
#
#
#
#
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     @staticmethod
#     def move():
#         print("I am Moving...")
#
#
# class Car(Vehicle):
#     pass
#
# class Ship(Vehicle):
#     @staticmethod
#     def move():
#         print("I am Swimming...")
#
#
# class Airplane(Vehicle):
#     @staticmethod
#     def move():
#         print("I am Flying...")
#
#
# car = Car("BMW", "X5")
# ship = Ship("SomeCompany", "dasdasds")
# plane = Airplane("Boing", "sasdads")
#
# car.move()
#
#
#
# from abc import ABC, abstractmethod
#
# class Figures(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# class Cycle(Figures):
#     def __init__(self, r):
#         self.radius = r
#
#     def area(self):
#         print(3.14 * self.radius * self.radius)
#
#     def area(self):
#         print(2 * 3.14 * self.radius)
#
#
#
#
#
