import sys

def print_sequence():
    norwegian_alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

    for i in range(0, 29):
        print("f(", i, norwegian_alphabet[i], ") =", (11*i-5)%29, "which corresponds to letter", norwegian_alphabet[(11*i-5)%29])

def print_inverse_sequence():
    norwegian_alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

    for i in range(0, 29):
        print("f^-1(", i, norwegian_alphabet[i], ") =", (8*(i+5))%29, "which corresponds to letter", norwegian_alphabet[(8*(i+5))%29])

def encrypt(str):
    norwegian_alphabet = "abcdefghijklmnopqrstuvwxyzæøå"
    encrypted_string = ""

    str = str.lower()

    for char in str:
        if char in norwegian_alphabet:
            encrypted_string += norwegian_alphabet[(11*norwegian_alphabet.index(char)-5)%29]
    
    encrypted_string = encrypted_string.upper()

    return encrypted_string

def decrypt(str):
    norwegian_alphabet = "abcdefghijklmnopqrstuvwxyzæøå"
    decrypted_string = ""

    str = str.lower()

    for char in str:
        if char in norwegian_alphabet:
            decrypted_string += norwegian_alphabet[(8*(norwegian_alphabet.index(char)+5))%29]
    
    return decrypted_string


def main():
    print("This program solves task 2 of assignment 7")
    print("Press 1 for encryption, 2 for decryption, 3 to exit")
    choice = int(input())
    if choice == 1:
        print("The encryption key is f(x) = (11*x-5)mod 29")
        print_sequence()
        print("Enter the string to encrypt:")
        string = str(input())
        print("The encrypted string is:", encrypt(string))
    elif choice == 2:
        print("The decryption key is f^-1(x) = (8*(x+5))mod 29")
        print_inverse_sequence()
        print("Enter the string to decrypt:")
        string = str(input())
        print("The decrypted string is:", decrypt(string))
    else:
        print("Exiting...")
        sys.exit(1)

if __name__ == '__main__':
    main()