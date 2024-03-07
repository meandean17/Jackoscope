import Cards
import json

class PlayingCard:
    def __init__(self,rank,suit) -> None:
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def to_dict(self):
        return {"rank": self.rank, "suit": self.suit}




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


def add(hand):
    hand_dict = [card.to_dict() for card in hand]
    # hand_dict = [{'rank': 'Queen', 'suit': 'Spades'}, {'rank': 'King', 'suit': 'Clubs'}]
    print("Data to be written:", hand_dict)
    try:
        with open("cards.json", "w") as outfile:
            json.dump(hand_dict, outfile)
        print("Data has been written to cards.json")
    except Exception as e:
        print(f"An error occurred: {e}")
    


  


def printHand(hand):
    for card in hand:
        print(card.rank,card.suit)
