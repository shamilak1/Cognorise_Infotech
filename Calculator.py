import math

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b

def percentage(a,b):
    return (a / 100) * b

def square(a):
    return a ** 2

def square_root(a):
    if a < 0:
        return "Cannot calculate square root of negative number"
    else:
        return math.sqrt(a)


while True:
    print("\n====== PYTHON CALCULATOR ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage")
    print("6. Square")
    print("7. Square Root")
    print("8. Exit")

    choice = input("Enter the choice: ")

    if choice == "8":
        print("Thank you")
        break

    try:
        if choice in ["1","2","3","4","5"]:
            a = float(input("Enter the number: "))
            b = float(input("Enter the number: "))

            if choice == "1":
                print("Result:", addition(a,b))
            elif choice == "2":
                print("Result:", subtraction(a,b))
            elif choice == "3":
                print("Result:", multiplication(a,b))
            elif choice == "4":
                print("Result:", division(a,b))
            elif choice == "5":
                print("Result:", percentage(a,b))

                
        elif choice == "6":
            a = float(input("Enter Number: "))
            print("Result:", square(a))

        elif choice == "7":
            a = float(input("Enter Number: "))
            print("Result:", square_root(a))

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please enter valid numbers!")




