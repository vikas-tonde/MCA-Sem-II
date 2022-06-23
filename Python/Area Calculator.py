class shape:
    def area(self):
        print("This is base area")


class Triangle(shape):
    def __init__(self):
        self.b = int(input("Enter the base: "))
        self.h = int(input("Enter the height: "))
        super().area()

    def area(self):
        print("Area = ", (self.b*self.h)/2)


class Circle(shape):
    def __init__(self):
        self.r = int(input("Enter the radius of circle: "))

    def area(self):
        print("Area = ", 3.14*(self.r**2))


t = Triangle()
t.area()
c = Circle()
c.area()
