class Father:
    a = 5
    b = 4

    def add(self):
        print(self.a + self.b)


class Mother:
    a = 6
    b = 3

    def sub(self):
        print(Mother.a - Mother.b)


class Child(Father, Mother):

    def mul(self):
        print(Father.a * Father.b)

    def div(self):
        print(Mother.a / Mother.b)


obj = Child()
obj.add()
obj.sub()
obj.mul()
obj.div()
