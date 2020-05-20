print("Welcome to United Bank of India ATM")
count = 0
for count in range (0,3,1):
    pin = input("ENTER YOUR PIN: ")
    if pin == '1257':
        print("Access Granted")
        break
    else:
        print("Wrong PIN. Try Again")

        count+=1

while count > 2:

        print("Account Blocked")

        break
