from itertools import product, groupby
from random import shuffle

class Suit(object):
    def __init__(self, display, text):
        self.display = display
        self.text = text

    def __str__(self):
        return self.display

class Card(object):
    numbers = [str(n) for n in range(2,11)]+['J','Q','K','A']
    suits = [Suit('♠','spade'), Suit('♥','heart'), Suit('♦','diamond'), Suit('♣','club')]
    values = {name:index for index,name in enumerate(numbers)}
    map_to_values = lambda ci: Card.values[ci.number]
    map_to_suits = lambda ci: {s:i for i,s in enumerate(Card.suits)}[ci.suit]

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.display = number+suit.display

    def __str__(self):
        return self.display

class Deck(object):
    def __init__(self):
        card_tuples = list(product(Card.numbers, Card.suits))
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
    hands = [deck.draw_cards(2) for _ in range(4)]
    table = deck.draw_cards(5)
    print("TABLE:\t"+" ".join(card_list(sorted(table, key=Card.map_to_values))))
    [get_matches(hand, table) for hand in hands]

def card_list(cards):
    return [card.display for card in cards]
def card_str(cards):
    return " ".join(card_list(cards))

def get_matches(hand, table):
    print(f" > {card_str(hand)}:")

    #Merge table and hand together + sort by value
    merged = sorted(hand + table, key=Card.map_to_values)

    #Find pairs through grouping by number
    for key, group in groupby(merged, Card.map_to_values):
        group = list(group)
        if len(group) == 2:
            print(f"\tPAIR: {card_str(group)}")
        elif len(group) == 3:
            print(f"\tTHREE OF A KIND: {card_str(group)}")
        elif len(group) == 4:
            print(f"\tFOUR OF A KIND: {card_str(group)}")

    #Find flushes through grouping by suit
    for key, group in groupby(merged, Card.map_to_suits):
        group = list(group)
        if len(group) >= 5:
            print(f"\tFLUSH: {card_str(group)}")

    n_card_windows = lambda data, n=5: [data[i:i+n] for i,_ in enumerate(data[:-n+1])]

    #Find straights by iterating through windows of n cards
    possible_straights = n_card_windows(Card.numbers)
    current_sequences = n_card_windows(merged)
    for s in current_sequences:
        if [c.number for c in s] in possible_straights:
            print(f"\tSTRAIGHT: {card_str(s)}")


if __name__ == "__main__":
    main()
