class Person:
    species = "human"
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Natalia", 24)

Person.lastname = "Piwińska"
p1.age = "25 years soon"
Person.city = "Rakszawa"
Person.country = "Polska"
Person.born = "01.12.2000"

print(p1.name)
print(p1.lastname)
print(p1.age)
print(p1.born)
print(p1.city)
print(p1.country)
print(p1.species)