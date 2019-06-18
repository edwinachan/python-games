import random

initalHandSize = 2

class Card:

    colours = ['Red', 'Yellow', 'Green', 'Blue']
    numbers = ['dummy', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    #Define new object to represent a playing card
    #It will have attributes 'colour' and 'number'
    #Provide initialization method with optional parameters for each attribute
    
    def __init__(self, colour=0, number=1):
        self.colour = colour
        self.number = number

    def __str__(self):
         return (self.numbers[self.number] + " of " + self.colours[self.colour])


class Deck:

    #This initialization method creates the attribute 'cards' and creates a deck
    #of 40 cards
    #Each iteration creates a new instance of 'Card' (prev class) with the
    #current 'colour' and 'number' & appends that card to the 'cards' list
    
    def __init__(self):
        self.cards = []
        for colour in range(len(Card.colours)):
            for number in range(1,len(Card.numbers)):
                self.cards.append(Card(colour,number))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        rng = random.Random()
        rng.shuffle(self.cards)

    def isEmpty(self):
        return self.cards == []

    def pop(self):
        #Check if empty. If empty, last card in discard pile remains, but we take rest of pile, shuffle, and that now becomes new mydeck
        return self.cards.pop()
    
    def dealCards(self, numOfPlayers):
        for i in range(initalHandSize):
            for j in range(numOfPlayers):
                players[j].addCardToHand(self.cards.pop())
    
    def createPlayers(self, numOfPlayers):
        for i in range(1, numOfPlayers + 1):
            players.append(Player(input('Name player ' + str(i) + ': ')))
        print('\n')
        
            
class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name
        
    def addCardToHand(self, card):
        self.hand.append(card)

    def haveGo(self, myDeck):
        if len(self.hand) == 0:
            return True
        else:
            print("Top of discard pile: " + str(discardPile[-1])+ '\n')

        playOrNot = input('Do you wish to play (type: play) or pick up (type: pick) a card? ')

        if playOrNot == 'pick':
            self.addCardToHand(myDeck.pop())
            print("No matches made for " + self.name)
            print(str(self.hand[-1]) + " from the deck has been added to the hand\n")
            return False
        elif playOrNot == 'play':
            indexOfCard = int(input('What\'s the position of the card you want to play? ')) - 1
            card = self.hand[indexOfCard]
            if card.colour == discardPile[-1].colour or card.number == discardPile[-1].number:
                print(self.name + ' has matched with ' + str(card))
                self.hand.remove(card)
                discardPile.append(card)
                print('Remaining cards: '+ str([str(self.hand[i]) for i in range(len(self.hand))]) + "\n")
                if len(self.hand) == 0:
                    return True
                else:
                    return False
            else:
                print('No match was made, next player will go.\n')
                return False

    def __str__(self):
        s = ""
        for i in range(len(self.hand)):
            s += str(self.hand[i]) + "\n"
        return s


class Game:

    def playGame(self):
        playerGoing = random.randint(0,len(players))
        won = False
        while won == False:
            playerGoing = (playerGoing + 1) % len(players)
            print(str(players[playerGoing].name) + " is going")
            #print(str(players[playerGoing].name) + " has:\n" + str(players[playerGoing]))
            print(str(players[playerGoing].name) + " has:\n")
            playersHand = players[playerGoing].hand
            listOfCards = [str(i+1) + ': ' + str(playersHand[i]) + '\n' for i in range(len(playersHand))]
            print(''.join(listOfCards))
            won = players[playerGoing].haveGo(myDeck)
            #Needs to return True in order to break out of while loop
            if won == True:
                print(str(players[playerGoing].name) + " has won")
            

#Play the game
print('Welcome to Chuno! The rules of the game are simple, and pretty much identical to Uno.\n 1) The aim of the game is to get rid of all your cards!\n 2) Each player starts with two cards in their hand. \n 3) You can play if a card in your hand matches the a) colour or b) number of the top card on the discard pile. Doing so removes the card from your hand. \n 4) If you can\'t go, you must pick up a card from the deck. \n 5) Repeat until someone\'s hand is empty. \nHave fun!\n') 
numPlayers = int(input('How many players are there? '))
players = []      
myDeck = Deck()
myDeck.shuffle()
myDeck.createPlayers(numPlayers)
myDeck.dealCards(numPlayers)
discardPile = []
discardPile.append(myDeck.pop()) #Putting this right after we've dealt
#the cards as we only want to pop from myDeck at the start of the game
game = Game()
game.playGame()
