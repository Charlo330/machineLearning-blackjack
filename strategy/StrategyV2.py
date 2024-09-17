from strategy.AbstractStrategy import AbstractStrategy
from utils.DataHandler import DataHandler
from strategy.RandomStrategy import RandomStrategy


class StrategyV2(AbstractStrategy):

    def __init__(self):
        super().__init__()

    def take_decision(self, player_hand, dealer_hand, nb_figure_out=0):
        decision = DataHandler.get_data_by_player_dealer_hand_figure_out(player_hand, dealer_hand, nb_figure_out)
        if decision is None:
            return RandomStrategy.take_decision(RandomStrategy())

        return decision
