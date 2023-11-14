# returns the multiplicative inverse to a mod n
def euclid_ext(a, n):
    t = 0
    newt = 1
    r = n
    newr = a

    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r - quotient * newr)

    if r > 1:
        return "a is not invertible"
    if t < 0:
        t = t + n

    return t

def main():
    print(euclid_ext(3, 2597332))

if __name__ == '__main__':
    main()