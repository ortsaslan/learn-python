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

## define string-constants for letters, digits and punctuations
LETTERS = string.ascii_letters
DIGITS = string.digits
PUNCTUATIONS = string.punctuation

## add letters to password
for _ in range(passwd_letters_len):
    password.append(random.choice(LETTERS))

## add digits to password
for _ in range(passwd_digits_len):
    password.append(random.choice(DIGITS))

## add symbols to password
for _ in range(passwd_symbols_len):
    password.append(random.choice(PUNCTUATIONS))

## randomize assembled password and join it to string
random.shuffle(password)
password = "".join(password)

# Print password
print(password)
