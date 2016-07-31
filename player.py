class Player():
    """
    Contains information about players, such as their current in-game status as
    well as their names/identifiers.

    Currency is defined in terms of pi(e)s.
    """

    def __init__(self, tag, pies=0):
        self.tag = tag
        self.pies = pies
        self.game = None
