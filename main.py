from deck import Deck
from card_player import Player, Dealer


def deal_first_hand(player, dealer, deck):
    player.get_card(deck.deal_card())
    player.get_card(deck.deal_card())
    dealer.get_card(deck.deal_card())
    dealer.get_card(deck.deal_card())
    print(f"You are dealt: {player.show_hand()}")
    print(f"Dealer is dealt: {dealer.show_first_hand()}")


def get_bet(player_money):
    while True:
        current_bet = int(input("Place your bet: "))
        if current_bet <= 0:
            print("Minimum bet is $1.")
            continue
        elif current_bet > player_money:
            print("You have insufficient funds.")
            continue
        else:
            break
    return current_bet


def get_player_choice():
    while True:
        possible_choices = ['h', 'hit', 's', 'stay']
        player_choice = input("Would you like to hit or stay? ")
        player_choice.lower()

        if player_choice in possible_choices:
            if player_choice == 'h' or player_choice == 'hit':
                return True
            else:
                return False
        else:
            print("That is not a valid option.")
            continue


def player_turn(player, deck):
    while True:
        choice = get_player_choice()
        if choice:
            next_card = deck.deal_card()
            print(f"You are dealt {next_card}")
            player.get_card(next_card)
            print(f"You now have: {player.show_hand()}")
        else:
            return player.check_hand_value()

        if player.check_hand_value() == 21:
            return player.check_hand_value()
        elif player.check_hand_value() > 21:
            return player.check_hand_value()
        else:
            continue


def dealer_turn(dealer, deck):
    dealer_score = dealer.check_hand_value()
    print(f"The dealer has {dealer.show_hand()}")

    if dealer_score >= 17:
        return dealer_score

    while dealer_score <= 16:
        next_card = deck.deal_card()
        print(f"Dealer hits and is dealt {next_card}")
        dealer.get_card(next_card)
        print(f"The Dealer has {dealer.show_hand()}")
        dealer_score = dealer.check_hand_value()

    if dealer_score >= 17 and dealer_score < 22:
        print("The Dealer stays.")
        return dealer_score

    if dealer_score > 21:
        return dealer_score


def main():
    print("Welcome to Blackjack!")

    player = Player()
    dealer = Dealer()

    while True:
        deck = Deck()
        player.reset_hand()
        dealer.reset_hand()
        start_dealing = input(
            f"You are starting with ${player.money}. Would you like to play a hand? ")

        if start_dealing.lower() == 'n' or start_dealing.lower() == 'no':
            print(
                f'K!. Thanks for playing. You leave the game with ${player.money}')
            break
        else:
            this_bet = get_bet(player.money)

            deal_first_hand(player, dealer, deck)

            if player.check_hand_value() == 21 and dealer.check_hand_value() != 21:
                print(f'Blackjack! You win {this_bet * 1.5}')
                player.money += (this_bet + this_bet*1.5)

            elif player.check_hand_value() < 21:
                player_score = player_turn(player, deck)

            if player_score > 21:
                print(
                    f"Your hand value is over 21 and you lose ${this_bet} :(")
                player.money -= this_bet
                if player.money <= 0:
                    print(
                        "You've ran out of money. Please restart this program to try again. Goodbye.")
                    break
                else:
                    continue

            if player_score <= 21:
                dealer_score = dealer_turn(dealer, deck)

            if dealer_score > 21:
                print(f"Dealer busts, you win ${this_bet}")
                player.money += this_bet
                continue

            elif dealer_score > player_score:
                print(f"The dealer wins, you lose ${this_bet} :(")
                player.money -= this_bet
                if player.money <= 0:
                    print(
                        "You've ran out of money. Please restart this program to try again. Goodbye.")
                    break

            elif dealer_score == player_score:
                print("It's a tie!")

            else:
                print(f"You win ${this_bet}")
                player.money += this_bet


main()
