# returns the powers of 2 that add up to n
def repeated_squaring(x):
    powers = []
    while x > 0:
        powers.append(x & 1)    # appends the last bit of x to powers
        x >>= 1                 # shift x to the right by 1 bit
    return powers

# returns the exponentiation of n to the powers of 2 obtained from repeated_squaring
def power_rep_sqr(message, powers, n):
    result = 1
    for i in range(len(powers)):
        if powers[i] == 1:
            result *= message ** (2 ** i)
            result %= n         # do modulo n at each step to avoid overflow
    return result

# returns the binary representation of n
def dec_to_bin(n):
    return int(bin(n)[2:])

# returns the decimal representation of n
def bin_to_dec(n):
    return int(n, 2)

def main():
    # initialize RSA parameters
    n = 2600641
    e = 1731555
    d = 3
    message = "111"

    # retrieve the powers of 2 that add up to e to efficiently compute the encryption of the message
    print("Encrypting the message '" + message + "' with RSA using repeated squaring... ")
    powers = repeated_squaring(e)
    print("The powers of 2 that add up to " + str(e) + " are: " + str(powers))
    message = bin_to_dec("111")
    encrypted_message = power_rep_sqr(message, powers, n)
    print("Decimal value: " + str(encrypted_message))
    print("Binary value: " + str(dec_to_bin(encrypted_message)) + "\n")

    # retrieve the powers of 2 that add up to d to efficiently compute the decryption of the message
    print("Decrypting the message '" + str(encrypted_message) + "' with RSA using repeated squaring... ")
    powers = repeated_squaring(d)
    print("The powers of 2 that add up to " + str(d) + " are: " + str(powers))
    decrypted_message = power_rep_sqr(encrypted_message, powers, n)
    print("Decimal value: " + str(decrypted_message))
    print("Binary value: " + str(dec_to_bin(decrypted_message)))

if __name__ == '__main__':
    main()