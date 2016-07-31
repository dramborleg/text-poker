import argparse
import game
import player


class Parser():
    """
    Handles the commands given by the user, including tracking the list
    of games running and creating/ending games when necessary.

    Limitations:
    - Options shouldn't be specified multiple times in the same command,
      that will result in weird behaviour. It generally doesn't make
      sense to do so, but even when it maybe does, it is not guaranteed
      to work as expected.
    - Players can only participate in one game at a time.
    """

    def __init__(self):
        self.games = {}
        self.players = {}
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-c', '--create', nargs='?', const='GAME_',
                                 type=self.create_game)
        self.parser.add_argument('-j', '--join', type=self.join_game)
        self.parser.add_argument('-t', '--tag', type=self.set_tag)

    def create_game(self, name):
        if name is 'GAME_':
            name += str(len(self.games))
        if name in self.games:
            return ('Game name "%s" collides with another game. '
                    'Please provide a different game name.' % name)
        self.games[name] = game.Game(name)
        return 'Created game %s' % name

    def join_game(self, game_id):
        if (self.current_id in self.players and
            self.players[self.current_id].game is not None):
            return ('You already appear to be in-game. Please quit game '
                    'before joining a new game.')
        elif self.current_id not in self.players:
            self.players[self.current_id] = player.Player(self.current_id)
        if game_id not in self.games:
            return ('Game %s does not exist, please create new game or join '
                    'an existing game' % game_id)
        self.games[game_id].add_player(self.players[self.current_id])
        self.players[self.current_id].game = self.games[game_id]
        return 'Successfully joined game %s' % game_id

    def set_tag(self, player_tag):
        if self.current_id in self.players:
            self.players[self.current_id].tag = player_tag
        else:
            self.players[self.current_id] = player.Player(player_tag)
        return 'Successfully set tag to %s' % player_tag

    def parse(self, command, player_id):
        self.current_id = player_id
        try:
            known, unknown = self.parser.parse_known_args(command.split())
        except:
            return 'Internal error. Incorrect arguments?'
        known_dict = vars(known)
        ret = ''
        prefix = ''
        for opt in known_dict:
            if known_dict[opt] is not None:
                ret += known_dict[opt]
        if len(unknown) > 0:
            if len(ret) > 0:
                prefix = '\n'
            ret += prefix + 'Unknown arguments:'
            for opt in unknown:
                ret += ' ' + opt
        return ret
