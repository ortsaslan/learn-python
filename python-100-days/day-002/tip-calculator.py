print("\nWelcome to the Tip Calculator!")

print("\nWhat was the total bill? ", end="")
total_bill = float(input())

print("\nWhat percentage tip would you like to give? 10, 12 or 15? ", end="")
tip_percentage = int(input())

print("\nHow many people to split the bill? ", end="")
payers = int(input())

payment = total_bill / payers * (tip_percentage / 100)
print(f"\nEach person should pay: {payment:.2f}")