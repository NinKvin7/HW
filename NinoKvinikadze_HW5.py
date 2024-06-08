# 1. შექმენი ტრანსპორტის კლასი მინიმუმ 4 კლასის პარამეტრით
# 2. დაამატე ერთი სტატიკური მეთოდი.
# 3. დაამატე ორი კლასის მეთოდი.
# 4. დაამატე __init__ magic მეთოდი და მინიმუმ 3 ობიექტის პარამეტრი.
# 5. დაამატე მინიმუმ 2, ობიექტის მეთოდი.
# 6. დაამატე __repr__ magic მეთოდი.
# 7. ზემოხსენებული კლასისგან შექმენი მინიმუმ 5 ობიექტი და გამოიძახე მისი ზოგიერთი მეთოდი და პარამეტრი.

class Transport:
    wheels = 5
    SteeringWheel = 1
    mirrors = 3
    pedals = 2

    def __init__ (self, brendi, weli, garbeni):
        self.brand = brendi
        self.year = weli
        self.mile = garbeni

    def say_brand(self):
        print(f"The brand name is {self.brand}")

    def say_mile(self):
        print(f"ამ მანქანას აქვს {self.mile} მილი გარბენი")

    @staticmethod
    def moving():
        print("შუქნიშანს დააკვირდი!")

    @classmethod
    def wheels_Number(cls):
        print(f"ამ ტრანსპორტს აქვს {cls.wheels} ბორბალი")

    @classmethod
    def mirrors_Number(cls):
        print(f"ამ ტრანსპორტს აქვს {cls.mirrors} სარკე")

    def __repr__(self):
        return f"Transport(brand: {self.brand}, year: {self.year}, mile: {self.mile})"


car1=Transport('Toyota', 2015, 26000 )

car1.moving()
car1.wheels = 4
car1.wheels_Number()
car1.mirrors_Number()

print(car1)

car2 = Transport('Toyota', 2020, 38000 )
car3 = Transport('Audi', 2017, 35000 )
car4 = Transport('BMW', 2023, 30000 )
car5 = Transport('Honda', 2020, 44000 )

print(car2, car3, car4)

car2.say_brand()
car3.say_brand()
car4.say_brand()
car5.say_brand()

car2.say_mile()
car3.mirrors_Number()

car5.moving()