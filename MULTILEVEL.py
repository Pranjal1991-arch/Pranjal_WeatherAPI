class Grandparent:
    a = 5
    b = 4

    def add(self):
        print(self.a + self.b)


class Parent(Grandparent):
    def sub(self):
        print(Parent.a - Parent.b)


class Child(Parent):
    def mul(self):
        print(Child.a * Child.b)


obj = Child()
obj.add()
obj.sub()
obj.mul()
