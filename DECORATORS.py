def incr(a):
    a += 1
    return a


def decr(a):
    a -= 1
    return a

def operate(fn,a):
    print(fn(a))

operate(incr,6)
operate(decr,6)
#print(incr(5))
#print(decr(8))
