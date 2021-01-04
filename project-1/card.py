import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        # Random changes the list and does not return back anything!
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


if __name__ == '__main__':
    new_deck = Deck()
    new_deck.shuffle()
    print(len(new_deck.all_cards))
    my_card = new_deck.deal_one()
    print(my_card)
    print(len(new_deck.all_cards))
    for card in new_deck.all_cards:
        print(card)
