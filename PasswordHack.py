from random import *

guess = ""
password = input("Enter Password:")
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
while guess != password:
    guess = ""
    for letter in password:
        guessletter = letters[randint(0, 25)]
        guess = str(guessletter) + str(guess)
        print(guess)

        print("Password guessed!")

    # input("")
