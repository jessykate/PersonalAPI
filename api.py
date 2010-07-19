#!/usr/bin/python

# A basic personal API.  
#
# To run:
# ./main.py
# and visit localhost:8888

import tornado.httpserver
import tornado.ioloop
import tornado.web
import urllib, urllib2
import os, datetime
from data import * # all the actual personal information goes here. 

try:
    import json
except:
    import simplejson as json

# settings
BASE_URL = "http://api.jessykate.com"


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
	print dir(application)
	print application.handlers
        self.render('templates/index.html')

class BaseHandler(tornado.web.RequestHandler):
	name = 'Jessy Kate Cowan-Sharp'
	

class BioHandler(tornado.web.RequestHandler):
    def get(self):
	    # XXX TODO format=plaintext, format=html, prettyprint. 
        version = self.get_argument('version', None)
        resp = {'name': NAME, 'date': CURRENT_DATE} 
        if version == 'work':
            resp['bio'] = BIO_WORK
        else:
            resp['bio'] =  BIO_MAIN
        js = json.dumps(resp)
        self.set_header("Content-Type", "application/json")
        self.write(js)
        return

class ContactHandler(tornado.web.RequestHandler):
    def get(self):
	contact_info = {
	    'email' : EMAIL_MAIN, 
	    'phone' : PHONE_MOBILE,
	    'twitter' : TWITTER,
	    'web' : WEBSITE_MAIN,
	}
	js = json.dumps(contact_info)
	self.set_header("Content-Type", "application/json")
	self.write(js)
	return


class ResumeHandler(tornado.web.RequestHandler):
    def get(self):
	pass


application = tornado.web.Application([
        (r'/', IndexHandler),
        (r'/bio.json', BioHandler),
        (r'/contact.json', ContactHandler),
        (r'/resume.json', ResumeHandler),
        ])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8912)
    tornado.ioloop.IOLoop.instance().start()
