# Ask if want to generate random password
# If yes, ask for length
# generate password
# print password
# If no, exit

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password? Yes/No\n").lower()

if option == "yes":
    generate_password()
elif option == "no":
    print("Ending Program")
    quit()
else:
    print("Invalid inout. Please input yes or no")
    quit()    