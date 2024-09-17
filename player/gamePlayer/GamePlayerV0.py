from objects.Game import Game
from config import SHOW_GAME_CASH
from player.gamePlayer.AbstractGamePlayer import AbstractGamePlayer


class GamePlayerV0(AbstractGamePlayer):

    def __init__(self, game_storage, decision_strategy):
        super().__init__(game_storage=game_storage, decision_strategy=decision_strategy)

    def play(self):
        if self.decision_strategy is None:
            raise Exception("Decision strategy not set on the game player")

        game = Game()
        game.bet()
        while True:
            if game.state == "IN_GAME":
                decision = self.decision_strategy.take_decision()

                if decision == "HIT":
                    game.hit()
                elif decision == "HOLD":
                    game.hold()

            if game.state == "WON" or game.state == "LOST" or game.state == "TIE":
                if SHOW_GAME_CASH:
                    print(f"\r{game.cash}", end="")
                break
        return game


