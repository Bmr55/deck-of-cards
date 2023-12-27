from deck import Deck

def pop_and_print(card_deck: Deck) -> None:
    card = card_deck.pop()
    print('\nNext Card: ' + card.value)
    print('Remaining Cards:')
    card_deck.print_deck()

def main() -> None:
    card_deck = Deck()

    print('Deck of Cards Test\n')

    print('Unshuffled Deck:')
    card_deck.print_deck()
    print()

    card_deck.shuffle()

    print('Shuffled Deck:')
    card_deck.print_deck()

    pop_and_print(card_deck)
    pop_and_print(card_deck)

if __name__ == '__main__':
    main()