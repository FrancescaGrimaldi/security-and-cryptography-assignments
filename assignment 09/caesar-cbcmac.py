x1 = "1101111110100001"
x2 = "0010110000011111"

# returns the bitwise XOR of two numbers
def bitwise_xor(a, b):
    a = int(a, 2)
    return a ^ b

# encrypts a block using the Caesar Cipher
def caesar_encrypt(dec_block):
    encrypted_block = (dec_block + 3) % (2 ** 8)
    return bin(encrypted_block)[2:].zfill(8)

# returns the CBC-MAC of a message
def cbc_mac(message, block_len, num_blocks):
    IV = "00000000"
    y = IV
    k = 0

    for i in range(0, num_blocks):
        x = int(message[k:k+block_len], 2)
        print("block_" + str(i) + ": " + str(x) + " (" + message[k:k+block_len] + ")")
        y = caesar_encrypt(bitwise_xor(y, x))
        print("y_" + str(i) + ": " + y + "\n")
        k = k+block_len

    return y

def main():
    print("Calculating CBC-MAC of message x = '1101 1111 1010 0001'...")
    print("CBC-MAC = " + cbc_mac(x1, 8, 2) + "\n")
    print("Calculating CBC-MAC of message x' = '0010 1100 0001 1111'...")
    print("CBC-MAC = " + cbc_mac(x2, 8, 2) + "\n")

if __name__ == '__main__':
    main()