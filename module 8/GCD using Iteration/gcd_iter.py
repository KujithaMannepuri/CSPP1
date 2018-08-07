'''gcd iteration'''
# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers
# and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcditer(num1, num2):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(1, small + 1):
        if ((num1 % i == 0) and (num2 % i == 0)):
            gcd = i
    return gcd

def main():
    '''gcd iteration'''
    data = input()
    data = data.split()
    print(gcditer(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
