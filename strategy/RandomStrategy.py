from strategy.AbstractStrategy import AbstractStrategy
import random


class RandomStrategy(AbstractStrategy):

    def __init__(self):
        super().__init__()

    def take_decision(self, player_hand=None, dealer_hand=None):
        return random.choice(["HIT", "HOLD"])
