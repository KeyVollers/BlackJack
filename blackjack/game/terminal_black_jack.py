from blackjack.core.black_jack import BlackJack
from blackjack.utils.logger import print_card


def main():
    blackjack = BlackJack()
    end_game = False
    while not end_game:
        user_input = input("Next: ")

        if user_input == 'q':
            end_game = True
        elif user_input == 'n':
            print_card(blackjack.game_deck.draw_card())

        if len(blackjack.game_deck.get_draw_deck()) == 0:
            end_game = True


if __name__ == '__main__':
    main()