# Fix path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

import webapp2
from twilio import twiml
import logging

class Welcome(webapp2.RequestHandler):
    def get(self):
        r = twiml.Response()

        # Nest the 'say' inside the gather to allow user to skip intro.
        with r.gather(numDigits=4, action='/results') as g:
            g.say('Hello. Please enter your code to retrieve your results.') 

        logging.info('Welcome XML=' + str(r))
        self.response.headers['Content-Type'] = 'text/xml'
        self.response.out.write(str(r))

class Results(webapp2.RequestHandler):
    def post(self):
        Digits = self.request.get('Digits')
        logging.info('Digits=' + str(Digits))

        r = twiml.Response()

        if (Digits == '1234'):
            r.say('Test X, negative. Test Y, positive. Test Z, negative.')
        else:
            r.say('Invalid code')

        self.response.headers['Content-Type'] = 'text/xml'
        self.response.out.write(str(r))

app = webapp2.WSGIApplication([('/', Welcome),
                               ('/results', Results),
                              ],
                              debug=True)
