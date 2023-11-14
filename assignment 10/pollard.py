import math

def pollard(a, b, n):
    A = (a ** math.factorial(b)) % n
    f = math.gcd(A - 1, n)
    
    if f > 1:
        return f
    else:
        return "The algorithm failed to find a factor of n"
    
def main():
    n = 18779
    b = 7
    print("Computing the factor of '" + str(n) +"' using Pollard's p-1 algorithm...")
    for a in range(2, 20):
        print("with a = " + str(a) + ": " + str(pollard(a, b, n)))
        
if __name__ == '__main__':
    main()