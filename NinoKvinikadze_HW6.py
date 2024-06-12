# 1. შექმენი ქვეყნის აბსტრაქტული კლასი. რომელსაც ექნება მინიმუმ სამი აბსტრაქტული მეთოდი.
# 2. შექმენი მისგან საქართველოს კლასი, რომელსაც ექნება public, protected და private ცვლადები
# (მაგალითად ბიუჯეტი, მოსახლეობა და ა.შ.).
# 3. შექმენი საქართველოს ობიექტი და გამოიყენე ზემოხსენებული მეთოდები.

from abc import ABC, abstractmethod

class Country(ABC):
    def __init__(self, kontinenti, mosaxleoba):
        self._continent = kontinenti
        self.population = mosaxleoba
        self._a = "Country.protected variable"
        print(self._a)
        self.__a = "Country.private variable"
        print(self.__a)

    @abstractmethod
    def capital_city(self):
        pass

    @abstractmethod
    def official_language(self):
        pass

    @abstractmethod
    def currency(self):
        pass


class Georgia:
    def __init__(self, kontinenti, mosaxleoba):
        Country.__init__(self, kontinenti, mosaxleoba)
        print(self._a)
        # print(self.__a) ეს აქ არ ჩანს
        self._a = "Georgia.Protected variable"
        print(self._a)
        self.__b = "Georgia.Private variable"
        print(self.__b)

    def capital_city(self):
        print("Tbilisi")

    def official_language(self):
        print("Georgian")

    def currency(self):
        print("GEL")

    @staticmethod
    def Country():
        print("Georgia")

georgia1 = Georgia("europe",3740000)
georgia1.currency()
georgia1.official_language()
georgia1.capital_city()
georgia1.Country()
print(georgia1._a)


# print(georgia1.__a) ეს აქედან არ იპრინტება
# print(georgia1.__b) ეს აქედან არ იპრინტება



