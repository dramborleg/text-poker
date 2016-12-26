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

    def reveal(self):
        msg = "%s's cards are" % self.tag
        for c in self.cards:
            msg += ' ' + Card.int_to_pretty_str(c)
        self.cards = []
        if self.game is not None:
            self.game.message_players(msg)
        else:
            return 'Not in game'
        return 'Revealed and discarded hand'

    def acquire(self, numpies):
        self.pies += numpies
        return 'Added %d pies to wallet' % numpies

    def bet(self, numpies):
        if self.game is None:
            return 'Not in game'
        numpies = min(numpies, self.pies)
        self.game.potpies += numpies
        self.pies -= numpies
        return 'Added %d pies to pot' % numpies

    def withdraw(self, numpies):
        if self.game is None:
            return 'Not in game'
        numpies = min(numpies, self.game.potpies)
        self.game.potpies -= numpies
        self.pies += numpies
        return 'Withdrew %d pies from pot' % numpies

    def message_game(self, msg):
        if self.game is not None:
            msg = self.tag + ': ' + msg
            self.game.message_players(msg)
        else:
            return 'Not in game'
        return 'Messaged players'
