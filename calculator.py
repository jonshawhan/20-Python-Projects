# define the functions needed: add, sub, mul, div
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until user wants to exit

def add(a, b):
    answer = a + b
    print("\n" + ">>>> " + str(a) + " + " + str(b) + " = " + str(answer) + " <<<<" + "\n")

def sub(a, b):
    answer = a - b
    print("\n" + ">>>> " + str(a) + " - " + str(b) + " = " + str(answer) + " <<<<" + "\n")

def mul(a, b):
    answer = a * b
    print("\n" + ">>>> " + str(a) + " * " + str(b) + " = " + str(answer) + " <<<<" + "\n")

def div(a, b):
    answer = a / b
    print("\n" + ">>>> " + str(a) + " / " + str(b) + " = " + str(answer) + " <<<<" + "\n")

while True:
    print("\n")
    print("A. Addition")
    print("S. Subtraction")
    print("M. Multiplication")
    print("D. Division")
    print("E. Exit")
    print("\n")

    choice = input("Input your choice: \n").lower()

    if choice == "a":
        print("\nYou chose Addition\n")
        a = int(input("Input first number: \n"))
        b = int(input("Input second number: \n"))
        add(a, b)
    elif choice == "s":
        print("\nYou chose Subtraction\n")
        a = int(input("Input first number: \n"))
        b = int(input("Input second number: \n"))
        sub(a, b)
    elif choice == "m":
        print("\nYou chose Multiplication\n")
        a = int(input("Input first number: \n"))
        b = int(input("Input second number: \n"))
        mul(a, b)
    elif choice == "d":
        print("\nYou chose Division\n")
        a = int(input("Input first number: \n"))
        b = int(input("Input second number: \n"))
        div(a, b)
    elif choice == "e":
        print("\nExiting\n")
        quit()