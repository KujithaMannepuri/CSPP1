'''Guess My Number Exercise'''

def main():
    #your code here
    '''guess a number'''
    mid = 50
    first = 0
    last = 100
    inp = 'l'
    while inp != 'c':
        print(mid)
        inp = input(" ")
        if inp == 'h':
            last = mid
            mid = (last + first) // 2
        elif inp == 'l':
            first = mid
            mid = (last + first) //  2
    print('your guess number is :', mid)
if __name__ == "__main__":
    main()
