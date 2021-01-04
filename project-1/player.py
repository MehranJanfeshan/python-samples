import card


class Player:
    def __init__(self, name):
        self.name = name
        self.all_card = []

    def remove_one(self):
        return self.all_card.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # Adding multiple cards
            self.all_card.extend(new_cards)
        else:
            # Adding one card
            self.all_card.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_card)} cards'


new_player = Player('Jose')

new_deck = card.Deck()
my_card = new_deck.deal_one()
new_player.add_cards([my_card, my_card, my_card, my_card, my_card])
print(new_player)
new_player.remove_one()
print(new_player)
