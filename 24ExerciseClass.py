class Person:
    def __init__(self, name):
        self.name=name

    def talk(self):
        print(f"Hi, I am {self.name} ")

pravi=Person("Praveen")
varun=Person("Varun")
pravi.talk()
varun.talk()