# Conditional statements
numb = int(input("Enter the number: "))
if numb < 0:
    print("Negative")
elif numb > 0:
    if numb % 2 == 0:
        print("Even")
    else:
        print("odd")
    print("Positive")
else:
    print("zero")
