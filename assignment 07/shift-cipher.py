import sys

# encrypts a string shifting letters by a given number of places (forwards)
def encrypt(input, shift):
    encrypted_string = ""
    norwegian_alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

    input = input.lower()

    for char in input:
        if char in norwegian_alphabet:
            encrypted_string += norwegian_alphabet[(norwegian_alphabet.index(char) + shift) % len(norwegian_alphabet)]

    encrypted_string = encrypted_string.upper()

    return encrypted_string

# decrypts a string shifting its letters by a given number of places (backwards)
def decrypt(input, shift):
    decrypted_string = ""
    norwegian_alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

    input = input.lower()

    for char in input:
        if char in norwegian_alphabet:
            decrypted_string += norwegian_alphabet[(norwegian_alphabet.index(char) - shift) % len(norwegian_alphabet)]
        # else:
        #     decrypted_string += char

    return decrypted_string

# bruteforces the decryption of a string by trying all possible shifts
def bruteforce(input):
    for i in range(1, 30):
        print("Attempt with shift " + str(i) + ": " + decrypt(input, i))
        # write to file
        # f = open("bruteforce.txt", "a")
        # f.write(decrypt(input, i) + "\n")


def main():
    print("Welcome to the Shift Cipher program!")
    print("You can: \n 1. Encrypt a message \n 2. Decrypt a message (knowing the shift) \n 3. Brute force (to find the shift) \n 4. Exit")
    choice = int(input("What do you want to do? "))

    if choice == 1:
        print("Enter the text to encrypt:")
        text = str(input())
        print("Enter the shift:")
        shift = int(input())
        print("Your encrypted text is: " + encrypt(text, shift))
    elif choice == 2:
        print("Enter the text to decrypt:")
        text = str(input())
        print("Enter the shift that was used:")
        shift = int(input())
        print("The plaintext is: " + decrypt(text, shift))
    elif choice == 3:
        print("Enter the encrypted text:")
        text = str(input())
        bruteforce(text)
    else:
        print("Exiting...")
        sys.exit(1)

if __name__ == '__main__':
    main()
