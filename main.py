from player.gamePlayer.GamePlayerV0 import GamePlayerV0
from player.gamePlayer.GamePlayerV1 import GamePlayerV1
from player.gamePlayer.GamePlayerV2 import GamePlayerV2

from player.sessionPlayer.SessionPlayerV0 import SessionPlayerV0
from player.sessionPlayer.SessionPlayerV1 import SessionPlayerV1
from player.sessionPlayer.SessionPlayerV2 import SessionPlayerV2

from player.blackjackPlayer.BlackjackPlayerV0 import BlackjackPlayerV0
from player.blackjackPlayer.BlackjackPlayerV1 import BlackjackPlayerV1
from player.blackjackPlayer.BlackjackPlayerV2 import BlackjackPlayerV2

from utils.DataHandler import DataHandler

from strategy.RandomStrategy import RandomStrategy
from strategy.StrategyV1 import StrategyV1
from strategy.StrategyV2 import StrategyV2

from config import VERSION
import config


def main():
    if VERSION == "V0":
        strategy = RandomStrategy()
        game_player = GamePlayerV0(None, strategy)

        session_player = SessionPlayerV0(game_player)

        blackjack_player = BlackjackPlayerV0(session_player)

        blackjack_player.start()

    elif VERSION == "V1":

        if config.LEARNING_MODE:
            strategy = RandomStrategy()
        else:
            strategy = StrategyV1()

        game_player = GamePlayerV1(DataHandler, strategy)

        session_player = SessionPlayerV1(game_player)

        blackjack_player = BlackjackPlayerV1(session_player)

        blackjack_player.start()
        pass

    elif VERSION == "V2":

        if config.LEARNING_MODE:
            strategy = RandomStrategy()
        else:
            strategy = StrategyV2()

        game_player = GamePlayerV2(DataHandler, strategy)

        session_player = SessionPlayerV2(game_player)

        blackjack_player = BlackjackPlayerV2(session_player)

        blackjack_player.start()
        pass


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
