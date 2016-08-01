class Game():
    """
    Contains all the data and functions relevant to a game of Texas Holdem.
    """

    def __init__(self, name='kiwi'):
        self.players = []
        self.name = name

    def add_player(self, player):
        self.players.append(player)
