print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

choice_turn = input("You're at a crossroad, where do you want to go? Type 'left' or 'right': ").lower()
if choice_turn == "right":
    print("Game over! You fell off a cliff.")
elif choice_turn == "left":
    print("Well done! The game continues...")
    choice_pool = input("You're reach a pool. Do you swim or wait? Type 'swim' or 'wait': ").lower()
    if choice_pool == "swim":
        print("Game over! Pool was full of fire🔥.")
    elif choice_pool == "wait":
        print("Well done! The game continues...")
        choice_door = input("You're at three doors - Red, Blue and Yellow. Choose one. Type 'red', 'blue' or 'yellow': ").lower()
        if choice_door == "red":
            print("Game over! A bricks🧱 fell on your head.")
        elif choice_door == "blue":
            print("Game over! You were eaten by a bear🐻.")
        elif choice_door == "yellow":
            print("You are WIN the game! Take your treasure chest👑.")