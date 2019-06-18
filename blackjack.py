#https://www.youtube.com/watch?v=qqp11XNMNRg

from random import shuffle

#Create the deck of cards
#Suits: H, S, D, C
#Ranks: A, 2-9, T(en), J, Q, K
#Returns a shuffled deck of cards

def deck():
    #Create empty list for the deck
    deck = []
    #Use a for loop to iterate through each suit and rank and append this
    #card to deck
    for suit in ['H', 'S', 'D', 'C']:
        for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']:
            deck.append(suit+rank)

    shuffle(deck)

    return(deck)

#Count the points for the cards given

def pointCount(myCards):
    myCount = 0
    aceCount = 0
    for i in myCards:
        #We use i[1] and not i[0] as we are interested in the ranks not the suits
        if (i[1] == 'T' or i[1] == 'J' or i[1] == 'Q' or i[1] == 'K'):
            myCount += 10
            #As Ace can be 1 or 11 depending on the hand, we will deal with it last
        elif (i[1] != 'A'):
            myCount += int(i[1])
        else:
            aceCount += 1

    if(aceCount == 1 and myCount <= 10):
        myCount += 11
    elif(aceCount != 0):
        myCount += 1

    return myCount

#Create the player and dealer's hands
#Randomly give them two cards each from the deck
#Return a list with both hands

def createPlayingHands(myDeck):
    dealerHand = []
    playerHand = []
    dealerHand.append(myDeck.pop())
    dealerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())

    while(pointCount(dealerHand) <= 16):
        dealerHand.append(myDeck.pop())

    return [dealerHand, playerHand]

#Create the game

game = ""
myDeck = deck()
hands = createPlayingHands(myDeck)
dealer = hands[0]
player = hands[1]
    
while(game != 'exit'):
    dealerCount = pointCount(dealer)
    playerCount = pointCount(player)

    print('Dealer has: ', dealer[0])
    print('Player has: ', player)

    if(playerCount == 21):
        print('Blackjack! Player wins!')
        break
    elif(playerCount > 21):
        print('Player busts with ', str(playerCount), ' points. Dealer wins!')
        break
    elif(dealerCount > 21):
        print('Dealer busts with ', str(dealerCount), ' points. Player wins!')
        break

    game = input('What would you like to do? H: Hit me, or S: Stand?')

    if(game == 'H'):
        player.append(myDeck.pop())
    elif(playerCount > dealerCount):
        print('Player wins with ', str(playerCount), ' points')
        print('Dealer has: ', str(dealer), ' points')
        break
    else:
        print('Dealer wins!')
        print('Dealer has: ', str(dealer), ' or ', str(dealerCount), ' points')
        print('Player has: ', str(playerCount), ' points')
        break
