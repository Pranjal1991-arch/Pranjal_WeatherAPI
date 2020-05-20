fo=open("input1.txt","a+")
fo.write("\nElephant")
fo.seek(0)
print(fo.read())
fo.close