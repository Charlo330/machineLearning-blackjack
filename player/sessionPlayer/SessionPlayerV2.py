from objects.Session import Session
from player.sessionPlayer.AbstractSessionPlayer import AbstractSessionPlayer


class SessionPlayerV2(AbstractSessionPlayer):

    def __init__(self, game_player):
        super().__init__(game_player)
        self.nbFigureOut = 0
        self.nbPlayedCard = 0

    def play(self):
        session = Session()
        session.load()
        # open the file in the write mode
        while True:
            game = self.game_player.play(self.nbFigureOut, self.nbPlayedCard)

            self.nbPlayedCard += game.nbPlayedCardAfterGame
            self.nbFigureOut += game.nbFigureOutAfterGame

            if self.nbPlayedCard >= 18:
                self.nbPlayedCard = 0
                self.nbFigureOut = 0

            session.gameCount += 1
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
