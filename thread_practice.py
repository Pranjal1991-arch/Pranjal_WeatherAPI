from threading import *


def cube(n):
    print(n ** 3)


def sqr(n):
    print(n ** 2)


if __name__ == "__main__":
    print("Thread is created")
    t1 = Thread(target=cube, args=(10,))
    t2 = Thread(target=sqr, args=(10,))
    print("Thread is started")
    t1.start()
    t2.start()
    print("Thread is joined")
    t1.join()
    t2.join()
    print("It is completed")
