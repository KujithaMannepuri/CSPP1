'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    '''tokenizing a string'''
    token = {}
    string = re.sub('[^A-Za-z0-9]+', ',', string)
    # string = string.split(',')
    for key in string:
        token[key] = token.get(key, 0) + 1
    return token   
def main():
    '''main function'''
    string = ''
    ip_lines = int(input())
    for index in range(ip_lines):
        index += 1
        string += input()
        string += '\n'
    print(tokenize(string))

if __name__ == '__main__':
    main()
