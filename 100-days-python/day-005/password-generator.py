import random
import string

# Print welcome statement
print("Welcome to the Password Generator")

# Take amount of letters in password
passwd_letters_len = int(input("\nHow many letters would you like in your password?\n"))

# Take amount of symbols in password
passwd_symbols_len = int(input("\nHow many symbols would you like?\n"))

# Take amount of numbers in password
passwd_digits_len = int(input("\nHow many numbers would you like?\n"))

# Generate password
password = ""

LETTERS = string.ascii_letters
DIGITS = string.digits
PUNCTUATIONS = string.punctuation

## define letters pool
letters_pool = ""
for _ in range(passwd_letters_len + 1):
    index = random.randint(0, len(LETTERS) - 1)
    letters_pool += LETTERS[index]

## define numbers pool
digits_pool = ""
for _ in range(passwd_digits_len + 1):
    index = random.randint(0, len(DIGITS) - 1)
    digits_pool += DIGITS[index]

## define symbols pool
symbols_pool = ""
for _ in range(passwd_symbols_len + 1):
    index = random.randint(0, len(PUNCTUATIONS) - 1)
    symbols_pool += PUNCTUATIONS[index]

## define all charcters pools
char_pool = letters_pool + digits_pool + symbols_pool

## assemble a password
for _ in range(len(char_pool)):
    index = random.randint(0, len(char_pool) - 1)
    password += char_pool[index]

print(password)