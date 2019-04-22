# python 3
import random
import math



# BlackJack

face = 'K Q J T'.split()
nums = '9 8 7 6 5 4 3 2'.split()
ace = 'A'.split()


def dealCard():
    deck = face + nums + ace    
    return random.choice(deck)


def cardValue(card):
    value = 0
    
    if card in face:
        value = 10
        return value
    elif card in nums:
        value = int(card)   
        return value
    else:
        print('Ace')
        value = [1,11]
        return value
    


def dealPlayer(): 
    c1 = dealCard()
    c2 = dealCard()
    myCards = [c1,c2]
    return myCards

def hitMe(myCards):
    c = dealCard()
    myCards += c
    return myCards


def showMyCards(myCards):
    display = ''
    
    for item in myCards:
        display += item + ' '
    print('My Cards = %s' % display)
    print('My Total = %d' % cardTotal(myCards))


def cardTotal(myCards):
    total = 0
    for card in myCards:
        if card == 'A':
            if total + 11 > 21:
                total += 1
            elif total + 11 == 21:
                total += 11
            else:
                total += 11
        else:
            total += cardValue(card)
            
    return total



def main():
    
    heroCards = dealPlayer()
    heroTotal = cardTotal(heroCards)
    
    dealerCards = dealPlayer()
    dealerTotal = cardTotal(dealerCards)

    print('Dealer shows %s\n' % (dealerCards[0]))
    
    dealerDone = False
    heroDone = False

    while heroDone == False and dealerDone == False:
        
        while heroTotal != 0:
            if heroTotal > 21:
                print('Hero Busts')
                heroDone = True
                break
            elif heroTotal == 21:
                heroDone = True
                print('Hero gets BlackJack')               
                break
            elif heroTotal < 21:
                showMyCards(heroCards)
                print('Would you like to hit? (yes, no)')
                answer = input()
                answer = answer.lower()
                if answer.startswith('y'):
                    heroCards = hitMe(heroCards)
                    heroTotal = cardTotal(heroCards)
                else:
                    heroDone = True
                    break
        
        print('Dealer shows %s' % (dealerCards))
        
        while dealerTotal != 0:
            
            if dealerTotal > 21:
                print('Dealer Busts with %d' % (dealerTotal))
                dealerDone == True
                dealerTotal = 0
                break
            elif dealerTotal == 21:
                print('Dealer gets Blackjack with %d' % (dealerTotal))
                dealerDone == True
                break
            elif dealerTotal >= 17:
                print('Dealer must stay with %d' % (dealerTotal))
                dealerDone == True
                break
            elif dealerTotal < 17:
                dealerCards = hitMe(dealerCards)
                print('Dealer takes a card = %s' % (dealerCards[-1]))
                dealerTotal = cardTotal(dealerCards)
                   
        print('\nHero vs Dealer')
        print(' %d  vs   %d\n' % (heroTotal, dealerTotal))
        
        print('Hero = %s --> %d' % (heroCards, heroTotal))
        print('Dealer = %s --> %d' % (dealerCards, dealerTotal))       
        
                        
        if ((heroTotal > dealerTotal) and (heroTotal <= 21)):
            print('HERO WINS')
        elif ((heroTotal < dealerTotal) and (dealerTotal <= 21)):
            print('DEALER WINS')
        elif (heroTotal == dealerTotal):
            print('PUSH')
    
main()

