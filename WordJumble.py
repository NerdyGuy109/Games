
import random

# Word Jumble

def get_secretWord(wordbank):
    return random.choice(wordbank)


def get_jumble(word):
    used = []

    while(len(used) < len(word)):
        n = random.randrange(0, len(word))
        if n not in used:
            used.append(n)

    output = ""

    for i in used:
        output += word[i]

    return output

def get_useranswer():
    print("Guess the word:")
    guess = input()
    return guess.lower()



def main():

    wordbank = ["happy", "puppy", "milk", "rooster", "pigeon"]
    
    secret = get_secretWord(wordbank)

    jumble = get_jumble(secret)

    numGuesses = 5

    guessList = []

    while(numGuesses >= 0):
        print("Jumble = %s" % jumble)
        guess = get_useranswer()
        if guess not in guessList:
            guessList.append(guess)

        if numGuesses == 0:
            print("--------- You Lose")
            
        if guess == secret:
            numGuesses = 0
            print("--------- You Win")
        else:
            numGuesses -= 1


          

    
main()
