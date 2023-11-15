import math
from rsa_repeated_squaring import repeated_squaring as rs, power_rep_sqr as exp

# returns a prime factor of n using Pollard (p-1) algorithm
def pollard(a, b, n):
    A = exp(a, rs(math.factorial(b)), n)    # a^(b!) is evaluated with repeated squaring
    f = math.gcd(A - 1, n)
    
    if f > 1:
        return f
    else:
        return "The algorithm failed to find a factor of n"
    
def main():
    # initialize parameters
    n = 18779
    b = 7
    
    print("Computing the factor of '" + str(n) +"' using Pollard (p-1) algorithm...")
    for a in range(2, 20):
        print("with a = " + str(a) + ": " + str(pollard(a, b, n)))
        
if __name__ == '__main__':
    main()