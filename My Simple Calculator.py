#Joebeck Andrew F. Gusi | BSCPE 1-5 | Assignment No.5
#https://github.com/Jubikk?tab=repositories

import time

# Define the whole calculator function
def simple_calculator():
    print("Welcome to My Simple Calculator!" + "\n")
    time.sleep(0.5)
    try:
        integer1 = float(input("Please Enter the first(1st) number: "))
        time.sleep(0.5)
        integer2 = float(input("Please Enter the second(2nd) number: "))
    except ValueError:
        print("Invalid! Please enter another number.")
        simple_calculator()
    time.sleep(0.5)
    # Using elif to make it easier and will make it look cleaner
    operation = input("Choose the operation (+, -, *, /): ")
    try:
        if operation == "+":
            result = integer1 + integer2
        elif operation == "-":
            result = integer1 - integer2
        elif operation == "*":
            result = integer1 * integer2
        elif operation == "/":
            result = integer1 / integer2
        else:
            print("Invalid operation! Please choose another operation.")
            simple_calculator()
    except ZeroDivisionError:
        print("Zero-based division is not allowed. Please try again.")
        simple_calculator()
    time.sleep(0.8)
    # Displaying the result
    print("The result is:", result)
    try_again = input("Do you want to try again? (Y/N): ")
    if try_again.upper() == "Y":
        simple_calculator()
    else:
        print("Thank you for using My Simple Calculator!")
simple_calculator()


