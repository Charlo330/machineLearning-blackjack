from utils import ApiCall


class Session:
    def __init__(self):
        self.state = "NOT_STARTED"
        self.gameWinCount = 0
        self.gameLostCount = 0
        self.gameCount = 0

    def load(self):
        game_json = ApiCall.load()
        if game_json is not None:
            self.state = "STARTED"
