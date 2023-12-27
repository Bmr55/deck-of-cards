# Deck of Cards
Python implementation of a card deck

## Usage

```python
from deck import Deck

# initialize an unshuffled deck
unshuffled_card_deck = Deck()

# initialize a shuffled deck
shuffled_card_deck = Deck(shuffle=True)

# suffle a deck
unshuffled_card_deck.shuffle()

# print a deck
shuffled_card_deck.print_deck()

# get a card
card = shuffled_card_deck.pop()
```

## Example `test.py` output

```
Deck of Cards Test

Unshuffled Deck:
A♣ 2♣ 3♣ 4♣ 5♣ 6♣ 7♣ 8♣ 9♣ 10♣ J♣ Q♣ K♣ A♦ 2♦ 3♦ 4♦ 5♦ 6♦ 7♦ 8♦ 9♦ 10♦ J♦ Q♦ K♦ A♥ 2♥ 3♥ 4♥ 5♥ 6♥ 7♥ 8♥ 9♥ 10♥ J♥ Q♥ K♥ A♠ 2♠ 3♠ 4♠ 5♠ 6♠ 7♠ 8♠ 9♠ 10♠ J♠ Q♠ K♠

Shuffled Deck:
A♦ A♠ 3♣ 10♦ 9♣ 2♥ 10♠ 8♣ 5♠ K♣ 7♠ J♣ 8♠ 9♠ 3♦ 3♠ J♥ 5♦ 5♣ 7♥ J♦ 2♣ Q♣ 10♣ A♥ 8♥ 8♦ 3♥ K♥ 4♥ 5♥ 6♠ 2♦ K♦ 9♥ 6♣ Q♥ 7♦ Q♦ 7♣ 9♦ 6♥ 10♥ 4♦ 4♠ A♣ 4♣ 2♠ 6♦ J♠ Q♠ K♠

Next Card: K♠
Remaining Cards:
A♦ A♠ 3♣ 10♦ 9♣ 2♥ 10♠ 8♣ 5♠ K♣ 7♠ J♣ 8♠ 9♠ 3♦ 3♠ J♥ 5♦ 5♣ 7♥ J♦ 2♣ Q♣ 10♣ A♥ 8♥ 8♦ 3♥ K♥ 4♥ 5♥ 6♠ 2♦ K♦ 9♥ 6♣ Q♥ 7♦ Q♦ 7♣ 9♦ 6♥ 10♥ 4♦ 4♠ A♣ 4♣ 2♠ 6♦ J♠ Q♠

Next Card: Q♠
Remaining Cards:
A♦ A♠ 3♣ 10♦ 9♣ 2♥ 10♠ 8♣ 5♠ K♣ 7♠ J♣ 8♠ 9♠ 3♦ 3♠ J♥ 5♦ 5♣ 7♥ J♦ 2♣ Q♣ 10♣ A♥ 8♥ 8♦ 3♥ K♥ 4♥ 5♥ 6♠ 2♦ K♦ 9♥ 6♣ Q♥ 7♦ Q♦ 7♣ 9♦ 6♥ 10♥ 4♦ 4♠ A♣ 4♣ 2♠ 6♦ J♠
```