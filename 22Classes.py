class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")

p1 = Point()
p1.x=10
p1.y=20
print(p1.y)
p1.move()
p1.draw()

p2=Point()
p2.x=50
print(p2.x)