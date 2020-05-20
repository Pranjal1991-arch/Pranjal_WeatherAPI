import re

# txt = "rmsundar21@gmail.com"
# x = re.search("[aeiou]", txt)
# print(x)
# y = re.findall("[aeiou]", txt)
# print(y)
# z = re.split('@', txt)[1]
# print(z)

Phone = input("Enter the Phone")
if Phone.__len__() > 10 or re.search("^[9786]{1}[0-9]{9}", Phone) == None:
    print("Invalid Phone number")
else:
    print("Correct number")
