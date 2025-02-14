import random

class Card:
    def __init__(self, suit, value):
        # Each card has one suit and one value
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9','10', 'J', 'Q', 'K']
        self.cards = []
        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.cards.append(card) # total = 52

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError("Cannot shuffle. The deck is incomplete.")
        random.shuffle(self.cards)


    def deal(self):
        if len(self.cards) == 0:
            raise ValueError("No more cards to deal.")
        return self.cards.pop() # last card of cards
    
deck = Deck()
deck.shuffle()
for i in range (5):
    print(deck.deal())  # for example :
                        # 6 of Clubs
                        # 4 of Hearts
                        # J of Diamonds
                        # 8 of Spades
                        # 7 of Clubs 
print(len(deck.cards)) # 52 - 5 = 47