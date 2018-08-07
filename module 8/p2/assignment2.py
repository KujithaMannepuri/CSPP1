'''sum of digits'''
# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in
# one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sumofdigits(num):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if num == 0:
        return 0
    return (num % 10) + sumofdigits(num // 10)
def main():
    '''sum of digits'''
    num = input()
    print(sumofdigits(int(num)))
if __name__ == "__main__":
    main()
