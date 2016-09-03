import configparser
from twilio.rest import TwilioRestClient


class SMSBot():
    """
    Bot that has the ability to communicate with players proactively
    through SMS messages. It can send messages not only as a response
    to commands sent by players, but also to send messages to all
    players of a game for times when the game changes state in a
    significant way.
    """

    def __init__(self, config_file, max_num_msgs=1024):
        config = configparser.ConfigParser()
        config.read(config_file)
        settings = config['Twilio']
        self.account_sid = settings['ACCOUNT_SID']
        self.auth_token = settings['AUTH_TOKEN']
        self.phone_number = settings['TWILIO_NUMBER']
        self.client = TwilioRestClient(self.account_sid, self.auth_token)
        self.total_msgs = 0
        self.max_num_msgs = max_num_msgs

    def message_players(self, phone_numbers, message):
        for nu in phone_numbers:
            if self.total_msgs < self.max_num_msgs:
                self.client.sms.messages.create(to=nu, from_=self.phone_number,
                                                body=message)
                self.total_msgs += 1
            else:
                return 'Max number of messages reached'
        return ''
