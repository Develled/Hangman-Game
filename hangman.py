# Hangman game
#

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    g = ""
    for x in list(secretWord):
        if x in lettersGuessed:
            g += x
            
                
    if g == secretWord:
        return True
            
    else:
        return False        
        



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    missingWord = ""
    
    for x in list(secretWord):
        if x in lettersGuessed:
            missingWord += x
        
        else:
            missingWord += "_ "
            
       
    return missingWord
        


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alpha = list(string.ascii_lowercase)
    for x in list(string.ascii_lowercase):
        if x in lettersGuessed:
            alpha.remove(x)
            
    return ("".join(alpha))
    

def hangman(secretWord):
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
    lettersGuessed = []
    numGuesses = 8
    print ("Welcome to the game Hangman!\nI am thinking of a word that is " + str(len(secretWord)) + " letters long")
    while isWordGuessed(secretWord, lettersGuessed) == False:
        
        if numGuesses == 0:
            print("-----------\nSorry, you ran out of guesses. The word was " + secretWord +".")
            break
        
        print("-----------\nYou have " + str(numGuesses) + " guesses left\nAvailable Letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        guessLower = guess.lower()      
            
        if guessLower not in getAvailableLetters(lettersGuessed):
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
    
        elif guessLower in secretWord:
            lettersGuessed.append (guessLower)
            print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
              
        else:
            lettersGuessed.append (guessLower)
            numGuesses -= 1
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
           
    
    else:
        print("-----------\nCongratulations, you won!")





lettersGuessed = []
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
