import random

from blackjack.core.card import Card


class Deck:
    def __init__(self):
        self.card_deck = []
        self.initiate_deck()

    def initiate_deck(self):
        for suit in range(1, 5):
            for value in range(1, 14):
                card = Card(value, suit)
                self.card_deck.append(card)

    def get_deck(self):
        return self.card_deck

    def shuffle_deck(self):
        random.shuffle(self.card_deck)
