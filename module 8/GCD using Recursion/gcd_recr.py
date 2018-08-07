''' gcd recursion'''
# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b), that takes in
# two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdrecur(num1, num2):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if num2 == 0:
        return num1
    return gcdrecur(num2, num1%num2)
def main():
    ''' gcd recursion'''
    data = input()
    data = data.split()
    print(gcdrecur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
