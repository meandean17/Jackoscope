import Cards


class PlayingCard:
    def __init__(self,rank,suit) -> None:
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"




def buildDeck():
    deck= []

    suits = ['Hearts','Spades','Clubs','Diamonds']
    ranks = ['Ace','Two','Three','Four','Five','Six','Seven','Eight',
                'Nine','Ten','Jack','Queen','King']

    for s in suits:
        for r in ranks:
            c = PlayingCard(r,s)
            deck.append(c)

    return deck

def deckChange(deck,rank, suit):
    for d in deck:
        if (d.rank == rank) & (d.suit == suit):
            # print(f"{d.rank} of {d.suit} heloooooooooooooo")
            deck.remove(d) 
    return deck

    
def printDeck(deck):
    for d in deck:
        print(d.rank,d.suit)

def createCard(rank,suit):
    return PlayingCard(rank,suit)


def createHand(deck):
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    hand = []

    # Iterate through all possible combinations of suits and ranks
    for s in suits:
        for r in ranks:
            # Check if the card with current suit and rank is not in the deck
            if not any(card.rank == r and card.suit == s for card in deck):
                # If not present in the deck, create the card and add it to the hand
                card = createCard(r, s)
                hand.append(card)
                
    return hand


  


def printHand(hand):
    for card in hand:
        print(card.rank,card.suit)
