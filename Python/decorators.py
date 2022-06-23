from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def personFromBirthYear(cls, name, year):
        return cls(name, int(date.today().year) - year)

    @staticmethod
    def isAdult(age):
        if(age >= 18):
            return True
        return False


p = Person("Rajeev", 24)
p2 = Person.personFromBirthYear("Bhaskar", 2019)

print(p.name, p.age)
print(p2.name, p2.age)
print(Person.isAdult(p.age))
print(Person.isAdult(p2.age))
