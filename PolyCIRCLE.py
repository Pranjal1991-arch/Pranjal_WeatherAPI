import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def display(self):
        print(" RADIUS: {}".format(self.radius))


class Area(Circle):
    def __init__(self, radius, area):
        self.radius = radius
        area = radius ** 2 * 3.14

        self.area = area
        Circle(self.radius)

    def display(self):
        Circle.display(self)
        print("AREA:{}".format(self.area))


class Circumference(Circle):
    def __init__(self, radius, circum):
        self.radius = radius
        circum = radius * 2 * 3.14
        self.circum = circum

        Circle(self.radius)

    def display(self):
        Circle.display(self)
        print("CIRCUM:{}".format(self.circum))


ARea1 = Area(2)
ARea1.display()
CIRcum1 = Circum(3)
CIRcum1.display()
