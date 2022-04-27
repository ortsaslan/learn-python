import random

print("H A N G M A N")

words = ["python", "java", "swift", "javascript"]

while True:
    random.seed()
    word = random.choice(words)
    user_in = input("Guess the word: ")
    if user_in == word:
        print("You survived!")
        break
    else:
        print("You lost!")