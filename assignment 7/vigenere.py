import sys

def encrypt(input, key):
    encrypted_string = ""
    norwegian_alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

    input = input.lower()
    key = key.lower()
    key_pos = 0

    for char in input:
        if char in norwegian_alphabet:
            encrypted_string += norwegian_alphabet[(norwegian_alphabet.index(char) + norwegian_alphabet.index(key[key_pos])) % len(norwegian_alphabet)]
            key_pos += 1
            if key_pos == len(key):
                key_pos = 0

    encrypted_string = encrypted_string.upper()
    
    return encrypted_string

def decrypt(input, key):
    decrypted_string = ""
    norwegian_alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

    input = input.lower()
    key = key.lower()
    key_pos = 0

    for char in input:
        if char in norwegian_alphabet:
            decrypted_string += norwegian_alphabet[(norwegian_alphabet.index(char) - norwegian_alphabet.index(key[key_pos])) % len(norwegian_alphabet)]
            key_pos += 1
            if key_pos == len(key):
                key_pos = 0
        #else:
        #    decrypted_string += char
    
    return decrypted_string

def main():
    print("Welcome to the Vigenere Cipher program!")
    print("You can: \n 1. Encrypt a message \n 2. Decrypt a message (knowing the key) \n 3. Exit")
    choice = int(input())

    if choice == 1:
        print("Enter the text to encrypt:")
        text = str(input())
        print("Enter the keyword:")
        key = str(input())
        print("Your encrypted text is: " + encrypt(text, key))
    elif choice == 2:
        print("Enter the text to decrypt:")
        text = str(input())
        print("Enter the keyword that was used:")
        key = str(input())
        print("The plaintext is: " + decrypt(text, key))
    else:
        print("Exiting...")
        sys.exit(1)

if __name__ == '__main__':
    main()