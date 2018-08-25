'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''main function to read input'''
    string = ''
    ip_lines = int(input())
    for index in range(ip_lines):
        index += 1
        string += input()
        string += '\n'
    print(string)

if __name__ == '__main__':
    main()
