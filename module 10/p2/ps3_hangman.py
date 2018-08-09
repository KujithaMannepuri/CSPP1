'''Hangman game'''
# Hangman game
#
# ----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadwords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    infile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = infile.readline()
    # wordlist: list of strings
    wordlist1 = line.split()
    print("  ", len(wordlist1), "words loaded.")
    return wordlist1
def testinput(guess):
    '''guess word'''
    if len(guess) > 1 or (guess <= 'a' and guess >= 'z'):
        print("Invalid")
        return False
    return True
def chooseword(word_list1):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(word_list1)

# end of helper code
# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadwords()

def iswordguessed(secretword, lettersguessed):
    '''
    secretword: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretword are in lettersguessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    for index in secretword:
        if index in lettersguessed:
            count += 1
    if count == len(secretword):
        return True
    return False


def getguessedword(secretword, lettersguessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    lst = []
    for index in secretword:
        if index in lettersguessed:
            lst.append(index)
        else:
            lst.append('_')
    return ''.join(lst)


def getavailableletters(lettersguessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    string = string.ascii_lowercase
    rslt = ''
    for index in string:
        if index in lettersguessed:
            continue
        else:
            rslt += index
    return rslt

def hangman(secretword):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to Hangman game")
    lettersguessed = []
    print("I am thinking of a word that is", len(secretword), "letter word")
    print("-----------------")
    flag = False
    maxguessletters = len(secretword) + 5
    print(getguessedword(secretword, lettersguessed))
    while maxguessletters != 0:
        print("you still have", maxguessletters, "letters")
        print("available letters: ", getavailableletters(lettersguessed))
        guess = input("guess a letter:")
        maxguessletters -= 1

        if not testinput(guess):
            continue
        lettersguessed.append(guess)
        flag = iswordguessed(secretword, lettersguessed)
        if flag:
            break
        print(getguessedword(secretword, lettersguessed))
    if flag:
        print("congratulations the word you guessed is correct")
    print("Try again...!")





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseword(wordlist).lower()
hangman(secretWord)
