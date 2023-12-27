from random import randrange
from .suits import Suits
from .card import Card

class Deck:
    def __init__(self, shuffle:bool=False):
        self.cards = list()
        self.suits = list([Suits.CLUBS, Suits.DIAMONDS, Suits.HEARTS, Suits.SPADES])

        for suit in self.suits:
            card_ranks = range(1, 14)
            for n in card_ranks:
                card = Card(suit, n)
                self.cards.append(card)

        if shuffle:
            self.shuffle()

    def shuffle(self) -> None:
        for i in range(52):
            number_of_cards = len(self.cards)
            random_num_1 = randrange(number_of_cards - 1)
            random_num_2 = randrange(number_of_cards - 1)
            self.swap(random_num_1, random_num_2)

    def swap(self, a:int, b:int) -> None:
        temp = self.cards[a]
        self.cards[a] = self.cards[b]
        self.cards[b] = temp

    def pop(self) -> Card:
        number_of_cards_left = len(self.cards)

        if number_of_cards_left > 0:
            deck_index = number_of_cards_left - 1
            next_card = self.cards.pop(deck_index)
            return next_card
        else:
            return None

    def print_deck(self) -> None:
        for card in self.cards:
            print(card.value + ' ', end='')
        print()
