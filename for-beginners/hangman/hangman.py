import random

print("H A N G M A N")
print()

words = ["python", "java", "swift", "javascript"]
random.seed()
word = random.choice(words)
hidden_word = ["-" for _ in word]

wrong_let_msg = "That letter doesn't appear in the word."
repeat_let_msg = "No improvements."
win_msg = "You guessed the word!\nYou survived!"
lost_msg = "You lost!"
attempts = 8


def find_all_indxs(txt, lttr):
    indxs = []
    for i in range(len(txt)):
        if txt[i] == lttr:
            indxs.append(i)
    return indxs


while True:
    
    if attempts == 0:
        print()
        print(lost_msg)
        break
    if "-" not in hidden_word:
        print()
        print(word)
        print(win_msg)
        break

    print("".join(hidden_word))
    letter = input("Input a letter: ")
    if letter in word and letter in hidden_word:
        attempts -= 1
        print(repeat_let_msg)
    elif letter in word:
        indxs = find_all_indxs(word, letter)
        for i in range(len(indxs)):
            hidden_word[indxs[i]] = letter
    else:
        attempts -= 1
        print(wrong_let_msg)        
    
    print()