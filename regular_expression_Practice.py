import re

txt = "The rain in Spain"
x = re.search("[aeiou]", txt)
y = re.findall("[aeiou]", txt)
print(x)
print(y)
z = re.sub('a', '*', txt)
print(z)
w = re.split("a", txt)
print(w)

Phone = input("Enter the Phone")

if re.search("^[9786]{1}[0-9]{9}", Phone) == None:
    print("Invalid Phone number")
else:
    print("Correct number")
