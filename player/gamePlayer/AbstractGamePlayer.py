from abc import ABC, abstractmethod


class AbstractGamePlayer(ABC):

    def __init__(self, game_storage, decision_strategy):
        self.game_storage = game_storage
        self.decision_strategy = decision_strategy

    @abstractmethod
    def play(self):
        pass
