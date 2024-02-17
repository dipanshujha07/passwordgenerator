import string
import random



# password length kis kitna hona chaiye
length = int(input("enter a length of password:"))

print('''chose character set for password form these:
         1. Digits:
         2. Letters:
         3. Special characters:
         4. Exit''')
characterlist = ""

while (True):
    choice = int(input("Pick a number:"))
    if (choice == 1):
        characterlist += string.ascii_letters
    elif (choice == 2):
        characterlist += string.ascii_letters
    elif (choice == 3):
        characterlist += string.ascii_letters
    elif (choice == 4):
        break
    else:
        print('Please pick a vaild option!')

password = []

for i in range(length):

    randomchar = random.choice(characterlist)


    password.append(randomchar)

# printing password as a string
print("The random password is " + "".join(password))