# list1 = [1,2,3,4,5,6,7]
# for i in list1:
#     print(i)

# dict1 = {
#     'Name':'abc',
#     'Location':'Bangalore',
#     'Salary':2000,
#     'Country':'India'
# }
# for i in dict1.items():
#     print('{} is {}'.format(i[0],i[1]))
#
# for i,j in dict1.items():
#     print(i,j)

list1 = [7,8,6,4,2,1]
print(type(list1))
itr_list = iter(list1)
print(type(itr_list))
print(itr_list.__next__())
print(itr_list.__next__())
print(itr_list.__next__())
print(itr_list.__next__())
print(itr_list.__next__())