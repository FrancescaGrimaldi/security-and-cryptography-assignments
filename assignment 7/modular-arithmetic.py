import sys
import math

def calc_module(a, m):
    return a % m

def module_multiplication_table(num):
    for i in range (1, num):
        for j in range (1, num):
            print (calc_module(i*j, num), end = " ")
        print("\n")

def find_inverse(a, m):
    for i in range (1, m):
        print("Trying with", i, "as inverse: the result is", calc_module(a*i, m))
        if calc_module(a*i, m) == 1:
            return i
    return "No inverse found"

def main():
    print("This program performs modular arithmetic operations.")
    print("Choose what you want to do: \n 1. Calculate the module of a number \n 2. Print a multiplication table \n 3. Bruteforce the multiplicative inverse of a number \n 4. Exit")
    choice = int(input())

    if choice == 1:
        print("Enter a number:")
        a = int(input())
        print("Enter a module:")
        m = int(input())
        print("The module is", calc_module(a, m))
    elif choice == 2:
        print("Enter the number you want to print the multiplication table of:")
        num = int(input())
        module_multiplication_table(num)
    elif choice == 3:
        print("Enter a number:")
        a = int(input())
        print("Enter a module:")
        m = int(input())
        print("The multiplicative inverse to", a, "modulo", m, "is", find_inverse(a, m))
    else:
        print("Exiting...")
        sys.exit()


if __name__ == '__main__':
    main()