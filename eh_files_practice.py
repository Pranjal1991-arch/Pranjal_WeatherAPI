# Exception handling in Files


try:
    fo = open("testfile.txt", "r")
    fo.write(" \nThis is my test file for exception handling!!")
except Exception:
    print(" File not available ")
else:
    print(" Written content in file sucessfully")

finally:
    print(" Program Halt")
