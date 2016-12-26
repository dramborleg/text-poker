from deuces import Card, Deck
import smsbot
import testbot


class Game():
    """
    Contains a deck of cards that can be accessed by players to play
    various card games.
    """

    def __init__(self, bot, name='kiwi'):
        self.players = []
        self.name = name
        self.deck = Deck()
        self.visible_cards = []
        self.bot = bot
        self.potpies = 0

    def add_player(self, player):
        self.players.append(player)

    def shuffle(self):
        self.deck.shuffle()
        self.visible_cards = []

    def deal(self, ncards):
        for i in range(ncards):
            for p in self.players:
                p.cards.append(self.deck.draw())

    def flip_flop(self):
        """Create flop.
        Flips over 3 cards and makes them publicly visible, as would
        happen when creating the flop in Texas Hold'em.
        """
        self.visible_cards += self.deck.draw(3)

    def flip_cards(self, ncards=1):
        """Like flip_flop, but allows variable number of cards."""
        if ncards == 1:
            self.visible_cards.append(self.deck.draw(ncards))
        else:
            self.visible_cards += self.deck.draw(ncards)

    def query_players(self):
        players = '%s players: ' % self.name
        for p in self.players:
            players += '%s ' % p.tag
        return players

    def query_state(self):
        info = '%s visible cards: ' % self.name
        for c in self.visible_cards:
            info += Card.int_to_pretty_str(c)
        info += ', potpies: %d' % self.potpies
        return info

    def message_players(self, message):
        uids = []
        for p in self.players:
            uids.append(p.uid)
        self.bot.message_players(uids, message)
