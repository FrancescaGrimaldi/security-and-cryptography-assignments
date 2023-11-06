# returns the bitwise XOR of two numbers
def bitwise_xor(a, b):
    return a ^ b

# encrypts a character using the Caesar Cipher
def caesar_encrypt(char):
    return (char + 3) % 32

# decrypts a character using the Caesar Cipher
def caesar_decrypt(char):
    return (char - 3) % 32

alphabet = " abcdefghijklmnopqrstuvwxyzæøå,."
IV = 13

# encrypts a string using the CBC mode
def encrypt (plaintext):
    ciphertext = ""
    prev_block = IV

    for char in plaintext:
        char_index = alphabet.index(char)
        encr_char = caesar_encrypt(bitwise_xor(char_index, prev_block))
        prev_block = encr_char
        ciphertext += alphabet[encr_char]

    # divide into blocks of 5
    # ciphertext = ' '.join(ciphertext[i:i+5] for i in range(0, len(ciphertext), 5))

    return ciphertext

# decrypts a string using the CBC mode
def decrypt (ciphertext):
    plaintext = ""
    prev_block = IV

    for char in ciphertext:
        if char in alphabet:
            char_index = alphabet.index(char)
            decr_char = bitwise_xor(caesar_decrypt(char_index), prev_block)
            prev_block = char_index
            plaintext += alphabet[decr_char]

    return plaintext

def main():
    print("Encrypting 'aaaaaa'...")
    print(encrypt("aaaaaa") + '\n')

    print("Encrypting 'dette er en test'...")
    print(encrypt("dette er en test") + '\n')

    print("Decrypting 'qvxæyy hkgdgk,,oqhdnc'...")
    print(decrypt("qvxæyy hkgdgk,,oqhdnc"))

if __name__ == '__main__':
    main()