import random
import string

# Print welcome statement
print("Welcome to the Password Generator")

# Take amount of letters in password
passwd_letters_len = int(input("\nHow many letters would you like in your password?\n"))

# Take amount of symbols in password
passwd_symbols_len = int(input("\nHow many symbols would you like?\n"))

# Take amount of digits in password
passwd_digits_len = int(input("\nHow many digits would you like?\n"))

# Generate password
## define list-variable for password
password = list()
passwd_len = passwd_letters_len + passwd_symbols_len + passwd_digits_len

for _ in range(passwd_len):
    password.append(0)

# define string-constants for all python letters, digits and punctuations
LETTERS = string.ascii_letters
DIGITS = string.digits
PUNCTUATIONS = string.punctuation

## define letters pool
letters_pool = ""
for _ in range(passwd_letters_len):
    letters_pool += random.choice(LETTERS)

## define numbers pool
digits_pool = ""
for _ in range(passwd_digits_len):
    digits_pool += random.choice(DIGITS)

## define symbols pool
symbols_pool = ""
for _ in range(passwd_symbols_len):
    symbols_pool += random.choice(PUNCTUATIONS)

## define all charcters pools
char_pool = letters_pool + digits_pool + symbols_pool

## assemble a password
for char in char_pool:
    while True:
        index = random.randint(0, len(password) - 1)
        if password[index] == 0:
            password[index] = char
            break
        continue

password = "".join(password)

# Print password
print(password)