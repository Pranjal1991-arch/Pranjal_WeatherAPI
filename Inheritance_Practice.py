# Single Inheritance
class Parent:
    a = 5
    b = 4

    def add(self):
        print(self.a + self.b)


class Child(Parent):

    def sub(self):
        print(Parent.a - Parent.b)

    def mul(self):
        print(Parent.a * Parent.b)


obj = Child()
obj.add()
obj.sub()
obj.mul()
