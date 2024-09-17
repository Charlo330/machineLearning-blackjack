from objects.Session import Session
from player.sessionPlayer.AbstractSessionPlayer import AbstractSessionPlayer


class SessionPlayerV0(AbstractSessionPlayer):

    def __init__(self, game_player):
        super().__init__(game_player)

    def play(self):
        session = Session()
        session.load()
        # open the file in the write mode
        while True:

            game = self.game_player.play()

            if game.state == "WON":
                session.gameWinCount += 1

            elif game.state == "LOST":
                session.gameLostCount += 1

            if game.cash <= 0:
                session.state = "LOST"
                break

            if game.cash >= 2000:
                session.state = "WON"
                break

        return session
