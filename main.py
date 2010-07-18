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

class BaseHandler(tornado.web.RequestHandler):
	name = 'Jessy Kate Cowan-Sharp'
	

class BioHandler(tornado.web.RequestHandler):
    def get(self):
	# XXX TODO format=plaintext, format=html
	date = "2010-07-18" # year-month-day
	bio = '''Jessy Cowan-Sharp is an urban hacker, an alchemist of social systems, and a communities scientist. She currently works at the Sunlight Foundation, a DC-based open government think tank, writing code to jump start the next generation of participatory citizenry. Previous to Sunlight, Jessy was at NASA working on the Nebula cloud computing platform. Jessy's research interests focus on the study of patterns in human behaviour, organization, and governance; and the development of  platforms to facilitate collaboration and creativity.  She is variously involved in open source software development, open education, intentional housing, cooking and crossfit.  Find her @jessykate or online. '''
	resp = {'name': 'Jessy Kate Cowan-Sharp', 'date': date, 'bio': bio}
	js = json.dumps(resp)
	self.set_header("Content-Type", "application/json")
	self.write(js)
	return

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
