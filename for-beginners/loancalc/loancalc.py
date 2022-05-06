import math

principal = int(input("Enter the loan principal:\n"))
second_val = input('What do you want to calculate?\ntype "m" - for number of monthly payments,\ntype "p" - for the monthly payment:\n')

if second_val == "m":
    payment = int(input("Enter the monthly payment:\n"))
    months_to_repay = math.ceil(principal / payment)
    if months_to_repay == 1:
        print("\nIt will take 1 month to repay the loan")
    else:
        print(f"\nIt will take {months_to_repay} months to repay the loan")
elif second_val == "p":
    months = int(input("Enter the number of months:\n"))
    month_payment = principal / months
    if isinstance(month_payment, float):
        month_payment = math.ceil(month_payment)
        last_payment = principal - (months - 1) * month_payment
        print(f"\nYour monthly payment = {month_payment} and the last payment = {last_payment}.")
    else:
        print(f"\nYour monthly payment = {month_payment}")
