# Algorithm:
## Take operands and operator from stdin
## Print result of arithmetic operation in format: x + y = z
## Suggest further calculation with or without last result

import os
import art


# Define operation functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# Define operations dict
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# Define app's main function
def calculator():

    saved_result = None

    while True:
        
        if saved_result == None:
            print(art.calc_logo)
            first_operand = int(input("\nEnter the first number: "))
        else:
            first_operand = saved_result

        operator = input("\nPick the operation (+, -, *, /): ")
        second_operand = int(input("\nEnter the second number: "))

        current_operation = operations[operator]
        result = current_operation(first_operand, second_operand)

        print(f"\n{first_operand} {operator} {second_operand} = {result}")

        next_calc = input(f"\nType 'c' to continue calculating with {result} as first number, \
                          \nType 'n' to start new calculation,\nType 'e' to exit from calculator. \
                          \nYour choice: ")
        if next_calc == "c":
            saved_result = result
        elif next_calc == "n":
            saved_result = None
            os.system("clear")
        elif next_calc == "e":
            print("\nCalculator is turned off!")
            break


calculator()
