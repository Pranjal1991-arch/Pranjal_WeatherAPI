age = int(input("Enter the Age of the Person: "))
if age >= 0 and age < 18:
    print("Person is not eligible to vote")
elif age >= 18:
    if age >= 60:
        print("Person is a Senior citizen")
    else:
        print("Person is not a Senior citizen")
    print("Person is Eligible to vote")
else:
    print("Invalid Age")
