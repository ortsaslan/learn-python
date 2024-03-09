import random

# Take names from input
names_str = input("Type names, separated by a comma and space: ")

# Split string to list of names
names_lst = names_str.split(", ")

# Defigning upper bound for random numbers generator
generator_ceil = len(names_lst) - 1

# Finding index randomly to choose a name
index = random.randint(0, generator_ceil)

# Print name from names list
print(names_lst[index])