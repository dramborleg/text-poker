from deuces import Card


class Player():
    """
    Contains information about players, such as their current in-game status as
    well as their names/identifiers.

    Currency is defined in terms of pi(e)s.
    """

    def __init__(self, tag, uid, pies=0):
        self.tag = tag
        self.uid = uid
        self.pies = pies
        self.game = None
        self.cards = []

    def query_state(self):
        ret = 'pies = %d, cards = ' % self.pies
        for c in self.cards:
            ret += Card.int_to_pretty_str(c)
        if self.game is None:
            ret += ', currently not in-game'
        else:
            ret += ', ' + self.game.query_state()
        return ret
