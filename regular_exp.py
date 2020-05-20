import re

#str = "A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog"
# print(re.findall('[aeiou]', str))
# print(re.search("bro", str))
# print(re.split(" ", str)) #maxsplit =1, to split [optional]
# print(re.sub("\s", "*", str))  # replace

num = input("Enter the number")

print(re.findall(r'[0-28]', num))
