# Algorithm:
## Take operands and operator from stdin
## Print result of arithmetic operation in format: x + y = z
## Suggest further calculation with or without last result

def calculator():

    calc_art = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

    print(calc_art)

    while True:
        first_operand = int(input("\nWhat's the first number? "))
        operator = input("\nPick the operation (+, -, *, /): ")
        second_operand = int(input("\nWhat's the second number? "))

        result = 0
        if operator == "+":
            result = first_operand + second_operand
        elif operator == "-":
            result = first_operand - second_operand
        elif operator == "*":
            result = first_operand * second_operand
        elif operator == "/":
            result = first_operand / second_operand

        print(f"\n{first_operand} {operator} {second_operand} = {result:.2f}")

        is_next_calc = input("\nIs there another calculation? Type 'yes' or 'no': ")
        if is_next_calc == "no":
            break
    
calculator()