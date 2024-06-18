import random

# Game title
print("H A N G M A N")
print()

# Messages for user
wrong_let_msg = "That letter doesn't appear in the word."
wrong_len_msg = "Please, input a single letter."
wrong_type_msg = "Please, enter a lowercase letter from the English alphabet."
guessed_let_msg = "You've already guessed this letter."
win_msg = "You guessed the word {}!\nYou survived!"
lost_msg = "You lost!"

# Initialize the game win and lost counters
count_win = 0
count_lost = 0

# English alphabet for input check
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Function finds and return all letter occurrences in word
def find_all_indxs(txt, lttr):
    indxs = []
    for i in range(len(txt)):
        if txt[i] == lttr:
            indxs.append(i)
    return indxs

# Game start point
while True:
    
    # Initialize word and it's dashed (hidden) version
    words = ["python", "java", "swift", "javascript"]
    random.seed()
    word = random.choice(words)
    hidden_word = ["-" for _ in word]

    # Initialize current game state variables:
    ## max invalid guesses and guessed letters
    attempts = 8
    guessed_lttrs = ""

    # Take user's input
    menu_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    
    # Start the game if user's choice - PLAY
    if menu_choice == "play":
        while True:
            # Check state for win and lost terms   
            if attempts == 0:
                print()
                print(lost_msg)
                count_lost += 1
                break
            if "-" not in hidden_word:
                print()
                print(word)
                print(win_msg.format(word))
                count_win += 1
                break
            
            # Check input and make relevant changes in state
            print("".join(hidden_word))
            letter = input("Input a letter: ")
            if len(letter) != 1:
                print(wrong_len_msg)
            elif letter not in alphabet:
                print(wrong_type_msg)
            elif letter.lower() in alphabet:
                if letter in guessed_lttrs:
                    print(guessed_let_msg)
                elif letter in word:
                    indxs = find_all_indxs(word, letter)
                    for i in range(len(indxs)):
                        hidden_word[indxs[i]] = letter
                    guessed_lttrs += letter
                else:
                    attempts -= 1
                    guessed_lttrs += letter
                    print(wrong_let_msg)        
            
            print()
    
    # Display win and lost statistics if user's choice - RESULTS
    elif menu_choice == "results":
        print(f"You won: {count_win} times")
        print(f"You lost: {count_lost} times")
    
    # End the game if user's choice - EXIT
    elif menu_choice == "exit":
        break

    else:
        continue