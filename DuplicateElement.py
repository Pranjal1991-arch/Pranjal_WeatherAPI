# program to print duplicate elements in a list
list1 = [2,1,2,1,5,4,5,6,4,7,6,11,34,66]
list1.sort()
for i in range(len(list1)-1):
    if list1[i] == list1[i+1]:
        print(list1[i])