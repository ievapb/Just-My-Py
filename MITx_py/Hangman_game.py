# Hangman game
#
# -----------------------------------
# Helper code
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

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for char in secretWord:
        if char in lettersGuessed:
            count += 1
    if len(secretWord) == count:
        return (True)
    else: 
        return (False)
# -----------------------------------
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess = []
    guessed = ' '
    for char in secretWord:
        if char in lettersGuessed:
            guess.append(char)
        else:
            guess.append(' _ ')
    return (guessed.join(guess))

# -----------------------------------
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    char1 = ''
    abc = string.ascii_lowercase
    for char in lettersGuessed:
        char1 = char
        abc = abc.replace(str(char1), '')
    return (abc)
    
# -----------------------------------
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
    ilgis = len(secretWord)
    print('Welcome to the game, Hangman!\n' + 'I am thinking of a word that is ' + str(ilgis) + ' letters long.')
    guesscount = 8
    guess = ' '
    g1 = ''
    lettersGuessed = []
    mistakesMade = 0
    availableLetters = ' '
    while guesscount > 0:
        if isWordGuessed(secretWord, lettersGuessed):
            break
        availableLetters = getAvailableLetters(lettersGuessed)
        print('-------------\n' + 'You have ' + str(guesscount) + ' guesses left.\n' + 'Available letters: ' + str(availableLetters))
        g1 = input('Please guess a letter: ')
        guess = g1.lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))
            else:
                print('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed)))
                guesscount -= 1
                mistakesMade += 1
                if (mistakesMade == ilgis) and (guesscount == 0):
                    break

    print('-------------\n')
    if (guesscount >= 0) and (isWordGuessed(secretWord, lettersGuessed)):
        print ('Congratulations, you won!')
    else:
        print ('Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.')



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
