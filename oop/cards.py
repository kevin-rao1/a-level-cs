import random

values = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
suits = ["Clubs", "Spades", "Hearts", "Diamonds"]

class Card:
    """ A class to describe cards in a pack """
    def __init__(self, number: int) -> None:
        self._card_number = number

    def get_suit(self):
        """ return a string 'C', 'S', 'H', 'D' """
        return "SHDC"[self._card_number//13]


    def get_value(self):
        """ return a string 'A'..'10', 'J', 'Q', 'K' """
        if self._card_number%12 == 0:
            return "A"
        elif self._card_number%12 == 10:
            return "J"        
        elif self._card_number%12 == 11:
            return "Q"        
        elif self._card_number%12 == 12:
            return "K"
        else:
            return str(self._card_number%12 + 1) # not one of special chars

    def get_short_name(self):
        """ return card name eg '10D' '8C' 'AH' """
        return self.get_value() + self.get_suit()

    def get_long_name(self):
        """ return card name eg 'Ten of Diamonds' """
        value_name = values[self._card_number%12]
        suit_name = suits[self._card_number//13]
        return value_name + " of " + suit_name


class Deck:
    """ A class to contain a pack of cards with methods for shuffling, adding or removing cards etc. """
    def __init__(self):
        self._card_list = []
        for i in range(52):
            self._card_list.append(Card(i))

    def length(self):
        """ returns the number of cards still in the deck """
        pass

    def shuffle_deck(self):
        """ shuffles the cards """
        random.shuffle(self._card_list)

    def take_top_card(self):
        """ removes the top card from the deck and returns it (as a card object) """
        pass

    def add_card(self, new_card):
        """ add a card to the bottom of the deck """
        self._card_list.append(new_card)


card = Card(42)
print(card.get_long_name())
deck = Deck()
deck.shuffle_deck()
for _ in range(deck.length()):
    card = deck.take_top_card()
    print(card.get_long_name())
