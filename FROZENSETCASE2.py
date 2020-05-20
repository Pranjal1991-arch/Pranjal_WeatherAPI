# creating a dictionary
Student = {"name": "Ankit", "age": 21, "sex": "Male", "college": "MNIT Allahabad", "address": "Allahabad"}
# making keys of dictionary as frozen set
Student1 = {"name": "Ankit", "age": 21, "sex": "Male"}
key = frozenset(Student)
print(key.difference(Student1))
print('The frozen set is:', key)
