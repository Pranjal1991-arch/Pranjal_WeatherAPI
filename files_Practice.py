fo=open("input.txt","r+")

fo.write(",\nElephant")
fo.seek(0)
print(fo.read())
# fo.seek(9)
# print(fo.read(2))
# print(fo.read(4))
# print(fo.readlines())
# for i in fo.readlines():
#     print(i)


fo.close()