# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    num = int(input())
    #your code here
    eps = 0.01
    root = num/2.0
    while abs(root*root-num) >= eps:
        root = root-(((root**2)-num)/(2*root))
    print(str(root))

if __name__ == "__main__":
    main()
