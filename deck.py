from random import shuffle, randint


class Deck():

    values = [2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
    suits = [u"\u2666", u"\u2665", u"\u2663", u"\u2660"]

    def __init__(self):
        self.deck = self.start_deck()
        self.shuffle_deck()

    def start_deck(self):
        deck = []

        for value in Deck.values:
            for suit in Deck.suits:
                deck.append(f"{value}{suit}")

        return deck

    def shuffle_deck(self):
        shuffle(self.deck)

    def deal_card(self):
        idx = randint(0, len(self.deck)-1)
        card = self.deck.pop(idx)
        return card


dc = Deck()
