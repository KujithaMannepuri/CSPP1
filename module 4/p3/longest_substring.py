'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s
in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem,
we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
    ''' substring '''
    string1 = input()
    length = len(string1)
    maxcount = " "
    for i in range(length):
        string2 = " "
        temp = string1[i]
        for j in range(i, length):
            if temp <= string1[j]:
                temp = string1[j]
                string2 += temp
            else:
                break
        if len(maxcount) < len(string2):
            maxcount = string2
    print(maxcount)

if __name__ == "__main__":
    main()
