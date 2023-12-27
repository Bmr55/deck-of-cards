class Card:
    DISPLAY_MAP = {
        1: 'A',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: '10',
        11: 'J',
        12: 'Q',
        13: 'K'
    }

    BLACKJACK_VALUE_MAP = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 10,
        12: 10,
        13: 10
    }

    def __init__(self, suit, rank):
        card_format = '{rank}{suit}'
        self.suit = suit
        self.rank = rank
        self.value = card_format.format(rank = self.DISPLAY_MAP[self.rank], suit = self.suit.value)

    def get_blackjack_value(self) -> int:
        return self.BLACKJACK_VALUE_MAP[self.rank]