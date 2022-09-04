class Cars:
    def __init__(self, name, price, colour):
        self.name = name
        self.price = price
        self.colour = colour
    def start(self):
        print(self.name+" Engine started..Vroom vroom")

car1 = Cars("Maruthi Swift", 500000, "Red")
car2 = Cars("Toyoto Innova", 1500000, "White")

car1.price=1000000
car2.colour="Yellow"

# del car1.colour
print(car1.name, car1.price, car1.colour)
print(car2.name, car2.price, car2.colour)
car1.start()
car2.start()