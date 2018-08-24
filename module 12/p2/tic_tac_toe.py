'''Tic_Tac_Toe Game'''

def play_game(data):
    '''Checking the game winner'''
    s_a = set()
    s_b = set()
    s_c = set()
    s_d = set()
    s_e = set()
    len_1 = len(data)
    for i in range(len_1):
        for j in range(len(data[i])):
            # horizontal elements
            set1 = set(data[i])
            if len(set1) == 1:
                if 'x' in set1:
                    return 'x'
                return 'o'
            # vertical elements
            if j == 0:
                s_a.add(data[i][j])
            if j == 1:
                s_b.add(data[i][j])
            if j == 2:
                s_c.add(data[i][j])
            # diagonal elements
            if i == j:
                s_d.add(data[i][j])
            if i + j == (len(data)-1):
                s_e.add(data[i][j])
    if len(s_a) == 1:
        return loop(s_a)
    if len(s_a) == 1:
        return loop(s_a)
    if len(s_a) == 1:
        return loop(s_a)
    if len(s_a) == 1:
        return loop(s_a)
    if len(s_a) == 1:
        return loop(s_a)
    return "draw"

def loop(set_1):
    '''Checking Set Values and elements'''
    if 'x' in set_1:
        return 'x'
    return 'o'

def check_game(data):
    ''' To check the inputs of game'''
    element1 = 'x'
    element2 = 'o'
    element3 = '.'
    count1 = 0
    count2 = 0
    count3 = 0
    for index in data:
        if len(index) != 3:
            return "invalid game"
        if element1 in index:
            count1 += index.count(element1)
        if element2 in index:
            count2 += index.count(element2)
        if element3 in index:
            count3 += index.count(element3)
    if abs(count1 - count2) != 1:
        return "invalid input"
    if count1 + count2 + count3 != 9:
        return "invalid input"
    return play_game(data)
def main():
    '''main function'''
    lst = []
    for _ in range(3):
        input_1 = input()
        input_1 = list(map(str, input_1.split(' ')))
        lst.append(input_1)
    lst = check_game(lst)
    print(lst)
if __name__ == '__main__':
    main()
