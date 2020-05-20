class Sample:

    def __init__(self):
        print("Constructor has been called")

    def display(self):
        print("Normal Function")

    def __del__(self):
        print("Destructor has been called")


print('Main Program Starts')
obj1=Sample()
print('Main Program Ends')
obj1.display()
