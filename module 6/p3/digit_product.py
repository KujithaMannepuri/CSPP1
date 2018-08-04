'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    num = int(input())
    prdct = 1
    length = len(str(num))
    if num > 0:
        while num > 0:
            rem = num%10
            prdct = prdct*rem
            num = num // 10
        print(prdct)
    elif num < 0:
        for num in range(1, length, 1):
            while num > 0:
                rem = num%10
                prdct = prdct*rem
                num = num//10
        prdct1 = -int(prdct)
        print(prdct1)
    else:
        print('0')
if __name__ == "__main__":
    main()
