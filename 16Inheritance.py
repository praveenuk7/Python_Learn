#parent class
class Person:
    def __init__(self, name, contact):
        self.name=name
        self.contact=contact
    def address(self):
        print("Address:")
        print(self.name, self.contact)

#child class
class Doctor(Person):
    pass

class Patient(Person):
    pass

doc1=Doctor("John",1234)
pat1=Patient("Anil", 9876)

doc1.address()
print("************************************8")
pat1.address()