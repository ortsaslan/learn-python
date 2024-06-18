import random

# Take names from input
names_str = input("Type names, separated by a comma and space: ")

# Split string to list of names
names_lst = names_str.split(", ")

# Defining upper bound for random numbers generator
generator_ceil = len(names_lst) - 1

# Finding index randomly to choose a name
index = random.randint(0, generator_ceil)

# Define person who will pay
person_who_pays = names_lst[index]

# Print name of person who pays
print(f"{person_who_pays} is going to buy the meal today!")