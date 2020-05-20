class Schoolmember:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("NAME: {} \n AGE: {}".format(self.name, self.age))

class Student(Schoolmember):

    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
        Schoolmember(self.name,self.age)

    def display(self):
        Schoolmember.display(self)
        print("MARKS: {}".format(self.marks))


class Staff(Schoolmember):

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Schoolmember(self.name, self.age)

    def display(self):
        Schoolmember.display(self)
        print("SALARY: {}".format(self.salary))

stud1=Student("JOHN",12,98)
stud1.display()
staff1 = Staff("TOM",54,60000)
staff1.display()