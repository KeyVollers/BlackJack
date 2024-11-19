from blackjack.core.deck import Deck
from blackjack.utils.logger import print_deck


def main():
    deck1 = Deck()
    print_deck(deck1.get_deck())


if __name__ == '__main__':
    main()
