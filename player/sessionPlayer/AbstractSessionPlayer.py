from abc import ABC, abstractmethod


class AbstractSessionPlayer(ABC):

    def __init__(self, game_player):
        self.game_player = game_player

    @abstractmethod
    def play(self):
        pass
