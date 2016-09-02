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
        self.parser.add_argument('-c', '--create', nargs='?', const='GAME_')
        self.parser.add_argument('-j', '--join')
        self.parser.add_argument('-t', '--tag')
        self.parser.add_argument('-s', '--shuffle', action='store_true')
        self.parser.add_argument('-d', '--deal', type=int)
        self.parser.add_argument('-f', '--flop', action='store_true')
        self.parser.add_argument('-o', '--overturn', nargs='?', const=1,
                                 type=int)
        self.parser.add_argument('-q', '--query', action='store_true')
        self.parser.add_argument('-p', '--players', action='store_true')
        self.parser.add_argument('-r', '--reveal', action='store_true')
        self.parser.add_argument('-m', '--msg', type=str, nargs='+')

    def create_game(self, bot, name='GAME_'):
        if name is 'GAME_':
            name += str(len(self.games))
        if name in self.games:
            return ('Game name "%s" collides with another game. '
                    'Please provide a different game name. ' % name)
        self.games[name] = game.Game(bot, name)
        return 'Created game %s ' % name

    def get_cur_game(self):
        if self.current_id in self.players:
            return self.players[self.current_id].game
        else:
            return None

    def join_game(self, game_id):
        if (self.current_id in self.players and
            self.players[self.current_id].game is not None):
            return ('You already appear to be in-game. Please quit game '
                    'before joining a new game. ')
        elif self.current_id not in self.players:
            self.players[self.current_id] = player.Player(self.current_id,
                                                          self.current_id)
        if game_id not in self.games:
            return ('Game %s does not exist, please create new game or join '
                    'an existing game ' % game_id)
        self.games[game_id].add_player(self.players[self.current_id])
        self.players[self.current_id].game = self.games[game_id]
        return 'Successfully joined game %s ' % game_id

    def set_tag(self, player_tag):
        if self.current_id in self.players:
            self.players[self.current_id].tag = player_tag
        else:
            self.players[self.current_id] = player.Player(player_tag,
                                                          self.current_id)
        return 'Successfully set tag to %s ' % player_tag

    def shuffle(self):
        game = self.get_cur_game()
        if game is not None:
            game.shuffle()
        return ''

    def deal(self, ncards):
        game = self.get_cur_game()
        if game is not None:
            game.deal(ncards)
        return ''

    def flip_flop(self):
        game = self.get_cur_game()
        if game is not None:
            game.flip_flop()
        return ''

    def overturn(self, ncards):
        game = self.get_cur_game()
        if game is not None:
            game.flip_cards(ncards)
        return ''

    def reveal(self):
        if self.current_id in self.players:
            return self.players[self.current_id].reveal()
        else:
            return 'Not a player'

    def query_state(self):
        if self.current_id in self.players:
            return self.players[self.current_id].query_state()
        else:
            return 'Not a player, no info to query '

    def query_players(self):
        game = self.get_cur_game()
        if game is not None:
            return game.query_players()
        else:
            return 'Not participating in a valid game '

    def msg(self, msg):
        if self.current_id in self.players:
            return self.players[self.current_id].message_game(msg)
        else:
            return 'Not a player'

    def parse(self, command, player_id, bot):
        self.current_id = player_id
        try:
            known, unknown = self.parser.parse_known_args(command.split())
        except:
            return 'Internal error. Incorrect arguments? '
        ret = ''
        if known.create:
            ret += self.create_game(bot, known.create)
        if known.join:
            ret += self.join_game(known.join)
        if known.tag:
            ret += self.set_tag(known.tag)
        if known.shuffle:
            ret += self.shuffle()
        if known.deal is not None and known.deal > 0:
            ret += self.deal(known.deal)
        if known.flop:
            ret += self.flip_flop()
        if known.overturn is not None and known.overturn > 0:
            ret += self.overturn(known.overturn)
        if known.reveal:
            ret += self.reveal()
        if known.query:
            ret += self.query_state()
        if known.players:
            ret += self.query_players()
        if known.msg:
            ret += self.msg(' '.join(known.msg))
        prefix = ''
        if len(unknown) > 0:
            if len(ret) > 0:
                prefix = '\n'
            ret += prefix + 'Unknown arguments:'
            for opt in unknown:
                ret += ' ' + opt
        return ret
