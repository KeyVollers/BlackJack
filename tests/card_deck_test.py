from blackjack.core.deck import Deck
from blackjack.utils.logger import print_card


def main():
    deck1 = Deck()
    for card in deck1.get_deck():
        print_card(card)


if __name__ == '__main__':
    main()
