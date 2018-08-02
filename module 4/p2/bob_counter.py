'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    string1 = input()
    string2 = 'bob'
    length1 = len(string1)
    length2 = len(string2)
    i, j, count = 0, 0, 0
    while i<length1-1:
        if string1[i] == string2[j]:
            j = j+1
            if j == len(string2)-1:
                j = 0
                count = count+1
                i = i-1
        i = i+1
    print (count)                   
if __name__== "__main__":
    main()
