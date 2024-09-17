from objects.Game import Game
from config import SHOW_GAME_CASH, LEARNING_MODE
from player.gamePlayer.AbstractGamePlayer import AbstractGamePlayer
from utils.DataHandler import DataHandler


class GamePlayerV2(AbstractGamePlayer):

    def __init__(self, game_storage, decision_strategy):
        super().__init__(game_storage=game_storage, decision_strategy=decision_strategy)

    def play(self, nb_figure_out=0, nb_played_card=0):
        if self.decision_strategy is None:
            raise Exception("Decision strategy not set on the game player")

        data = []
        game = Game()
        game.bet()
        while True:

            if game.state == "IN_GAME":
                nb_figure_out += game.nbFigureOutAfterGame
                nb_played_card += game.nbPlayedCardAfterGame
                player_hand_before = game.playerHand
                dealer_hand_before = game.dealerHand
                nb_figure_out_before = nb_figure_out
                decision = self.decision_strategy.take_decision(player_hand_before, dealer_hand_before)
                if decision == "HIT":
                    game.hit()
                elif decision == "HOLD":
                    game.hold()

                if LEARNING_MODE:
                    if game.state == "WON" or game.state == "TIE" or game.state == "IN_GAME":
                        DataHandler.add_data_with_figure([player_hand_before,
                                                          dealer_hand_before, nb_figure_out_before, decision, "WIN"])
                    else:
                        DataHandler.add_data_with_figure([player_hand_before,
                                                          dealer_hand_before, nb_figure_out_before, decision, "LOST"])

            elif game.state == "WON" or game.state == "TIE":

                if SHOW_GAME_CASH:
                    print(f"\r{game.cash}", end="")
                break

            elif game.state == "LOST":
                if SHOW_GAME_CASH:
                    print(f"\r{game.cash}", end="")
                break
        return game
