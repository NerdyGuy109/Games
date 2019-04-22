
import random

# Hangman


def get_secretWord(wordbank):
    return random.choice(wordbank)

def get_blankstring(word):
    output = ""
    for char in word:
        if char in alphabet:
            output += "_"
        if char == " ":
            output += " "
    return output

def get_userguess(guessList):
    guess = input("Guess a Letter --> ")
    if guess not in guessList:
        return guess
    else:
        print("Input Error --- this was already guessed")
        return None


def findIndexes(letter, word):
    L = []
    i = 0
    for char in word:
        if char == letter:
            L.append(i)
        i += 1
    return L

def replaceIndexes(indexList, secretWord):
    update = ""

    for i in range(0, len(secretWord)):
        if i in indexList:
            update += secretWord[i]
        else:
            update += "_"

    return update

def guessingAccuracy(guessList, secretWord):
    incorrect = 0
    for guess in guessList:
        if guess not in secretWord:
            incorrect += 1
    return incorrect

    

def draw(incorrect):
    pics = {
        0: """
            ------------------------------------
            ------------------------------------
            ------------------------------------
            ------------------------------------
            ------------------------------------
            ------------------------------------
            ------------------------------------
        """,
        1: """
            ------------------------------------
            --------[]--------------------------
            ------------------------------------
            ------------------------------------
            ------------------------------------
            ------------------------------------
        """,
        2: """
            ------------------------------------
            --------[]--------------------------
            --------()--------------------------
            ------------------------------------
            ------------------------------------
            ------------------------------------
        """,
        3: """
            ------------------------------------
            --------[]--------------------------
            --------()/-------------------------
            ------------------------------------
            ------------------------------------
            ------------------------------------
        """,
        4: """
            ------------------------------------
            --------[]--------------------------
            -------\()/-------------------------
            ------------------------------------
            ------------------------------------
            ------------------------------------
        """,
        5: """
            ------------------------------------
            --------[]--------------------------
            -------\()/-------------------------
            --------()--------------------------
            ------------------------------------
            ------------------------------------
        """,
        6: """
            ------------------------------------
            --------[]--------------------------
            -------\()/-------------------------
            --------()--------------------------
            -------/----------------------------
            ------------------------------------
        """,
        7: """
            ------------------------------------
            --------[]-------------YOU LOSE-----
            -------\()/-------------------------
            --------()--------------------------
            -------/--\-------------------------
            ------------------------------------
        """,        
        }

    return(pics[incorrect])


                

wordbank = "pulp, mississippi, hamster, potash, happy, climb, zebra".split(", ")

alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()


def main():
    secretWord = get_secretWord(wordbank)

    blank = get_blankstring(secretWord)

    clue = blank
    guessList = []
    print("Clue:  %s" % clue)

    while (("_" in clue) or (incorrect >= 7)):
        guess = get_userguess(guessList)
        if guess == None:
            continue
        else:
            guessList.append(guess)

        incorrect = guessingAccuracy(guessList, secretWord)
        drawing = draw(incorrect)

        indexList = []
        for guess in guessList:
            L = findIndexes(guess, secretWord)
            indexList += L

        clue = replaceIndexes(indexList, secretWord)

        if "_" not in clue:
            print("You Won!!")

        print("Clue:  %s" % clue)
        print(guessList)
        print(drawing)



main()

            
        
    
    

