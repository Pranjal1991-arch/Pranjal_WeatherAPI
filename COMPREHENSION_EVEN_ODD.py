# list1 = []
# for i in range(1, 101, 1):
#    if i % 2 == 0:
#        list1.append(i)
#        print(list1)
list1 = ["Even" if i % 2 == 0 else "Odd" for i in range(1,101,1)]
print(list1)
