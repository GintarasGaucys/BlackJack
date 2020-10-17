import random

cards = {1: "Ace", 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: "Jack", 12: "Queen", 13: "King"}
faces = {1: "Clubs", 2: "Spades", 3: "Diamonds", 4: "Hearts"}
value = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:10, 12:10, 13:10}

class Card:
    def __init__(self, num, face):
        self.card = num
        self.face = face
        self.cardstr = str(cards[self.card])
        self.facestr = str(faces[self.face])
        self.value = int(value[num])

    def getCard(self):
        return self.card

    def getFace(self):
        return self.facestr

    def getValue(self):
        return self.value

    def __str__(self):
        return self.cardstr + " of " + self.facestr

def checkifbustorbj():
    if valueplayer > 21:
        print("Bust! The player loses with a score of", valueplayer)
        done1 = True
        return True
    elif valueplayer < 21:
        return False
    elif valueplayer == 21:
        print("BLACKJACK!!! You win!")
        done1 = True
        return True


#Prints the cards ant their total value
def playerInfo():
    print("Your cards are: ")
    for i in playercards:
        print(str(i))
    print("Your score is:", valueplayer)
    print("")


def updatePlayerValues():
    valueplayer = 0
    for i in playercards:
        valueplayer = valueplayer + i.getValue()
    return valueplayer


def updateDealerValues():
    valuepc = 0
    for i in dealercards:
        valuepc = valuepc + i.getValue()
    return valuepc


#The dealer hits if value < 17 and stands if value > 17
def dealerChoice():
    if valuepc < 17:
        acard = dealCard()
        print("The dealer hit and drew", acard)
        dealercards.append(acard)
        return False
    elif valuepc >= 17:
        print("The dealer stood.")
        return True


#The first players choice (includes split)
def firstChoice():
    answer = input("Stand or hit? ")
    if answer.lower() == "stand":
        print("You stood.")
        return False
    elif answer.lower() == "hit":
        print("You hit.")
        acard = dealCard()
        print("You drew", acard)
        playercards.append(acard)
        return True
    elif answer.lower() == "split":
        if playercards[0].cardstr() == playercards[1].cardstr():
            print("You split.")
            playercards1 = [playercards[0]]
            playercards2 = [playercards[1]]
        else:
            print("To split your cards have to have the same number.\n")
            firstChoice()

def playerChoice():
    answer = input("Stand or hit? ")
    if answer.lower() == "stand":
        print("You stood.")
        return True
    elif answer.lower() == "hit":
        print("You hit.")
        acard = dealCard()
        print("You drew", acard)
        playercards.append(acard)
    return False


#Prints the dealers known card and its value
def dealerStartInfo():
    print("The dealer's known card is", dealercards[0])
    print("The dealer's score is", dealercards[0].getValue())


def dealerInfo():
    print("The dealers cards are: ")
    for i in dealercards:
        print(str(i))
    print("The dealer's score:", valuepc)
    print("")

# Reshuffles the deck
deck = []
def newDeck():
    for i in range(1, 14):
        for j in range(1, 5):
            deck.append(Card(i, j))
    return deck


# Deals a random card from the deck and removes the card from the deck list
def dealCard():
    if len(deck) == 1:
        dealtcard = deck[0]
        newDeck()
        return dealtcard
    elif len(deck) == 0:
        newDeck()
        return dealCard()
    else:
        idx = random.randrange(1, len(deck), 1)
        dealtcard = deck[idx]
        deck.pop(idx)
        return dealtcard


done = False
while not done:
    newDeck()
    print("\n****WELCOME TO BLACKJACK***\n")
    playercards = [dealCard(), dealCard()]
    dealercards = [dealCard(), dealCard()]
    valueplayer = updatePlayerValues()
    valuepc = updateDealerValues()
    playerInfo()
    print("")
    dealerStartInfo()
    #player choices
    if firstChoice():
        valueplayer = updatePlayerValues()
        if not checkifbustorbj():
            playerInfo()
            done1 = False
            while not done1:
                done1 = playerChoice()
                valueplayer = updatePlayerValues()
                if not checkifbustorbj():
                    playerInfo()
    #dealers turn
    dealerdone = False
    while not dealerdone:
        dealerdone = dealerChoice()
        valuepc = updateDealerValues()
    dealerInfo()

    if valuepc == 21:
        print("Blackjack! The dealer won.")
    elif valueplayer > valuepc and valueplayer < 21:
        print("You won!")
    elif valueplayer == valuepc:
        print("You tied!")
    elif valuepc > valueplayer and valuepc < 21:
        print("The dealer won.")
    elif valuepc > 21:
        print("The dealer busted! You won")



    answer = input("Play again? Y/N ").lower()
    if answer.lower() == "n":
        done = True
    elif answer.lower() == "y":
        pass
