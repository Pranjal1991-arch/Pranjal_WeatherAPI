fo = open("vinod.txt", "r")
fo.seek(9)
print(fo.read(2))
print(fo.read(2))
fo.close()