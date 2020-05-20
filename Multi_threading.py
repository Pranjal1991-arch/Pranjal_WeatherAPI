# from threading import *
# def new():
#     for x in range(5):
#         print('Child Executing...',current_thread().getName())
#
# t1=Thread(target=new)
# t1.start() #start thread execution
# t1.join() # Waiting
# print('Main ENDS', current_thread().getName())


from threading import *

print('Main Thread Starts', current_thread().getName())


def new():
    for i in range(10):
        print('Child thread is executing', current_thread().getName())


def new1():
    for i in range(10):
        print('Child 2', current_thread().getName())


t1 = Thread(target=new)
t2 = Thread(target=new1)
t1.start()
t2.start()
t1.join()
t2.join()
print('Main Thread Ends', current_thread().getName())
