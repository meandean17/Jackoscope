import Cards



class PlayingCard:
    def __init__(self,rank,suit) -> None:
        self.rank = rank
        self.suit = suit


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