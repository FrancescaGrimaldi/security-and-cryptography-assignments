import math

# returns true if n is a perfect square
def is_square(n):
    return math.sqrt(n) == math.ceil(math.sqrt(n))

# returns the 2 prime factors of n
def fermat_factorization(n):
    a = math.ceil(math.sqrt(n))
    b2 = a ** 2 - n
    
    step = 1

    while not is_square(b2):
        a = a + 1
        b2 = a ** 2 - n
        step += 1

    b = math.sqrt(b2)
    p = a + b
    q = a - b
    print("Found at step", step)

    return int(p), int(q)

def main():
    n = 1829
    print("Computing the factors of '" + str(n) + "' using Fermat's factorization algorithm...")
    print(str(fermat_factorization(n)))

if __name__ == '__main__':
    main()