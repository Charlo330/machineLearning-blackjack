import json

from utils import ApiCall


class Game:
    def __init__(self):
        self.state = "IDLE"
        self.cash = 0
        self.dealerHand = []
        self.playerHand = []
        self.nbPlayedCardAfterGame = 0
        self.nbFigureOutAfterGame = 0

    def bet(self):
        game = ApiCall.bet(50)
        if game is not None:
            self.state = game["state"]
            self.cash = game["cash"]
            self.nbPlayedCardAfterGame = len(game["dealerHand"]) + len(game["playerHand"])

            self.nbFigureOutAfterGame = (check_number_of_figures(game["dealerHand"])
                                         + check_number_of_figures(game["playerHand"]))

            self.dealerHand = calculate_hand_value(game["dealerHand"])
            self.playerHand = calculate_hand_value(game["playerHand"])

    def hit(self):
        game = ApiCall.hit()
        if game is not None:
            self.state = game["state"]
            self.cash = game["cash"]
            self.nbPlayedCardAfterGame = len(game["dealerHand"]) + len(game["playerHand"])

            self.nbFigureOutAfterGame = (check_number_of_figures(game["dealerHand"])
                                         + check_number_of_figures(game["playerHand"]))

            self.dealerHand = calculate_hand_value(game["dealerHand"])
            self.playerHand = calculate_hand_value(game["playerHand"])

    def hold(self):
        game = ApiCall.hold()
        if game is not None:
            self.state = game["state"]
            self.cash = game["cash"]
            self.nbPlayedCardAfterGame = len(game["dealerHand"]) + len(game["playerHand"])

            self.nbFigureOutAfterGame = (check_number_of_figures(game["dealerHand"])
                                         + check_number_of_figures(game["playerHand"]))

            self.dealerHand = calculate_hand_value(game["dealerHand"])
            self.playerHand = calculate_hand_value(game["playerHand"])


def calculate_hand_value(current_hand):
    """Calculates the value of a blackjack hand."""
    total_value = 0
    num_aces = 0

    hand = []
    for card_value in current_hand:
        hand.append(card_value['rank'])

    for card in hand:
        if card in ['J', 'Q', 'K']:
            total_value += 10
        elif card == 'A':
            num_aces += 1
            total_value += 11  # Assume 11 for now, we'll adjust later if needed
        else:
            total_value += int(card)

    # Adjust the value for aces
    while num_aces > 0 and total_value > 21:
        total_value -= 10  # Change the value of an ace from 11 to 1
        num_aces -= 1
    return total_value


def check_number_of_figures(hand):
    total_figure = 0
    for card in hand:
        if card['rank'] in ['J', 'Q', 'K']:
            total_figure += 1
    return total_figure


