# keys
K1 = "0123456789ABCDEF0123456789ABCDEF"
K2 = "1123456789ABCDEF0123456789ABCDEF"

# plaintexts
x1 = "0100000000000000000000000000000"
x2 = "0200000000000000000000000000000"

# returns the binary representation of a hex string
def hex_to_bin(hex):
    return bin(int(hex, 16))[2:].zfill(128)

# returns the hex representation of a binary string
def bin_to_hex(bin):
    return hex(int(bin, 2))[2:].zfill(32)

# returns the decimal representation of a hex string
def hex_to_dec(hex):
    return int(hex, 16)

# returns the hex representation of a decimal string
def dec_to_hex(dec):
    return hex(dec)[2:].zfill(32)

# compares two binary strings and returns the number of different bits
def compare_bits(bin1, bin2):
    diff = 0
    for i in range (0, len(bin1)):
        if bin1[i] != bin2[i]:
            diff += 1
    return diff

# compares two binary ciphertexts and prints the number and percentage of different bits (for diffusion and confusion)
def compare(bin1, bin2):
    differences = compare_bits(bin1, bin2)
    print("The number of different bits between the two ciphertexts is " + str(differences))
    percentage = differences / 128 * 100
    print("In percentage, " + str(percentage) + "%\n")

# encrypts a plaintext using a one time pad
def one_time_pad(plaintext, key):
    ciphertext = ""
    bin_plaintext = hex_to_bin(plaintext)
    bin_key = hex_to_bin(key)

    for i in range(0, 128):
        ciphertext += str(int(bin_plaintext[i]) ^ int(bin_key[i]))
        
    return ciphertext

# encrypts a plaintext using an affine cipher
def affine_cipher(plaintext, a, b):
    a = hex_to_dec(a)
    b = hex_to_dec(b)

    ciphertext = (a*hex_to_dec(plaintext) + b)%(2**128)

    # print('a = ' + str(a)) 
    # print('b = ' + str(b))
    # print('plaintext = ', hex_to_dec(plaintext))
    # print('ciphertext = ' + str(ciphertext))

    return dec_to_hex(ciphertext)

def main():
    print("PART A - Encrypting x1 and x2 using K1")
    
    print("A1. ONE TIME PAD")
    en_x1 = one_time_pad(x1, K1)
    en_x2 = one_time_pad(x2, K1)
    print("x1 -> " + bin_to_hex(en_x1))
    print("x2 -> " + bin_to_hex(en_x2))
    # diffusion
    compare(en_x1, en_x2)
    
    print("A2. AFFINE CIPHER")
    en_x1 = affine_cipher(x1, K1, K1)
    en_x2 = affine_cipher(x2, K1, K1)
    print("x1 -> " + en_x1)
    print("x2 -> " + en_x2)
    # diffusion
    compare(hex_to_bin(en_x1), hex_to_bin(en_x2))
    
    print("A3. ONE ROUND OF AES")
    # results obtained using cryptools.org
    en_x1 = "b3543dccec87235705c3aa65640fabdf"
    en_x2 = "834c25e4ec87235705c3aa65640fabdf"
    print("x1 -> " + en_x1)
    print("x2 -> " + en_x2)
    # diffusion
    compare(hex_to_bin(en_x1), hex_to_bin(en_x2))

    print("A4. FULL AES")
    # results obtained using cryptools.org
    en_x1 = "0694267ba398480c6b2b9f649be476cb"
    en_x2 = "282f7b11019800f8a978c6f750827ab5"
    print("x1 -> " + en_x1)
    print("x2 -> " + en_x2)
    # diffusion
    compare(hex_to_bin(en_x1), hex_to_bin(en_x2))

    print("PART B - Encrypting x1 using K1 and K2")

    print("B1. ONE TIME PAD")
    en_wk1 = one_time_pad(x1, K1)
    en_wk2 = one_time_pad(x1, K2)
    print("x1 using K1 -> " + bin_to_hex(en_wk1))
    print("x1 using K2 -> " + bin_to_hex(en_wk2))
    # confusion
    compare(en_wk1, en_wk2)
    
    print("B2. AFFINE CIPHER")
    en_wk1 = affine_cipher(x1, K1, K1)
    en_wk2 = affine_cipher(x1, K2, K2)
    print("x1 using K1 -> " + en_wk1)
    print("x1 using K2 -> " + en_wk2)
    # confusion
    compare(hex_to_bin(en_wk1), hex_to_bin(en_wk2))

    print("B3. ONE ROUND OF AES")
    # results obtained using cryptools.org
    en_wk1 = "b3543dccec87235705c3aa65640fabdf"
    en_wk2 = "eafd942cfc87235715c3aa65740fabdf"
    print("x1 using K1 -> " + en_wk1)
    print("x1 using K2 -> " + en_wk2)
    # confusion
    compare(hex_to_bin(en_wk1), hex_to_bin(en_wk2))

    print("B4. FULL AES")
    # results obtained using cryptools.org
    en_wk1 = "0694267ba398480c6b2b9f649be476cb"
    en_wk2 = "7af49a8defad94fa27cb03ac9f1c149a"
    print("x1 using K1 -> " + en_wk1)
    print("x1 using K2 -> " + en_wk2)
    # confusion
    compare(hex_to_bin(en_wk1), hex_to_bin(en_wk2))


if __name__ == '__main__':
    main()