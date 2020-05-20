try:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    print("Division is : ", a / b)
except ZeroDivisionError:
    print("You cannot divide the number by zero")
except Exception:
    print(" Something Went Wrong!! ")
else:
    print(" Division is success")
finally:
    print(" Program halt ")