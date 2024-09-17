from abc import ABC, abstractmethod


class AbstractStrategy(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def take_decision(self, player_hand, dealer_hand):
        pass
