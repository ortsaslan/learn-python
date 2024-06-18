print("Welcome to Python Pizza Deliveries!")

pizza_size = input("What size pizza do you want? S, M or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()

SMALL_PIZZA_PRICE = 15
MEDIUM_PIZZA_PRICE = 20
LARGE_PIZZA_PRICE = 25
PEPPERONI_SMALL_PRICE = 2
PEPPERONI_MEDIUM_LARGE_PRICE = 3
EXTRA_CHEESE_PRICE = 1

total_payment = 0

if pizza_size == "s":
    total_payment += SMALL_PIZZA_PRICE
elif pizza_size == "m":
    total_payment += MEDIUM_PIZZA_PRICE
elif pizza_size == "l":
    total_payment += LARGE_PIZZA_PRICE

if add_pepperoni == "y":
    if pizza_size == "s":
        total_payment += PEPPERONI_SMALL_PRICE
    else:
        total_payment += PEPPERONI_MEDIUM_LARGE_PRICE
    
if extra_cheese == "y":
    total_payment += EXTRA_CHEESE_PRICE

print(f"Your final bill is: {total_payment}")