import argparse
import game


class Parser():
    """
    Handles the commands given by the user, including tracking the list of
    games running and creating/ending games when necessary.

    Limitations: options shouldn't be specified multiple times in the same
    command, that will result in weird behaviour. It generally doesn't make
    sense to do so, but even when it maybe does, it is not guaranteed to work
    as expected.
    """

    def __init__(self):
        self.games = {}
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-c', '--create', type=self.create_game)

    def create_game(self, name):
        if name is None:
            return 'Game name argument is required'
        if name in self.games:
            return 'Game %s already exists' % name
        self.games[name] = game.Game(name)
        return 'Created game %s' % name

    def parse(self, command):
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
