'''biggest exercise'''
#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to
# the entry with the largest number of values associated with it.
# If there is more than one such entry, return any one of the matching keys.


def biggest(adict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    maxm = 0
    best = ""
    for index in adict:
        if len(adict[index]) > maxm:
            maxm = len(adict[index])
            best += index
    return best[-1]

def main():
    '''biggest exercise'''
    num = input()
    adict = {}
    for _ in range(int(num)):
        string = input()
        lgth = string.split()
        if lgth[0][0] not in adict:
            adict[lgth[0][0]] = [lgth[1]]
        else:
            adict[lgth[0][0]].append(lgth[1])
    print(biggest(adict))


if __name__ == "__main__":
    main()
    