import secrets
import string

characters = string.ascii_letters

while True:
    try:
        print("Password must be between 1 and 100 characters")
        pwLength = int(input("Enter the length of the password: "))

        if 0 < pwLength <= 100:
            break
        else:
            print("Password Length must be within range of 1 to 100")

    except ValueError:
        print("Password must be an integer")

#Include Numbers
while True:
    numAnswer = input("Would you like to include numbers: y/n ")
    if numAnswer == "y":
        characters += string.digits
        break
    elif numAnswer == "n":
        break
    else:
        print("Please enter y or n")

#Include Special Characters
while True:
    scAnswer = input("Would you like to include special characters: y/n ")
    if scAnswer == "y":
        characters += string.punctuation
        break
    elif scAnswer == "n":
        break
    else:
        print("Please enter y or n")

#Multiple passwords
while True:
    try:
        mpAnswer = int(input("How many passwords would you like to generate?: "))

        if mpAnswer > 0:
            break
        else:
            print("You must generate at least one password")

    except ValueError:
        print("Please enter an integer")

for i in range(mpAnswer):
    password = ""
    for j in range(pwLength):
        password += secrets.choice(characters)

    print("Generated Password:", password)



