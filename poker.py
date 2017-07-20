from itertools import product
from random import shuffle

class Suit(object):
    def __init__(self, display, text):
        self.display = display
        self.text = text

    def __str__(self):
        return self.display

class Card(object):
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.display = number+suit.display

    def __str__(self):
        return self.display

class Deck(object):
    def __init__(self):
        self.suits = [
            Suit('♠','spade'),
            Suit('♥','heart'),
            Suit('♦','diamond'),
            Suit('♣','club')]
        self.numbers = [str(n) for n in range(2,10)]+['J','Q','K','A']
        card_tuples = list(product(self.numbers, self.suits))
        self.cards = [Card(n,s) for n,s in card_tuples]

    def shuffle(self):
        shuffle(self.cards)

    def draw_cards(self, number):
        cards = [self.cards.pop() for _ in range(number)]
        return cards

    def return_cards(self, cards):
        self.cards = cards + self.cards

def main():
    deck = Deck()
    deck.shuffle()
    hand = deck.draw_cards(2)
    [print(c) for c in hand]

if __name__ == "__main__":
    main()
