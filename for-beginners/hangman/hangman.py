import random

print("H A N G M A N")
print()

words = ["python", "java", "swift", "javascript"]
random.seed()
word = random.choice(words)
hidden_word = ["-" for _ in range(len(word))]

wrong_let_msg = "That letter doesn't appear in the word."
game_end_msg = "Thanks for playing!"
attempts = 8


def find_all_indxs(txt, lttr):
    indxs = []
    for i in range(len(txt)):
        if txt[i] == lttr:
            indxs.append(i)
    return indxs


while True:
    
    if attempts == 0:
        print(game_end_msg)
        break

    print("".join(hidden_word))
    letter = input("Input a letter: ")
    if letter in word:
        indxs = find_all_indxs(word, letter)
        for i in range(len(indxs)):
            hidden_word[indxs[i]] = letter
    else:
        print(wrong_let_msg)
    
    print()
    
    attempts -= 1