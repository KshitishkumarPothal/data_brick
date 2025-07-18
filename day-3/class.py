# class Dog:
#     sound = "Bark"
# print(Dog.sound)

class Dog:
    species = "Canine"
    def __init__(self,name,age):
        self.name= name
        self.age = age
# d1 = Dog()
d1 = Dog("bunny",2)
print(d1.age)
print(d1.name)
print(d1.species)
        