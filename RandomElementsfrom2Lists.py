# Program to pick random elements from 2 lists
import random
list1 = ['1', '2', '3']
list2 = ['4', '5', '6']
num = []
for i in range(1,4,1):  # pick random elements for three times
    c = random.choice(list1), random.choice(list2)
    num.append(c)
for c in num:
    print(random.choice(num))

