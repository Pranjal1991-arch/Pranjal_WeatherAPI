class Sample:

    def __init__(self, a):
        self.a = a

    def __add__(self,other):
        return self.a + other.a


valueA = int(input("Enter the value A"))
valueB = int(input("Enter the value B"))
obj1 = Sample(valueA)
obj2 = Sample(valueB)
print(obj1 + obj2)

valueA = input("Enter the value A")
valueB = input("Enter the value B")
obj1 = Sample(valueA)
obj2 = Sample(valueB)
print(obj1 + obj2)