import spwd
print("Root: " + str(spwd.getspnam('root')) + '\n') #Password detail for root
for entry in spwd.getspall():
    print("Name: " + entry[0] + "\t\tPassword: " + entry.sp_pwdp)