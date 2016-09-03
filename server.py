import cherrypy
import twilio.twiml
import configparser
import smsbot


class Processor():
    def __init__(self):
        self.bot = smsbot.SMSBot('twilio.conf')

    @cherrypy.expose
    def index(self, **kwargs):
        resp = twilio.twiml.Response()
        resp.message('HelloWorld')
        return str(resp)

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('server.conf')
    settings = config['Server']
    cherrypy.config.update({'server.socket_host': settings['IP_ADDRESS'],
                            'server.socket_port': int(settings['PORT'])})
    cherrypy.quickstart(Processor())
