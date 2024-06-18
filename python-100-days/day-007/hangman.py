import random

# Define hangman pics
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Define list of words to choose from
words = ["table", "monitor", "refrigerator", "microvawe", "carpet", "kitchen", "computer", "camel", "lightning", "cocoa"]

# Choose word for game
word = random.choice(words)

# Type welcome
print("Welcome to HANGMAN game. Let's try guess a word...\n")

guesses = len(word)
pic_index = 0
letter_occurancies = list()

hidden_word = list()
for _ in range(len(word)):
    hidden_word.append("_")

while True:
    if pic_index > 6:
        print("Game over, player was hanged!")
        print(HANGMANPICS[6])
        break
    else:
        print(HANGMANPICS[pic_index])
        print(" ".join(hidden_word))

    guess_letter = input("\nType letter for guess: ")

    if guess_letter in word:
        for i in range(len(word)):
            if word[i] == guess_letter:
                hidden_word[i] = guess_letter
                guesses -= 1
        if "_" not in hidden_word:
            print(hidden_word)
            print("Player WINS!")
            break
        elif guesses <= 0:
            print("Player LOSE! Your guesses run out.")
    else:
        pic_index += 1
        