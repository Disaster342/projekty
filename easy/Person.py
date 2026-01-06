class Person:
    def __init__(self, first_name, surname, age):
        self.first_name = first_name
        self.surname = surname
        self.second_name = ""
        self.friends = []
        self.address = ""
        self.age = age
        self.email = first_name.lower() + "."+ surname.lower() + "@gmail.com"
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
    def del_friend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)
    def __str__(self):
        return f"{self.first_name} {self.surname}, {self.age} years old"


p1 = Person("Jane","Doe", 24)
p2 = Person("John", "Smith", 103)
p3 = Person("Chuy", "Gupi", 19)
p4 = Person("Walking", "Disaster", 67)
p5 = Person("Linkin", "Park", 33)

p1.add_friend(p5)
p1.add_friend(p3)

print(p5.email)
friends = ([str(friend) for friend in p1.friends])
print (friends)