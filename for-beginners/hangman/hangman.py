import random

# Game title
print("H A N G M A N")
print()

# Initialize word and it's dashed (hidden) version
words = ["python", "java", "swift", "javascript"]
random.seed()
word = random.choice(words)
hidden_word = ["-" for _ in word]

# Messages for user
wrong_let_msg = "That letter doesn't appear in the word."
wrong_len_msg = "Please, input a single letter."
wrong_type_msg = "Please, enter a lowercase letter from the English alphabet."
guessed_let_msg = "You've already guessed this letter."
win_msg = f"You guessed the word {word}!\nYou survived!"
lost_msg = "You lost!"

# Amount of max invalid guesses and guessed letters
attempts = 8
guessed_lttrs = ""

# English alphabet for input check
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Function finds and return all letter occurrences in word
def find_all_indxs(txt, lttr):
    indxs = []
    for i in range(len(txt)):
        if txt[i] == lttr:
            indxs.append(i)
    return indxs


while True:
    # Check state for win and lost terms   
    if attempts == 0:
        print()
        print(lost_msg)
        break
    if "-" not in hidden_word:
        print()
        print(word)
        print(win_msg)
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