from blackjack.core.deck import Deck
from blackjack.utils.logger import print_deck, print_card


def main():
    deck1 = Deck()
    print_deck(deck1.get_draw_deck())
#    deck1.shuffle_draw_deck()
#    print_deck(deck1.get_draw_deck())
    print("*******************************")
    print_card(deck1.draw_card())
    print("*****************************")
    print_deck(deck1.get_draw_deck())


if __name__ == '__main__':
    main()
