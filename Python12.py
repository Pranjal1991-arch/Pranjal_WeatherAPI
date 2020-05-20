# ATM pin logic
print("Welcome to United Bank of INDIA")
count = 0
while count < 3:
    pin = input("ENTER YOUR PIN: ")
    if pin == '1257':
        print("Access Granted")
        break
    else:
        print("Wrong PIN. Try Again")
        count+=1
for count in range (0,3,1):

        print("Account Blocked")

        break





