class TestBot():
    """
    Test bot that "messages" players on terminal.
    """

    def message_players(self, uids, message):
        for uid in uids:
            print(str(uid) + ': ' + message)
