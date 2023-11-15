from rsa_repeated_squaring import repeated_squaring as rs, power_rep_sqr as exp

# returns the common key obtained by A and B using Diffie-Hellman
def dh_common_key(a, b, n, p):
    
    print("Step 1:")
    a1 = exp(n, rs(a), p)
    print("Alice sends Bob", a1)
    b1 = exp(n, rs(b), p)
    print("Bob sends Alice " + str(b1) + "\n")

    print("Step 2:")
    ka = exp(b1, rs(a), p)
    print("Alice calculates", ka)
    kb = exp(a1, rs(b), p)
    print("Bob calculates " + str(kb) + "\n")

    if (ka == kb):
        print("--> " + str(ka) + " is the common key")
    else:
        print("The keys are not equal")

def main():
    # initialize parameters
    a = 33
    b = 65
    n = 3
    p = 101

    dh_common_key(a, b, n, p)

if __name__ == '__main__':
    main()