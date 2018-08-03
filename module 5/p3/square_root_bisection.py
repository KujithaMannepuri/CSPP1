# Write a python program to find the square root of the given number
'''square root bisection'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''square root bisection '''
    num = int(input())
    # epsilon and step are initialized
    # don't change these values
    eps = 0.01
    low = 0.0
    high = num
    rslt = (high + low) / 2.0

    while abs(rslt**2-num) >= eps:
        if rslt**2 < num:
            low = rslt
        else:
            high = rslt
        rslt = (high + low) / 2.0
    print(str(rslt) )
if __name__ == "__main__":
    main()
