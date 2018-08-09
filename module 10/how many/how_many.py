'''how many'''
#Exercise : how many
# write a procedure, called how_many, which returns the sum of the
# number of values associated with a dictionary.


def how_many(adict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    sum1 = 0
    value = adict.values()
    for sublist in value:
        sum1 = sum1 + len(sublist)
    return sum1

def main():
    '''how many'''
    num = input()
    adict = {}
    for _ in range(int(num)):
        string = input()
        length = string.split()
        if length[0][0] not in adict:
            adict[length[0][0]] = [length[1]]
        else:
            adict[length[0][0]].append(length[1])
    print(how_many(adict))

if __name__ == "__main__":
    main()
