class A:
    a = 8
    b = 6

    def add(self):
        print(self.a + self.b)


class B:
    a = 7
    b = 5

    def sub(self):
        print(B.a - B.b)


class C(A, B):

    def mul(self):
        print(A.a * A.b)

    def div(self):
        print(B.a / B.b)


class D(C):

    def sqr(self):
        print(D.a ** 2)


class E(D):
    def cube(self):
        print(E.b ** 3)


obj = E()
obj.add()
obj.sub()
obj.mul()
obj.div()
obj.sqr()
obj.cube()
