class Animal:
    def walk(self):
        print("walking")

class Dog(Animal):
    def bark(self):
        print("Bow Bow")
class Cat(Animal):
    def meow(self):
        print("Meow Meow")

d=Dog()
c=Cat()
d.walk()
d.bark()
c.walk()
c.meow()