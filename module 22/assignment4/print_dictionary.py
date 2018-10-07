'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    dict1 = []
    for i in dictionary:
        for i[j] in dictionary:
            dict1 = dict1.append(i)
            dict1 = dict1.append(i[j])
    return dict1

def main():
    dictionary = eval(input())
    print(print_dictionary(dictionary))

if __name__ == '__main__':
    main()
