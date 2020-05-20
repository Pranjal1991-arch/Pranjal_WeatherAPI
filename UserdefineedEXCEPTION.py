class EmpIDNotZero(Exception):
    pass


try:
    empid = int(input("Enter EMP ID:"))
    if empid == 0:
        raise EmpIDNotZero
except Exception:
    print(" Something Went Wrong!!")
else:
    print("EMP ID is success")
finally:
    print(" Program Halt")
