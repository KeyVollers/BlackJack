card_value_map = {
    1: "A",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K",
}

card_suit_map = {
    1: "\u2663",  # Clubs
    2: "\u2660",  # Spades
    3: "\u2665",  # Hearts
    4: "\u2666"
}


def print_card(card):
    print(card_value_map[card.get_value()], card_suit_map[card.get_suit()])
