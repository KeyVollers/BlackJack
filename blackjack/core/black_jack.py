from blackjack.core.deck import Deck


class BlackJack:
    def __init__(self):
        self.game_deck = Deck()

    def get_game_deck(self):
        return self.game_deck
