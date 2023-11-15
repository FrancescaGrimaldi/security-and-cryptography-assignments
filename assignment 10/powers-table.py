from rsa_repeated_squaring import repeated_squaring as rs

# returns the exponentiation of n to the powers of 2 obtained from repeated_squaring
def exp(message, powers):
    result = 1
    for i in range(len(powers)):
        if powers[i] == 1:
            result *= message ** (2 ** i)
    return result

# prints all the powers of n from 1 to 100
def print_powers(n):
    print("All the powers " + str(n) + "^i for i=1, ..., 100")
    for i in range(1, 101):
        print(str(exp(n, rs(i))))

def main():
    print_powers(3)
    print()
    print_powers(5)

if __name__ == '__main__':
    main()
