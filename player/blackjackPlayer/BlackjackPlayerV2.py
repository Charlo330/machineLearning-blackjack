from config import SHOW_SESSION_COUNT, SHOW_SESSION_RESULT, APPEND_LOG, STOP_AFTER_N_SESSION, STORE_AFTER_N_SESSION
from utils import csvHandler
from player.blackjackPlayer.AbstractBlackjackPlayer import AbstractBlackjackPlayer
from utils.DataHandler import DataHandler

global nb_session


class BlackjackPlayerV2(AbstractBlackjackPlayer):

    def __init__(self, session_player):
        super().__init__(session_player)

    def start(self):
        if self.session_player is None:
            raise Exception("Session player not set on the blackjack player")

        print("=====================================", end="")
        global nb_session
        nb_session = 0
        count_session = 0
        data = []
        total_win, total_lost, total_game_count = csvHandler.get_total_game_win_lost()
        DataHandler.init_data()

        while True:
            session = self.session_player.play()
            game_win = session.gameWinCount
            game_lost = session.gameLostCount
            game_count = session.gameCount

            DataHandler.store_data()

            total_win += game_win
            total_lost += game_lost
            total_game_count += game_count
            count_session += 1
            nb_session += 1
            show_session_output(game_win, game_lost)

            # get the average win rate
            data.append([game_win, game_lost, game_count, total_win / total_game_count])

            if count_session >= STORE_AFTER_N_SESSION:
                csvHandler.write_data(data)
                count_session = 0
                data = []

            if STOP_AFTER_N_SESSION != 0 and nb_session >= STOP_AFTER_N_SESSION:
                break


def show_session_output(game_win, game_lost):
    global nb_session
    print("\r\033[K", end="") if APPEND_LOG else print("\n")
    if SHOW_SESSION_COUNT:
        print(f"Session: {str(nb_session)}", end=" | ")
    if SHOW_SESSION_RESULT:
        print(f"\033[92mGame Win: {str(game_win)} \033[91mGame Lost: {str(game_lost)}\033[0m", end="")
