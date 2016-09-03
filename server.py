import cherrypy
import twilio.twiml
import configparser
import smsbot
import parser


class Processor():
    def __init__(self):
        self.bot = smsbot.SMSBot('twilio.conf')
        self.parser = parser.Parser()

    @cherrypy.expose
    def index(self, **kwargs):
        user = kwargs['From']
        message = kwargs['Body']
        resp_msg = self.parser.parse(message.replace('.', '-'), user, self.bot)
        resp = twilio.twiml.Response()
        resp.message(resp_msg)
        return str(resp)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('server.conf')
    settings = config['Server']
    cherrypy.config.update({'server.socket_host': settings['IP_ADDRESS'],
                            'server.socket_port': int(settings['PORT'])})
    cherrypy.quickstart(Processor())
