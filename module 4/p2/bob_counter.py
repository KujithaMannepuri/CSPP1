'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    '''string'''
    string = input()
    count = 0
    num = string.find('bob')
    while num >= 0:
        count = count+1
        num = string.find('bob', num+2)
    print(count)
if __name__ == "__main__":
    main()
