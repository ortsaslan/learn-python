# Program algorithm:
## Define alphabet
## Take input for operation type (encryption or decryption), message and shift
## Define two functions - encode for encryption and decode for decryption
## Implement shift algorithm (in both directions):
### - reference alphabet defined as List data-structure
### - each letter has it's own index and letters shifted by their indexes
### - if shift gone out of the List's length, excess length start it's counting from the beginning of the List
### - for encyption shift is addition, for decryption is substruction
## Define cipher function

import string


# Define encode function
def encode(alphabet, message, shift):
    encoded_msg = ""

    actual_index = 0
    for letter in message:
        actual_index = alphabet.index(letter)

        shifted_index = actual_index + shift
        if shifted_index > len(alphabet) - 1:
            encoded_msg += alphabet[shifted_index - len(alphabet)]
        else:
            encoded_msg += alphabet[shifted_index]

    return encoded_msg


# Define decode function
def decode(alphabet, message, shift):
    decoded_msg = ""

    shifted_index = 0
    for letter in message:
        shifted_index = alphabet.index(letter)

        actual_index = shifted_index - shift
        decoded_msg += alphabet[actual_index]

    return decoded_msg


# Define cipher function
def cipher():
    ALPHABET = string.ascii_lowercase + ".!? "
    result = ""

    action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message (only latin letters, whitespace and !/./?):\n").lower()
    shift = int(input("Type the shift number (from 1 to 29):\n"))

    if action == "encode":
        result = encode(ALPHABET, message, shift)
    elif action == "decode":
        result = decode(ALPHABET, message, shift)

    return result


# Execute app
print(cipher())
