

class Player:

    starting_amount = 500

    def __init__(self):
        self.hand = []
        self.money = Player.starting_amount

    def get_card(self, card):
        self.hand.append(card)

    def check_hand_value(self):
        total = 0

        hand_value = [card[0] for card in self.hand]

        if 'A' in hand_value:
            hand_value.pop(hand_value.index('A'))
            for item in hand_value:
                if item.isdigit():
                    total += int(item)
                elif item in ['T', 'J', 'Q', 'K']:
                    total += 10
            if total >= 12:
                return total + 1
            else:
                return total + 11
        else:
            for item in hand_value:
                if item.isdigit():
                    total += int(item)
                elif item in ['T', 'J', 'Q', 'K']:
                    total += 10
            return total

    def show_hand(self):
        show_hand = ''
        for card in self.hand:
            show_hand = show_hand + card + ','

        return show_hand[:-1]

    def reset_hand(self):
        self.hand = []


class Dealer(Player):

    def __init__(self):
        self.hand = []

    def show_first_hand(self):
        return f"{self.hand[0]}, Unknown"
