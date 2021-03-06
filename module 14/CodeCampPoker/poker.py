'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def sort(hand):
    '''appwnding values to list'''
    len1 = len(hand)
    newhand = []
    for index in range(len1):
        if hand[index][0] == 'T':
            newhand.append(10)
        elif hand[index][0] == 'J':
            newhand.append(11)
        elif hand[index][0] == 'Q':
            newhand.append(12)
        elif hand[index][0] == 'K':
            newhand.append(13)
        elif hand[index][0] == 'A':
            newhand.append(14)
        else:
            newhand.append(int(hand[index][0]))
    return newhand
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    len1 = len(hand)
    sortlist = sorted(sort(hand))
    for index in range(len1 - 1):
        if sortlist[index+1] - sortlist[index] != 1:
            return False
    return True


def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    len1 = len(hand)
    for index in range(len1 - 1):
        if hand[index][1] != hand[index+1][1]:
            return False
    return True
def is_fourofakind(hand):
    ''' four face values'''
    count = 0
    sortlist = sorted(sort(hand))
    for i in range(len(sortlist)-3):
        if sortlist[i] == sortlist[i+1] == sortlist[i+2] == sortlist[i+3]:
            count += 1
    if count == 1:
        return True
    return False

def is_threeofakind(hand):
    '''three face values'''
    count = 0
    sortlist = sorted(sort(hand))
    for i in range(len(sortlist)-2):
        if sortlist[i] == sortlist[i+1] == sortlist[i+2]:
            count += 1
    if count == 1:
        return True
    return False

def is_onepair(hand):
    '''one pair values'''
    sortlist = sorted(sort(hand))
    setlist = set(sortlist)
    if len(sortlist) - len(setlist) == 1:
        for index in setlist:
            if sortlist.count(index) == 2:
                return index/10
    return 100

def is_twopair(hand):
    '''two pair values'''
    sortlist = sorted(sort(hand))
    setlist = set(sortlist)
    if len(sortlist) - len(setlist) == 2:
        return True
    return False

def is_fullhouse(hand):
    ''' three face values and two face values must be equal in a hand'''
    count = 0
    i = 0
    sortlist = sorted(sort(hand))
    if sortlist[i] == sortlist[i+1] == sortlist[i+2] or sortlist[i+3] == sortlist[i+4]:
        count += 1
    elif sortlist[i+3] == sortlist[i+4] and sortlist[i] == sortlist[i+1] == sortlist[i+2]:
        count += 1
    if count == 1:
        return True
    return False

def high_hand(hand):
    ''' high hand values'''
    sortlist = sorted(sort(hand))
    setlist = set(sortlist)
    if len(setlist) == 5 and not is_flush(hand):
        return max(setlist)/100
    return False

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    if is_straight(hand) and is_flush(hand):
        return 8
    if is_flush(hand):
        return 6
    if is_straight(hand):
        return 5
    if is_fourofakind(hand):
        return 4
    if is_threeofakind(hand):
        return 3
    if is_onepair(hand) != 100:
        return is_onepair(hand)
    if is_twopair(hand):
        return 2
    if is_fullhouse(hand):
        return 7
    return high_hand(hand)

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
