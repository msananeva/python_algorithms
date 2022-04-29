# on = True

def add():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number:"))
    print(a+b)

def substruction():
    a = float(input("Enter a number: "))
    b = float(input("Enter another number"))
    print(a-b)

def multipling():
    a = float(input("Enter a number"))
    b = float(input("Enter another number"))
    print(a*b)

def dividing():
    a = float(input("Enter a number"))
    b = float(input("Enter another number"))
    print(a/b)

# while on:


def x():
    operation = input("Please enter an operation +, -, *, / or q: ")
    if operation == "+":
        add()
    elif operation == "-":
        substruction()
    elif operation == "*":
        multipling()
    elif operation == "/":
        dividing()
        # elif operation == "q":
        #     on = False
    else:
        print("Please enter a valid operation")
        x()

x()
