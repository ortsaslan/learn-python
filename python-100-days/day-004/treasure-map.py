# Define rows and map
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]

# Print a map
print(f"{row1}\n{row2}\n{row3}")

# Take position and put into it a treasure
position_input = input("Where do you want to put the treasure? Type two-digit number, first for row and second for column: ")
horizontal = int(position_input[0]) - 1
vertical = int(position_input[1]) - 1
map[horizontal][vertical] = "❎"

# Print map with treasure position
print(f"{map[0]}\n{map[1]}\n{map[2]}")
