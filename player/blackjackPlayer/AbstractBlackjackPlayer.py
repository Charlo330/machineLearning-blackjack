from abc import ABC, abstractmethod


class AbstractBlackjackPlayer(ABC):

    def __init__(self, session_player):
        self.session_player = session_player

    @abstractmethod
    def start(self):
        pass
