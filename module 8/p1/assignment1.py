'''factorial of a number'''
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one
#number and returns the factorial of given number.

# This function takes in one number and returns one number.

def fact(num):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if num in (1, 0):
        return 1
    return num * fact(num - 1)
def main():
    ''' factorial of a number'''
    num = input()
    print(fact(int(num)))
if __name__ == "__main__": 
    import sys
    sys.setrecursionlimit(25500)
    main()
