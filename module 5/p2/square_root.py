# Write a python program to find the square root of the given number
'''square root exception'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''square root exception'''
    square = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    step = 0.1
    sroot = 0.0
    # your code starts here
    while abs(sroot**2 - square) >= epsilon:
        sroot += step
    if abs(sroot**2-square) >= epsilon:
        print()
    else:
        print(sroot)

if __name__ == "__main__":
    main()
