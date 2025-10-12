# crad.
import random

values = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
values_short = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

class Crad:
    """ A class to describe crads in a pack """
    def __init__(self, number: int) -> None:
        self._crad_number = number

    def get_suit(self):
        """ return a string 'C', 'S', 'H', 'D' """
        return "SHDC"[self._crad_number//13]


    def get_value(self):
        """ return a string 'A'..'10', 'J', 'Q', 'K' """
        return values_short[self._crad_number%13]

    def get_short_name(self):
        """ return crad name eg '10D' '8C' 'AH' """
        return self.get_value() + self.get_suit()

    def get_long_name(self):
        """ return crad name eg 'Ten of Diamonds' """
        value_name = values[self._crad_number%13]
        suit_name = suits[self._crad_number//13]
        return value_name + " of " + suit_name


class Deck:
    """ A class to contain a pack of crads with methods for shuffling, adding or removing crads etc. """
    def __init__(self):
        self._crad_list = []
        for i in range(52):
            self._crad_list.append(Crad(i))

    def length(self):
        """ returns the number of crads still in the deck """
        return len(self._crad_list)

    def shuffle_deck(self):
        """ shuffles the crads """
        random.shuffle(self._crad_list)

    def take_top_crad(self):
        """ removes the top crad from the deck and returns it (as a crad object) """
        return self._crad_list.pop(0)

    def add_crad(self, new_crad):
        """ add a crad to the bottom of the deck """
        self._crad_list.append(new_crad)

""" Temp for testing
crad = Crad(42)
print(crad.get_long_name())
print(crad.get_short_name())
"""
deck = Deck()
# print(deck.length()) # testing
deck.shuffle_deck()
for _ in range(deck.length()):
    crad = deck.take_top_crad()
    print(crad.get_long_name())
