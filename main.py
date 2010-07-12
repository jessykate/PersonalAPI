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


class BioHandler(tornado.web.RequestHandler):
    def get(self):
	pass

class ContactHandler(tornado.web.RequestHandler):
    def get(self):
	contact_info = {
	    'email' : 'jessy.cowansharp@gmail.com',
	    'phone' : '202-360-3967',
	    'twitter' : 'http://twitter.com/jessykate',
	    'web' : 'http://jessykate.com',
	}
	js = json.dumps(contact_info)
	self.set_header("Content-Type", "application/json")
	self.write(js)



class ResumeHandler(tornado.web.RequestHandler):
    def get(self):
	pass


application = tornado.web.Application([
        (r'/', IndexHandler),
        (r'/bio', BioHandler),
        (r'/contact', ContactHandler),
        (r'/resume', ResumeHandler),
        ])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8912)
    tornado.ioloop.IOLoop.instance().start()
