import random

# Define Rock Paper Scissors ASCII Art
rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Define shapes art list
shapes_art = [rock_art, paper_art, scissors_art]

# Define shapes list to player choices
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
shapes = [ROCK, PAPER, SCISSORS]

# Take user choice for shape from input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
user_shape = shapes[user_choice]

# Take computer choice for shape from random number generator
comp_choice = random.randint(0, 2)
comp_shape = shapes[comp_choice]

# Print players choices
print(f"\nYou chose:\n{shapes_art[user_choice]}")
print(f"\nComputer chose:\n{shapes_art[comp_choice]}")

# Define a winner
USER = "User"
COMPUTER = "Computer"

winner = ""
game_result = ""

if user_shape == comp_shape:
    game_result = "Draw"

else:
    if user_shape == ROCK:
        if comp_shape == PAPER:
            winner = COMPUTER
        else: 
            winner = USER
    
    elif user_shape == PAPER:
        if comp_shape == SCISSORS:
            winner = COMPUTER
        else:
            winner = USER

    elif user_shape == SCISSORS:
        if comp_shape == ROCK:
            winner = COMPUTER
        else:
            winner = USER

    game_result = f"{winner} wins!"

# Print game result
print(game_result)
