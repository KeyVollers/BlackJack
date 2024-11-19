import random

from blackjack.core.card import Card


class Deck:
    def __init__(self):
        self.draw_deck = []
        self.discard_deck = []
        self.initiate_deck()

    def initiate_deck(self):
        for suit in range(1, 5):
            for value in range(1, 14):
                card = Card(value, suit)
                self.draw_deck.append(card)

    def get_draw_deck(self):
        return self.draw_deck


    def get_discard_deck(self):
        return self.discard_deck

    def shuffle_draw_deck(self):
        random.shuffle(self.draw_deck)

    def draw_card(self):
        card = self.draw_deck.pop()
        self.discard_deck.append(card)
        return card
